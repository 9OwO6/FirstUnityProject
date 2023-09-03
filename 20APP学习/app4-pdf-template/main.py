from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False,margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times",style="B",size=16)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # draw lines
    countL = 0
    cy = 22
    while countL < 27:
        pdf.line(10, cy, 200, cy)
        cy = cy+10
        countL = countL+1

    # set footer
    pdf.ln(260)

    pdf.set_font(family="Times",style="I",size=8)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

    for i in range(row["Pages"]):
        pdf.add_page()

        # set footer
        pdf.ln(272)

        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

        # draw line
        countLS = 0
        cyS = 22
        while countLS < 27:
            pdf.line(10, cyS, 200, cyS)
            cyS = cyS + 10
            countLS = countLS + 1

# pdf.cell(w=0,h=12,txt="Hellow There!",align="L",ln=1,border=1)
pdf.output("output.pdf")




