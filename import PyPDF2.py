import PyPDF2
import os

def parse_and_rename_pdf(input_pdf_path, output_folder):
    # Liste des noms pour chaque lettre de motivation
    companies = [
        "Sanofi", "Genfit", "CIC-IT", "Pegasus Data and Analytics", "Aliri Bioanalysis",
        "AlzProtect", "Aquilab", "Aurora", "Axorus", "Bayer Healthcare", "Bioversys SAS",
        "Bluegriot", "C2RC", "Caerus Medical", "Carma", "Centre de référence maladies rares",
        "Centre oscar lambret", "Cerim", "chu lille", "Caduvet", "Clubster nsl", "Diagast",
        "Efs hfno", "Digestscience", "Gd biotech (gènes diffusion)", "Genosplice technology",
        "Giphar technologies (pharmavision)", "Hcs pharma", "Hnl fipsico",
        "Intestinal biotech development", "Impecs", "inbrain pharma", "innobiochips",
        "ircl plateforme de génomique", "isetim cefimis", "japet medical",
        "jparc centre de recherche JP Aubert", "laboratoire de virologie",
        "laboratoire midac", "laboratoire QBD", "lattice medical", "lesaffre puricenter",
        "lfb biotechnologies", "lso medical", "m2SV", "mblc", "mdms mdoloris medical systems",
        "ocr oncovet clinical research", "polyplus", "presage plateforme",
        "Registre général des cancers", "rnmcd", "4P pharma", "adinov", "laboratoire sanios",
        "ansara pharmacare", "boiron laboratoires", "eurofins laboratoire",
        "laboratoire chanflor", "laboratoires biové (inovet)", "cerballiance", "BioMérieux"
    ]

    with open(input_pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        for i, page in enumerate(pdf_reader.pages):
            # Récupérer le texte de la page
            text = page.extract_text()
            
            # Construire le nom du fichier
            letter_name = companies[i].replace(" ", "_").capitalize()
            output_file_path = os.path.join(output_folder, f"Lettre_motivation_{letter_name}.pdf")
            
            # Écrire la page dans un nouveau PDF
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(page)
            
            with open(output_file_path, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

if __name__ == "__main__":
    input_pdf_path = "C:/Users/Sarani/Desktop/Motivation_alternance.pdf"
    output_folder = "C:/Users/Sarani/Desktop"
    parse_and_rename_pdf(input_pdf_path, output_folder)
