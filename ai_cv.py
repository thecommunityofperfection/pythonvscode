import streamlit as st
import requests
from fpdf import FPDF
import base64

st.set_page_config(layout = "wide", page_title = "Student's AI CV generator", page_icon = "")
if "current_page" not in st.session_state:
    st.session_state.current_page = "start"
    st.rerun()
# pdf.ln(3)
#---------------------CONFIG-------------------------
api_key = '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'#API PROGRAM INTERFACE

api_link = "https://openrouter.ai/api/v1/chat/completions"
headers = {"Authorization": f"Bearer {api_key}", "Content-Type":"application/json"}
#----------------------------------------------------

#FUNCTION TO SEND DATA TO OPENROUTER
def ask_ai(content):
    """Send prompt to AI and return only the text content."""
    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": content}],
        "max_tokens": 250,
        "temperature": 0.7
    }
    response = requests.post(api_link, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code}"

def generate_pdf():
    pdf = FPDF()

    pdf.add_page()

    colx = 10
    coly = 10
    colw = 50
    colh = 10

    #name
    pdf.set_font("Arial", size = 25, style = "B")
    pdf.set_xy(75, 10)
    pdf.cell(colw, colh, txt = name, ln = True, align = "C")
    
    if pfp == "Yes":
        pdf.image(st.session_state.pic, x = 12.5, y = 12.5, w = 20)
    #email
    try:
        pdf.set_font("Arial", size = 10)
        pdf.set_xy(80, 22.5)
        pdf.cell(colw, colh, txt = "Email: " + email, ln = True, align = "C")
    except:
        pdf.set_font("Arial", size = 10)
        pdf.set_xy(80, 22.5)
        pdf.cell(colw, colh, txt = "", ln = True, align = "C")

    #phone
    try:
        pdf.set_font("Arial", size = 10)
        pdf.set_xy(80, 27.5)
        pdf.cell(colw, colh, txt = "Phone: " + phone, ln = True, align = "C")
    except:
        pdf.set_font("Arial", size = 10)
        pdf.set_xy(80, 22.5)
        pdf.cell(colw, colh, txt = "", ln = True, align = "C")

    #address
    pdf.set_font("Arial", size = 10)
    pdf.set_xy(80, 18)
    pdf.cell(colw, colh, txt = "Address: " + address, ln = True, align = "C")

    #summary
    pdf.set_font("Arial", size = 10, style = "B")
    pdf.set_xy(10, 40)
    pdf.cell(10, colh, txt = "Summary: ", ln = True, align = "L")

    pdf.set_font("Arial", size = 10)
    pdf.ln(0.8)
    pdf.multi_cell(0, 4.5, txt = st.session_state.pro_response, align = "L")

    #skills
    pdf.ln(3)
    pdf.set_font("Arial", size = 10, style = "B")
    pdf.cell(10, colh, txt = "Skills: ", ln = True, align = "L")

    pdf.set_font("Arial", size = 10)
    pdf.ln(0.8)
    pdf.multi_cell(0, 4.5, txt = st.session_state.skills_response, align = "L")

    #work
    pdf.ln(3)
    pdf.set_font("Arial", size = 10, style = "B")
    pdf.cell(10, colh, txt = "Work: ", ln = True, align = "L")

    pdf.set_font("Arial", size = 10)
    pdf.ln(0.8)
    pdf.multi_cell(0, 4.5, txt = st.session_state.work_response, align = "L")

    #education
    pdf.ln(3)
    pdf.set_font("Arial", size = 10, style = "B")
    pdf.cell(10, colh, txt = "Education: ", ln = True, align = "L")

    pdf.set_font("Arial", size = 10)
    pdf.ln(0.8)
    pdf.multi_cell(0, 4.5, txt = st.session_state.education_response, align = "L")

    #references
    pdf.ln(3)
    pdf.set_font("Arial", size = 10, style = "B")
    pdf.cell(10, colh, txt = "References: ", ln = True, align = "L")

    pdf.set_font("Arial", size = 10)
    pdf.ln(0.8)
    pdf.multi_cell(0, 4.5, txt = st.session_state.reference_response, align = "L")

    

    pdf_file = "invoice_sam.pdf"
    pdf.output(pdf_file)
    return pdf_file

