 
#  Pic to PDF converter
Convert files in .png and .jpg format to PDF with a simple python script

## Prerequisites
Prior running the script, the Pillow library must be installed. 

To install on Windows, run: pip install pillow

To install on Linux(Debian), run: sudo apt-get install python3-pil

##  Code analysis:
### Importing the necessary modules
Firstly we import the "image" module from PIL library (Python Imaging Library), which is intended for opening, manipulating, and saving different image file formats.

The module "pdfgen" is imported from "reportlab" library that allows us to generate PDF documents. also the "canvas" module was imported from "pdfgen", which facilitate us to create PDF pages and add content.

### Defining the Function###  
The two arguments: 'png_file' and 'pdf_file' in the 'png_to_pdf' function establish the path for both, the source and the output.

1.The function uses the **'image'** module to open the input PNG file.

2.Creates a PDF canvas object using the **'canvas'** module asociated with the output PDF file.

3.Retrieves the width and height of the input PNG image using the **'size'** attribute of the **'Image'** object.

4.Set the page size of the PDF canvas to match the dimensions of the input PNG image.

5.Draw the image on the PDF canvas at position (0,0) with the same width and heigth as the original image.

6.Save the PDF file through the **'c.save'** method

***


![reading...](https://media.giphy.com/media/Tf3mp01bfrrUc/giphy.gif?cid=ecf05e47wajghtrc5targr7mju7coe0avdyurnehrr1krgdt&ep=v1_gifs_search&rid=giphy.gif&ct=g  "...How could I ever do so unless someone guide me?")

***
