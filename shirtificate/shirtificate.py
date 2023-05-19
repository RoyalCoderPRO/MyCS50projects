from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("../docs/fpdf2-logo.png", 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "Title", border=1, align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

name = input("Name: ")
pdf = FPDF()
pdf= FPDF(orientation="P", unit="mm", format="A4")
pdf.set_font("helvetica", "B", 45)
pdf.add_page()
pdf.cell(0,60,"CS50 Shirtificate", align = "C")
pdf.image("shirtificate.png")
pdf.output("shirtificate.pdf")




#The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
#The shirt’s image should be centered horizontally.
#The user’s name should be on top of the shirt, in white text.