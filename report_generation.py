#!pip install PyPDF2
#!pip install nltk
#!pip install transformers
#!pip install pdfkit
#!pip install fpdf
#!pip install punkt_tab
#!pip install reportlab

from transformers import pipeline
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize
from PyPDF2 import PdfReader, PdfWriter
import pdfkit
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def text_to_pdf(text,filename):
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.drawString(100, 750, text)  # Write the text
    can.save()
    packet.seek(0)
    new_pdf = PdfReader(packet)
    output = PdfWriter()

    output.add_page(new_pdf.pages[0])
    with open(filename, 'wb') as f:
        pdf = PdfWriter()

def summarize_pdf(input_pdf_path, output_pdf_path, num_sentences=3):
    try:
        reader = PdfReader(input_pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        sentences = sent_tokenize(text)
        print(sentences)
        summarizer = pipeline("summarization")
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)

        summary_text = summary[0]["summary_text"]
        text_to_pdf(summary_text,output_pdf)
        print("PDF created successfully as output.pdf")
    except FileNotFoundError:
        print("Error: Input PDF file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_pdf  = '/content/sample_data/input_pdf.pdf'
output_pdf = '/content/sample_data/output_pdf.pdf'
summarize_pdf(input_pdf, output_pdf)




