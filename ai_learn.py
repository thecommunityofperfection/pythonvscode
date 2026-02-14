import streamlit as st
import requests


if "generate" not in st.session_state:
    st.session_state.generate = 0
    st.session_state.gen = 0
    st.rerun()
st.set_page_config(layout = "wide", page_title = "Sam's AI CV generator", page_icon = "")

#---------------------CONFIG-------------------------
api_key = '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'#API PROGRAM INTERFACE

api_link = "https://openrouter.ai/api/v1/chat/completions"
headers = {"Authorization": f"Bearer {api_key}", "Content-Type":"application/json"}
#----------------------------------------------------

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
    
with st.sidebar:
    st.title("AI learning aid")
    grade = st.text_input("What school level(or grade) are you in?")
    subject = st.selectbox("Choose a subject", ["Choose a subject","Math", "English", "Geography", "History", "Science"])
    if subject != "Choose a subject":
        topic1 = f"""Generate a topic for {subject}
        at the {grade} level (canadian).
        1-4 words
        """
        topic2 = f"""Generate a topic for {subject}
        at the {grade} level (canadian).
        1-4 words
        not including {topic1}
        """
        topic3 = f"""Generate a topic for {subject}
        at the {grade} level (canadian).
        1-4 words
        not including {topic1, topic2}
        """
        if st.session_state.gen != 1:
            st.session_state.topic1AI = ask_ai(topic1)
            st.session_state.topic2AI = ask_ai(topic2)
            st.session_state.topic3AI = ask_ai(topic3)
            st.session_state.gen = 1
        else:
            if st.button("Regenerate topics"):
                st.session_state.topic1AI = ask_ai(topic1)
                st.session_state.topic2AI = ask_ai(topic2)
                st.session_state.topic3AI = ask_ai(topic3)
        topic = st.pills("What topics do you want to learn", ["Select","Choose your own", st.session_state.topic1AI, st.session_state.topic2AI, st.session_state.topic3AI])
        if topic == "Choose your own":
            topicChoice = st.text_input("Topic choice:")
            if topicChoice:
                topic = topicChoice
                done = True
        if topic != "Select":
            helpType = st.selectbox("What form of help do you want?", ["Select", "Short note", "Key points", "Questions to solve"])
            if helpType != "Select":
                if helpType == "Questions to solve":
                    qType = st.pills("Question type:", ["Problems with solutions included", "Problems without solutions included"])
                    helpAsk = f"""Generate 3-5 {helpType} for {subject} topic: {topic}.
                    {qType}
                    at the {grade} level.
                    no prompt text.
                    """
                elif helpType == "Short note":
                    helpAsk = f"""Generate {helpType} help for {subject} topic: {topic}.
                    at the {grade} level.
                    no prompt text.
                    """
                elif helpType == "Key points":
                    helpAsk = f"""Generate {helpType} for {subject} topic: {topic}.
                    at the {grade} level.
                    no prompt text.
                    """
                if st.button("Generate learning aid"):
                    response = ask_ai(helpAsk)
                    st.session_state.generate = 1
                    
if st.session_state.generate == 1:
    st.subheader(topic)
    st.divider()
    st.info(response)
    st.session_state.generate = 0
