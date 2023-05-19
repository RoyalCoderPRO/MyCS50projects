from fpdf import FPDF

name = input("Name: ")
pdf = FPDF()
pdf= FPDF(orientation="P", unit="mm", format="A4")
pdf.set_font("helvetica", "B", 36)
pdf.add_page()
pdf.cell(txt="CS50 Shirtificate", align = 'C')
pdf.image("shirtificate.png")
pdf.output("shirtificate.pdf")




#The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
#The shirt’s image should be centered horizontally.
#The user’s name should be on top of the shirt, in white text.