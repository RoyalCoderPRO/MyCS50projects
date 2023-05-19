from fpdf import FPDF

name = input("Name: ")
pdf = FPDF()
pdf(orientation="P", unit="mm", format="A4")
pdf.output("shirtificate.pdf")
pdf.add_page()
pdf.cell(txt="CS50 Shirtificate", align = 'C')




#The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
#The shirt’s image should be centered horizontally.
#The user’s name should be on top of the shirt, in white text.