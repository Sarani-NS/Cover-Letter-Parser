# PDF Motivation Letter Parsing and Renaming Script

## Objective
This Python script is designed to parse a PDF file containing motivation letters on each page and save them as individual PDF files, each named according to a provided list of company names.

## Prerequisites
- Python 3.x
- PyPDF2 Library (`pip install PyPDF2`)
- A PDF input file with individual cover letters on each page.
- A list of the companies to which you are willing to submit job applications.

## Usage
1. Make sure you have Python 3.x installed on your system.
2. Install the PyPDF2 library by running `pip install PyPDF2` in your terminal or command prompt.
3. Substitute the placeholder text "Actual_Company_Name_1..." with the names of the specific companies you are submitting applications to. Make certain that the initial company name aligns with the appropriate cover letter in your input PDF.
4. Replace "path/to/your/document.pdf" with the actual path to your PDF document in the script.
5. Replace "path/to/output/folder" with the path where you want to save the resulting PDFs.
6. Run the script using `python script.py` in your terminal or command prompt.

## File Naming Structure
Each generated PDF file will be named according to the following pattern: `Motivation_Letter_Company_Name.pdf`.

## Example Usage
```bash
python script.py
