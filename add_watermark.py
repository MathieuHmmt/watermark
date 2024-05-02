#!/usr/bin/python3
from reportlab.pdfgen import canvas
from pypdf import PdfReader, PdfWriter
from os import scandir, path, mkdir
import argparse

def create_watermark(content, output_path, angle, opacity):
	# Create a PDF with ReportLab
	c = canvas.Canvas(output_path, pagesize=(4000, 4000))
	width, height = (4000, 4000)
	c.setFont("Helvetica", 20)
	c.setFillAlpha(opacity)
	c.rotate(angle)

	x_interval = int((len(watermark_text) * 10))
	y_interval = 125
	for x in range(-int((len(watermark_text)) * 6), int(width) * 2, x_interval):
		for y in range(-300, int(height), y_interval):
			c.drawString(x, y, content)
	c.save()

def add_watermark_to_pdf(input_pdf, output_pdf, watermark_pdf):
	# Read the existing PDF
	original = PdfReader(input_pdf)
	watermark = PdfReader(watermark_pdf)
	watermark_page = watermark.pages[0]

	# Create a PdfWriter object for the output file
	writer = PdfWriter()

	# Apply the watermark to each page
	for page in original.pages:
		page.merge_page(watermark_page)
		writer.add_page(page)

    # Write the result to the output file
	with open(output_pdf, "wb") as output_file:
		writer.write(output_file)

# Get input args
parser = argparse.ArgumentParser()
parser.add_argument("watermark_text")
parser.add_argument("--opacity", help="Change watermark's text opacity (between 0.1 and 1)", type=float)
parser.add_argument("--angle", help="Change watermark text's display angle (in degrees)", type=int)
args = parser.parse_args()

# Add the watermark to every file in the docs directory
for file in scandir("./docs"):
	if file.is_file() and ".pdf" in file.path:

		input_pdf_path = file.path
		watermark_text = args.watermark_text
		opacity = args.opacity if args.opacity else 0.25
		angle = args.angle if args.angle else 45

		if not path.isdir("./watermarked"):
			mkdir("./watermarked")
			
		output_pdf_path = f'./watermarked/{file.name}_watermarked.pdf'

		create_watermark(watermark_text, output_pdf_path, angle, opacity)
		add_watermark_to_pdf(input_pdf_path, output_pdf_path, output_pdf_path)