with st.sidebar:
    global pro_response, skills_response, work_response, education_response, reference_response, pic
    st.title("AI CV Generator")
    st.write(":grey[Please fill this form to generate a free CV today!]")
    name = st.text_input("Input name", placeholder = "Full name", label_visibility = "collapsed")
    address = st.text_input("Input address", placeholder = "Address", label_visibility = "collapsed")
    contact = st.radio("Add contact info", ["Email", "Phone", "Both"])
    if contact == "Email" or contact == "Both":
        email = st.text_input("Input Email", placeholder = "Email", label_visibility = "collapsed")
    if contact == "Phone" or contact == "Both":
        phone = st.text_input("Input Phone number", placeholder = "Phone", label_visibility = "collapsed")
    #st.toggle("yes or no")
    gender = st.radio("Select Gender", ["Male", "Female"], horizontal = True)
    pfp = st.pills("Add Profile picture", ["Yes", "No"])
    if pfp == "Yes":
        uploadPicture = st.file_uploader("Choose profile picture: ", type = ["jpg", "png", "jpeg"])
        if st.button("Save Picture"):
            with open(name + ".png", "wb") as writepic:
                writepic.write(uploadPicture.getbuffer())
                st.session_state.pic = name + ".png"
                st.success("Saved Picture!")
    elif pfp == "No":
        st.info("You have opted out of adding a profile picture")
    education = st.text_area("Add level of education", placeholder = "Ex.\n Harvard school of medicine, class of 1993\n Masters degree")
    experience = st.text_area("Describe work experience, One per line", placeholder = "Ex. Worked at XX co. for XX years doing XX and gaining XX skills")
    skills = st.text_area("Describe key skills, One per line", placeholder = "Learned how to do XX at XX and have done it for XX years. Extensive knowledge in XX, which applies to XX and inclues XX skills.")
    references = st.text_area("Add references, one per line", placeholder = "John Doe: xxx-xxx-xxxx - Boss\nJane Doe: xxx-xxx-xxxx - Previous Employer\nLorem Ipsum: xxx-xxx-xxxx - Colleague")
    #work experience, education,,,, examples


    #---------------------Variables to store ai response------------------------------------
    summary = f"""Design a professional summary for my CV. Make it 3-5 lines, Using the information given below
    My key skills:{skills}
    My work experience: {experience}
    My education: {education}
    """
    skills_summary = f"""Create a bulleted list with just 1 line for each skill provided below
    My key skills:{skills}
    """
    work_summary = f"""Create a professional description of my work experience below using this format:
    Employer/Organization
    Start-End Date
    Job Title
    Responsibilities/Achievements (bullet points)
    My work experience:{experience}
    """
    education_summary = f"""Create an education outline in this format of each section:
    Course Title
    Start year - End year
    School or course provider
    with information provided below, no prompt text.
    My education:{education}
    """
    reference_summary = f"""Create a reference outline using the information provided below in this format:
    Name - Phone number/Email/Other Contact - relationship
    one line per reference
    My references:{references}
    """

    #---------------------------------------------------------
    generate =  st.button("Generate AI CV")


    



if generate:
    with st.spinner("Creating your CV"):
        if name and address and skills and education and experience:
            st.session_state.pro_response = ask_ai(summary)
            st.text_area(value = st.session_state.pro_response, height = 150, label = "Professional Summary   :blue[Click to edit]")
            st.session_state.skills_response = ask_ai(skills_summary)
            st.text_area(value = st.session_state.skills_response, height = 150, label = "Skills response   :blue[Click to edit]")
            st.session_state.work_response = ask_ai(work_summary)
            st.text_area(value = st.session_state.work_response, height = 150, label = "Work response   :blue[Click to edit]")
            st.session_state.education_response = ask_ai(education_summary)
            st.text_area(value = st.session_state.education_response, height = 150, label = "Education response   :blue[Click to edit]")
            st.session_state.reference_response = ask_ai(reference_summary)
            st.text_area(value = st.session_state.reference_response, height = 150, label = "Reference response   :blue[Click to edit]")
            if st.button('Show pdf'):
                pdf_func = generate_pdf()
                with open(pdf_func, "rb") as readtext:
                    pdf_data = readtext.read()
                pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')
                pdf_embed = f'<embed src= "data:application/pdf;base64, {pdf_base64}" type= "application/pdf" width="100%" height="600px" />'
                st.markdown(pdf_embed,unsafe_allow_html=True)
                st.download_button(label = "Download PDF", data = pdf_data, file_name = name + "_cv.pdf", mime = "application/pdf")

            
        else:
            st.error("Please fill out all the required info")