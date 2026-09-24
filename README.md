# E-Commerce Data Collection and Pre-Processing

This project demonstrates an end-to-end data engineering workflow using a synthetic e-commerce transaction dataset containing 500 records.
The workflow includes data loading, Python data structures, profiling, data cleaning, transformations, feature engineering, aggregation, and serialization.
A `Transaction` class is used to organize reusable cleaning and calculation logic.
Statistics Canada open data is used as a secondary metadata source for Canadian city information.
The cleaned transaction data is saved in both CSV and JSON formats.

## Quick Start

Create a virtual environment:

```bash
python -m venv venv
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open `ecommerce_data_engineering.ipynb` and run the notebook from top to bottom.

## Data Sources

- **Primary dataset:** Synthetic e-commerce transaction dataset generated using Python and Faker.
- **Secondary dataset:** Statistics Canada, *Population and dwelling counts: Canada and census subdivisions (municipalities)*, Table 98-10-0002-01.
- Statistics Canada source: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810000201

## Project Structure

```text
DataCollectionAndPre-processing_PROG8245/
├── data/
├── src/
│   ├── generate_ecommerce_data.py
│   └── transaction.py
├── ecommerce_data_engineering.ipynb
├── README.md
├── requirements.txt
└── .gitignore
```