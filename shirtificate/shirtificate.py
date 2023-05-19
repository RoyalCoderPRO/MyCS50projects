from fpdf import FPDF

name = input("Name: ")
pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=12)
pdf.cell(txt="CS50 Shirtificate")
pdf(orientation="P", unit="mm", format="A4")
pdf.output("shirtificate.pdf")


The orientation of the PDF should be Portrait.
The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
The shirt’s image should be centered horizontally.
The user’s name should be on top of the shirt, in white text.