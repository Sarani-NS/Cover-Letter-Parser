import PyPDF2
import os

def parse_and_rename_pdf(input_pdf_path, output_folder):
    # List of names for each motivation letter
    companies = [
        "Company_Name_1", "Company_Name_2", "Company_Name_3", "Company_Name_4", "Company_Name_5",
        "Company_Name_6", "Company_Name_7", "Company_Name_8", "Company_Name_9", "Company_Name_10",
        "Company_Name_11", "Company_Name_12", "Company_Name_13", "Company_Name_14", "Company_Name_15",
        "Company_Name_16", "Company_Name_17", "Company_Name_18", "Company_Name_19", "Company_Name_20",
        "Company_Name_21", "Company_Name_22", "Company_Name_23", "Company_Name_24", "Company_Name_25",
        "Company_Name_26", "Company_Name_27", "Company_Name_28", "Company_Name_29", "Company_Name_30",
        "Company_Name_31", "Company_Name_32", "Company_Name_33", "Company_Name_34", "Company_Name_35",
        "Company_Name_36", "Company_Name_37", "Company_Name_38", "Company_Name_39", "Company_Name_40",
        "Company_Name_41", "Company_Name_42", "Company_Name_43", "Company_Name_44", "Company_Name_45",
        "Company_Name_46", "Company_Name_47", "Company_Name_48", "Company_Name_49", "Company_Name_50",
        "Company_Name_51", "Company_Name_52", "Company_Name_53", "Company_Name_54", "Company_Name_55",
        "Company_Name_56", "Company_Name_57", "Company_Name_58", "Company_Name_59", "Company_Name_60"
    ]

    with open(input_pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        for i, page in enumerate(pdf_reader.pages):
            # Get the text from the page
            text = page.extract_text()
            
            # Build the filename
            letter_name = companies[i].replace(" ", "_").capitalize()
            output_file_path = os.path.join(output_folder, f"Motivation_Letter_{letter_name}.pdf")
            
            # Write the page into a new PDF
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(page)
            
            with open(output_file_path, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

if __name__ == "__main__":
    input_pdf_path = "path/to/your/document.pdf"
    output_folder = "path/to/output/folder"
    parse_and_rename_pdf(input_pdf_path, output_folder)
