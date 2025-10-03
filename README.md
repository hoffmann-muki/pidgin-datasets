# Pidgin-English Translation Dataset

This repository contains cleaned and processed datasets of English-Pidgin translation pairs and monolingual Pidgin sentences, along with the scripts used to process the data.

## Dataset Overview

### Translation Pairs Dataset
- **Language Pair**: English ↔ Nigerian Pidgin (PCM)
- **Total Pairs**: 22,001 translation pairs
- **Original Source**: [OPUS MT560 Dataset](https://opus.nlpl.eu/MT560)
- **Hugging Face Dataset**: [michsethowusu/english-nigerian-pidgin_sentence-pairs_mt560](https://huggingface.co/datasets/michsethowusu/english-nigerian-pidgin_sentence-pairs_mt560)
- **Source Content**: Religious texts (cleaned of biblical references and religious terminology)
- **Format**: Tab-separated pairs ready for machine learning training
- **License**: CC-BY-4.0 (Creative Commons Attribution 4.0 International)

### Monolingual Pidgin Dataset
- **Language**: Nigerian Pidgin (PCM) only
- **Total Sentences**: 176,843 sentences
- **Original Source**: [AfriBERTa Corpus](https://huggingface.co/datasets/castorini/afriberta-corpus)
- **Source Content**: BBC news articles and Common Crawl data
- **Format**: One sentence per line, ready for language model pretraining
- **License**: Apache-2.0

## Files

### Translation Pairs Dataset
- `pidgin-english-pairs/pidgin-english-pairs.txt` - **Final dataset**: Clean translation pairs in format `pidgin-text\t\tengglish-text`
- `pidgin-english-pairs/pidgin-english-data-cleaned.txt` - Intermediate cleaned data with structure
- `pidgin-english-pairs/pidgin-english-data.txt` - Initial converted data from parquet

### Monolingual Pidgin Dataset
- `pidgin-only/pidgin-sentences.txt` - **Final dataset**: 176,843 Nigerian Pidgin sentences (52.3 MB)
- `pidgin-only/train.txt` - Original training split from AfriBERTa corpus (161,843 sentences)
- `pidgin-only/eval.txt` - Original evaluation split from AfriBERTa corpus (15,000 sentences)

### Processing Scripts
- `pidgin-english-pairs/parquet-to-txt-conversion.py` - Converts parquet files to text format
- `pidgin-english-pairs/clean-pidgin-references.py` - Removes biblical references, religious terms, and formatting artifacts
- `pidgin-english-pairs/convert-to-pairs.py` - Converts structured data to simple pairs format
- `pidgin-only/combine-pidgin-data.py` - Combines train.txt and eval.txt into single file

### Source Data
- `pidgin-english-pairs/*.parquet` - Original parquet files

## Dataset Statistics

| Dataset | Metric | Value |
|---------|--------|-------|
| **Translation Pairs** | Pairs | 22,001 |
| | File Size | 3.6 MB |
| | Languages | English ↔ Nigerian Pidgin |
| | Format | Tab-separated pairs |
| **Monolingual Pidgin** | Sentences | 176,843 |
| | File Size | 52.3 MB |
| | Language | Nigerian Pidgin only |
| | Format | One sentence per line |

## Data Processing Pipeline

1. **Source**: Downloaded from [Hugging Face dataset](https://huggingface.co/datasets/michsethowusu/english-nigerian-pidgin_sentence-pairs_mt560)
2. **Extract**: Convert parquet files to structured text (`parquet-to-txt-conversion.py`)
3. **Clean**: Remove biblical references, religious terms, and formatting (`clean-pidgin-references.py`)
4. **Format**: Convert to simple pairs format (`convert-to-pairs.py`)

## Dataset Attribution

### Translation Pairs Dataset
This dataset is derived from the **OPUS MT560 dataset**, which contains parallel sentences extracted from religious texts. The original dataset was created by **michsethowusu** and is available on Hugging Face. Our processing pipeline has:

- ✅ **Removed religious content**: Biblical references like `( Jas . 1 : 25 )` and terms like "Jehovah", "Witness"
- ✅ **Cleaned formatting**: Removed enumeration patterns `( a )`, `( b )` and leading non-alphabetic characters  
- ✅ **Standardized structure**: Converted to clean tab-separated pairs format
- ✅ **Maintained quality**: Preserved all 22,001 translation pairs with improved readability

### Monolingual Pidgin Dataset
This dataset is a subset from the **AfriBERTa Corpus**, which was used to pretrain AfriBERTa language models. The corpus contains text from BBC news website and Common Crawl data. Our dataset includes:

- ✅ **Complete coverage**: Combined train and evaluation splits from original dataset
- ✅ **News domain**: Mostly BBC news content in Nigerian Pidgin
- ✅ **Large scale**: 176,843 sentences suitable for language model pretraining
- ✅ **Clean format**: One sentence per line, ready for processing

## Usage

### For Translation Model Training

The translation pairs dataset `pidgin-english-pairs.txt` is ready for use with machine translation models:

```python
# Example: Load the translation dataset
with open('pidgin-english-pairs/pidgin-english-pairs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        pidgin_text, english_text = line.strip().split('\t\t')
        # Your translation model training code here
```

### For Language Model Pretraining

The monolingual pidgin dataset `pidgin-sentences.txt` is ready for language model pretraining:

```python
# Example: Load the monolingual dataset
with open('pidgin-only/pidgin-sentences.txt', 'r', encoding='utf-8') as f:
    for line in f:
        pidgin_sentence = line.strip()
        # Your language model pretraining code here
```

### Re-running the Processing Pipeline

```bash
# Step 1: Convert parquet to text (if needed)
cd pidgin-english-pairs
python parquet-to-txt-conversion.py

# Step 2: Clean the data
python clean-pidgin-references.py

# Step 3: Convert to pairs format
python convert-to-pairs.py
```

## Environment Setup

The processing was done using conda environment:

```bash
conda create -n pidgin-data-env python=3.11
conda activate pidgin-data-env
pip install pandas pyarrow fastparquet
```

## Data Quality

✅ **Clean sentence beginnings** - No enumeration patterns or non-alphabetic prefixes  
✅ **Religious content removed** - Biblical references and religious terminology cleaned  
✅ **Consistent formatting** - Ready for ML training  
✅ **Error-free parsing** - All 22,001 pairs successfully processed  

## License

This dataset is released under the **Creative Commons Attribution 4.0 International License** (CC-BY-4.0).

## Citation

If you use this dataset, please cite:

**Original OPUS MT560 Dataset:**
```
Please refer to the citation guide of the original OPUS MT560 dataset.
```

**Hugging Face Dataset:**
```
@dataset{michsethowusu_english_nigerian_pidgin_2024,
  title={English-Nigerian Pidgin Parallel Dataset},
  author={michsethowusu},
  year={2024},
  url={https://huggingface.co/datasets/michsethowusu/english-nigerian-pidgin_sentence-pairs_mt560},
  license={CC-BY-4.0}
}
```

**AfriBERTa Corpus:**
```
@inproceedings{ogueji-etal-2021-small,
    title = "Small Data? No Problem! Exploring the Viability of Pretrained Multilingual Language Models for Low-resourced Languages",
    author = "Ogueji, Kelechi  and
      Zhu, Yuxin  and
      Lin, Jimmy",
    booktitle = "Proceedings of the 1st Workshop on Multilingual Representation Learning",
    month = nov,
    year = "2021",
    address = "Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.mrl-1.11",
    pages = "116--126",
}
```

**This Cleaned Version:**
```
@dataset{pidgin_english_cleaned_2025,
  title={Cleaned Pidgin-English Translation Dataset},
  year={2025},
  note={Processed from michsethowusu/english-nigerian-pidgin_sentence-pairs_mt560 and castorini/afriberta-corpus},
  description={22,001 English-Pidgin translation pairs and 176,843 monolingual Pidgin sentences}
}
```
