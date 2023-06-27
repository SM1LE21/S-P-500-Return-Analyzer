# S&P 500 Return Analyzer

## Description
This Python script processes historical S&P 500 data, computes daily returns, annualizes them, and organizes them yearly. It further calculates the expected market return.

## Usage
1. Ensure that you have a file named `SPX.csv` in your directory. This file should contain historical S&P 500 data in the format: 'Date,Close'. 

2. Run the script with Python:

```bash
python3 spx_return_analyzer.py
```

The script will output yearly average returns, annualized returns, and the expected market return.

## Requirements
- Python 3.x
- csv and datetime modules (part of Python's standard library)

## Note
Please use this script responsibly and acknowledge that historical returns are not indicative of future performance.
