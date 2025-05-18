# ORCID Data Extractor and Report Generator

This Python script extracts ORCID information from a file containing ORCID IDs and generates reports in various formats (TXT, PDF, JSON, CSV, Excel).

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [License](#license)
- [Contributions](#contributions)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/orcid-extractor.git
   cd orcid-extractor
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

### Command-Line Arguments

The script accepts the following command-line arguments:

- `--inputfile`: Path to the input file containing ORCID IDs.
- `--output-format`: Specify one or more output formats (txt, pdf, json). Example: `--output-format txt pdf json`. 
- `--report`: Specify if you want to generate a CSV or Excel report.

### Example Commands

1. Extract ORCID data and generate TXT, PDF, and JSON reports:
    ```bash
    python main.py --inputfile orcid_ids.txt --output-format txt pdf json
2. Extract ORCID data and generate a CSV report:
    ```bash
    python main.py --inputfile orcid_ids.txt --output-format txt --report csv
3. Extract ORCID data and generate an Excel report:
    ```bash
    python main.py --inputfile orcid_ids.txt --output-format json --report excel

### Input File Format

The input file should contain one ORCID ID per line. Example (`orcid_ids.txt`):

    0000-0002-1825-0097
    0000-0001-5109-3700
    0000-0002-1694-233X

### Output Files

The generated reports will be saved in the Result directory. The directory structure will look like this:

    Result/
    ├── 0000-0002-1825-0097.txt
    ├── 0000-0002-1825-0097.pdf
    ├── 0000-0002-1825-0097.json
    ├── orcid_report.csv
    └── orcid_report.xlsx

## Features

- **ORCID Data Extraction**: Extracts detailed information from ORCID IDs.
- **Multiple Output Formats**: Supports TXT, PDF, JSON, CSV, and Excel formats.
- **Customizable Reports**: Generate reports based on specific requirements.
- **Error Handling**: Handles missing or invalid data gracefully.

## Dependencies

- **argparse**: For parsing command-line arguments.
- **reportlab**: For generating PDF reports.
- **pandas**: For generating CSV and Excel reports.
- **orcid_extractor**: Custom module for extracting ORCID data.

To install the dependencies, run:

    pip install -r requirements.txt

## License

This project is licensed under the MIT License. See the [LICENSE]() file for details.

## Contributions

For any questions or issues, please open an issue on the GitHub repository.
