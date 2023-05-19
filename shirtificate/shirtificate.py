from fpdf import FPDF

name = input("Name: ")
pdf = FPDF()
pdf= FPDF(orientation="P", unit="mm", format="A4")
pdf.set_font("helvetica", "B", 45)
pdf.add_page()
pdf.cell(0,60,"CS50 Shirtificate", align = "C")
pdf.image("shirtificate.png", x=0, y =70)
pdf.set_font_size(30)
pdf.set_text_color(255, 255, 255)
pdf.text(x=45, y=150, txt=f"{name} took CS50")
pdf.output("shirtificate.pdf")
