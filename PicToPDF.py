from PIL import Image # Pillow package must be installed
from reportlab.pdfgen import canvas

def png_to_pdf(png_file, pdf_file):
	# Open the PNG file
	image = Image.open(png_file)

	# Create a PDF canvas
	c = canvas.Canvas(pdf_file)

	# Get image dimensions
	width, height = image.size

	# Set the page size to match the image size
	c.setPageSize(width, height)

	# Draw the image on the PDF canvas
	c.drawImage(png_file, 0, 0, width, height)

	# save the PDF file
	c.save()

# output
png_to_pdf("X:\source_path\file_name.png", "X:\output_path\file_name.pdf")