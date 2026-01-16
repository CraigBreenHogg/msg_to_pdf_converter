from importlib.resources import path
import os
import extract_msg
from fpdf import FPDF

def convert_msg_to_pdf(msg_file_path, output_pdf_path):
    try:
        msg = extract_msg.Message(msg_file_path)
        msg_subject = msg.subject or "No Subject"
        msg_sender = msg.sender or "Unknown Sender"
        msg_to = msg.to or "Unknown Recipient"
        msg_date = msg.date or "Unknown Date"
        msg_body = msg.body or "No Body Content"
        attachments = msg.attachments

        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)

        pdf.multi_cell(0, 10, f"Subject: {msg_subject}")
        pdf.multi_cell(0, 10, f"From: {msg_sender}")
        pdf.multi_cell(0, 10, f"To: {msg_to}")
        pdf.multi_cell(0, 10, f"Date: {msg_date}")
        pdf.ln(10)
        pdf.multi_cell(0, 10, "Body:")
        pdf.multi_cell(0, 10, msg_body)

        if attachments:
            pdf.ln(10)
            pdf.multi_cell(0, 10, "Attachments:")
            for attachment in attachments:
                pdf.multi_cell(0, 10, f"- {attachment.longFilename or attachment.shortFilename}")

        pdf.output(output_pdf_path)
        print(f"Converted '{msg_file_path}' to '{output_pdf_path}' successfully.")
    except Exception as e:
        print(f"Error converting '{msg_file_path}': {e}")

def batch_convert_msg_to_pdf(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".msg"):
            msg_path = os.path.join(folder_path, filename)
            pdf_filename = os.path.splitext(filename)[0] + ".pdf"
            pdf_path = os.path.join(output_folder, pdf_filename)
            convert_msg_to_pdf(msg_path, pdf_path)

# Example usage

input_folder = r"C:\msg_to_pdf_converter\msg_files"
output_folder = r"C:\msg_to_pdf_converter\pdf_output"
batch_convert_msg_to_pdf(input_folder, output_folder)

# How to run
# Navigate to the folder where the script and output files are saved and do cd C:\msg_to_pdf_converter or your set file path

# Run the script using python convert_msg_to_pdf.py