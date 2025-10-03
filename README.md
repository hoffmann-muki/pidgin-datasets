# Pidgin-English Translation Dataset

This repository contains a cleaned and processed dataset of English-Pidgin translation pairs, along with the scripts used to process the data.

## Dataset Overview

- **Language Pair**: English ↔ Nigerian Pidgin (PCM)
- **Total Pairs**: 22,001 translation pairs
- **Source**: Religious texts (cleaned of biblical references and religious terminology)
- **Format**: Tab-separated pairs ready for machine learning training

## Files

### Processed Datasets
- `pidgin-english-pairs/pidgin-english-pairs.txt` - **Final dataset**: Clean translation pairs in format `pidgin-text\t\tengglish-text`
- `pidgin-english-pairs/pidgin-english-data-cleaned.txt` - Intermediate cleaned data with structure
- `pidgin-english-pairs/pidgin-english-data.txt` - Initial converted data from parquet

### Processing Scripts
- `pidgin-english-pairs/parquet-to-txt-conversion.py` - Converts parquet files to text format
- `pidgin-english-pairs/clean-pidgin-references.py` - Removes biblical references, religious terms, and formatting artifacts
- `pidgin-english-pairs/convert-to-pairs.py` - Converts structured data to simple pairs format

### Source Data
- `pidgin-english-pairs/*.parquet` - Original parquet files

## Dataset Statistics

| Metric | Value |
|--------|-------|
| Translation Pairs | 22,001 |
| Final File Size | 3.6 MB |
| Languages | English, Nigerian Pidgin |
| Format | Tab-separated pairs |

## Data Processing Pipeline

1. **Extract**: Convert parquet files to structured text (`parquet-to-txt-conversion.py`)
2. **Clean**: Remove biblical references, religious terms, and formatting (`clean-pidgin-references.py`)
3. **Format**: Convert to simple pairs format (`convert-to-pairs.py`)

## Usage

### For Machine Learning Training

The final dataset `pidgin-english-pairs.txt` is ready for use with language models:

```python
# Example: Load the dataset
with open('pidgin-english-pairs/pidgin-english-pairs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        pidgin_text, english_text = line.strip().split('\t\t')
        # Your training code here
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

[Add your license information here]

## Citation

If you use this dataset, please cite:

```
[Add citation information here]
```
