import streamlit as st
from fpdf import FPDF #for the pdf
import base64#to write chars from python to pdf
name = "Mason"
grade = "Grade 12"
picture = "tree.png"
st.header(name)
st.write(grade)
st.image(picture)

def generate_pdf():
    pdf = FPDF()

    pdf.add_page()

    colx = 10
    coly = 10
    colw = 50
    colh = 10

    #name
    pdf.set_font("Arial", size = 25, style = "B")
    pdf.set_xy(colx, coly)
    pdf.cell(colw, colh, txt = name, ln = True, align = "L")
    
    #grade
    pdf.set_font("Arial", size = 12)
    pdf.set_xy(colx, coly + 10)
    pdf.cell(colw, colh, txt = grade, ln = True, align = "L")

    pdf.image(picture, x = colx + 50, y = coly, w = 20)

    pdf_file = "invoice_sam.pdf"
    pdf.output(pdf_file)
    return pdf_file

pdf_func = generate_pdf()
with open(pdf_func, "rb") as readtext:
    pdf_data = readtext.read()

if st.button('Show pdf'):
   pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')
   pdf_embed = f'<embed src= "data:application/pdf;base64, {pdf_base64}" type= "application/pdf" width="100%" height="600px" />'
   st.markdown(pdf_embed,unsafe_allow_html=True)

st.download_button(label = "Download PDF", data = pdf_data, file_name = "Sam_invoice.pdf", mime = "application/pdf")