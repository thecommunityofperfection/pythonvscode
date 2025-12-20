import streamlit as st
import time

if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
    st.rerun

if "score" not in st.session_state:
    st.session_state.score = 0

if "name" not in st.session_state:
    st.session_state.name = ""

def countdown():
    with st.spinner('Loading Next Page', show_time = True):
        time.sleep(3)

def home():
    st.title("Sam's Medical Awareness Quiz For Kids")
    st.write("")
    st.write("")
    st.session_state.name = st.text_input("What is your name?")
    st.write("")
    if st.button("Start Quiz"):
        st.write(f"Good luck on this quiz, {st.session_state.name}!")
        countdown()
        st.session_state.current_page = "q1"

def q1():
    st.info("Started Quiz!")
    st.subheader("Question 1")
    st.write("")
    q1 = st.radio("What is the main job of your heart?", ["Options:", "Digesting food", "Pumping blood", "Storing energy", "Breathing air"])
    if q1 != "Options:":
        if st.button("Next Question"):
            if q1 == "Pumping blood":
                st.success("Good job, you got it right!")
                st.session_state.score += 1
                countdown()
                st.session_state.current_page = "q2"
                st.rerun()
            else:
                st.error("Wrong answer.\n Better luck next time!")
                countdown()
                st.session_state.current_page = "q2"
                st.rerun()

def q2():
    
    st.subheader("Question 2")
    st.write("")
    q2 = st.radio("What do vaccines help protect you from?", ["Options:", "Diseases like measles or flu", "Cuts and bruises", "Common cold", "None of the above"])
    if q2 != "Options:":
        if st.button("Next Question"):
            if q2 == "Diseases like measles or flu":
                st.success("Good job, you got it right!")
                st.session_state.score += 1
                countdown()
                st.session_state.current_page = "q3"
                st.rerun()
            else:
                st.error("Wrong answer.\n Better luck next time!")
                countdown()
                st.session_state.current_page = "q3"
                st.rerun()

def q3():
    
    st.subheader("Question 3")
    st.write("")
    q3 = st.radio("Why is it important to wash your hands?", ["Options:", "To smell nice", "To look clean", "To prevent getting sick", "None of the above"])
    if q3 != "Options:":
        if st.button("Next Question"):
            if q3 == "To prevent getting sick":
                st.success("Good job, you got it right!")
                st.session_state.score += 1
                countdown()
                st.session_state.current_page = "q4"
                st.rerun()
            else:
                st.error("Wrong answer.\n Better luck next time!")
                countdown()
                st.session_state.current_page = "q4"
                st.rerun()

def q4():
    
    st.subheader("Question 4")
    st.write("")
    q4 = st.radio("What should you do if you have a fever?", ["Options:", "Stay up late", "Eat alot of candy", "Go play outside", "Tell an adult and rest"])
    if q4 != "Options:":
        if st.button("Next Question"):
            if q4 == "Tell an adult and rest":
                st.success("Good job, you got it right!")
                st.session_state.score += 1
                countdown()
                st.session_state.current_page = "q5"
                st.rerun()
            else:
                st.error("Wrong answer.\n Better luck next time!")
                countdown()
                st.session_state.current_page = "q5"
                st.rerun()

def q5():
    
    st.subheader("Question 5")
    st.write("")
    q5 = st.radio("What does a doctor do?", ["Options:", "Fix cars", "Help people stay healthy", "Teach math", "None of the above"])
    if q5 != "Options:":
        if st.button("Next Question"):
            if q5 == "Help people stay healthy":
                st.success("Correct answer!")
                st.session_state.score += 1
                countdown()
                st.session_state.current_page = "q6"
                st.rerun()
            else:
                st.error("Wrong answer.\n Better luck next time!")
                countdown()
                st.session_state.current_page = "q6"
                st.rerun()

def q6():
    
    st.subheader("Question 6")
    st.write("")
    q6 = st.radio("What is a healthy snack?", ["Options:", "Candy", "Chips", "Fruits and vegetables", "Soda"])
    if q6 != "Options:":
        if st.button("Next Question"):
            if q6 == "Fruits and vegetables":
                st.success("Correct answer!")
                st.session_state.score += 1
                countdown()
                st.session_state.current_page = "q7"
                st.rerun()
            else:
                st.error("Wrong answer.\n Better luck next time!")
                countdown()
                st.session_state.current_page = "q7"
                st.rerun()

def q7():
    
    st.subheader("Question 7")
    st.write("")
    q7 = st.radio("WHat does it mean to be allergic to something", ["Options:", "You like it alot", "You can't eat it", "Your body reacts badly to it", "None of the above"])
    if q7 != "Options:":
        if st.button("Next Question"):
            if q7 == "Your body reacts badly to it":
                st.success("Correct answer!")
                st.session_state.score += 1
                countdown()
                st.session_state.current_page = "q8"
                st.rerun()
            else:
                st.error("Wrong answer.\n Better luck next time!")
                countdown()
                st.session_state.current_page = "q8"
                st.rerun()

def q8():
    
    st.subheader("Question 8")
    st.write("")
    q8 = st.radio("What should you do if you get a cut?", ["Options:", "Show it to your friends", "Wash it and put a bandage on it", "Ignore it", "None of the above"])
    if q8 != "Options:":
        if st.button("Next Question"):
            if q8 == "Wash it and put a bandage on it":
                st.success("Correct answer!")
                st.session_state.score += 1
                countdown()
                st.session_state.current_page = "q9"
                st.rerun()
            else:
                st.error("Wrong answer.\n Better luck next time!")
                countdown()
                st.session_state.current_page = "q9"
                st.rerun()

def q9():
    
    st.subheader("Question 9")
    st.write("")
    q9= st.radio("WHy is it important to have breakfast?", ["Options:", "It gives you energy for school", "It's the best meal of the day", "You can skip it", "None of the above"])
    if q9!= "Options:":
        if st.button("Next Question"):
            if q9== "It gives you energy for school":
                st.success("Correct answer!")
                st.session_state.score += 1
                countdown()
                st.session_state.current_page = "q10"
                st.rerun()
            else:
                st.error("Wrong answer.\n Better luck next time!")
                countdown()
                st.session_state.current_page = "q10"
                st.rerun()

def q10():
    
    st.subheader("Question 10")
    st.write("")
    q10 = st.radio("What is one way to keep bones strong?", ["Options:", "", "", "", ""])
    if q10 != "Options:":
        if st.button("Next Question"):
            if q10 == "":
                st.success("Correct answer!")
                st.session_state.score += 1
                countdown()
                st.session_state.current_page = "q"
                st.rerun()
            else:
                st.error("Wrong answer.\n Better luck next time!")
                countdown()
                st.session_state.current_page = "q"
                st.rerun()

def q11():
    
    st.subheader("Question 11")
    st.write("")
    q11 = st.radio("What is the purpose of first aid?", ["Options:", "To help with homework?", "To give immediate care in emergencies", "To make food", "None of the above"])
    if q11 != "Options:":
        if st.button("Next Question"):
            if q11 == "To give immediate care in emergencies":
                st.success("Correct answer!")
                st.session_state.score += 1
                countdown()
                st.session_state.current_page = "q12"
                st.rerun()
            else:
                st.error("Wrong answer.\n Better luck next time!")
                countdown()
                st.session_state.current_page = "q12"
                st.rerun()

def q12():
    
    st.subheader("Question 12")
    st.write("")
    q12 = st.radio("What can help you breathe better whne you're sick?", ["Options:", "Eating ice cream", "Drinking warm fluids", "Running around", "None of the above"])
    if q12 != "Options:":
        if st.button("Next Question"):
            if q12 == "Drinking warm fluids":
                st.success("Correct answer!")
                st.session_state.score += 1
                countdown()
                st.session_state.current_page = "q13"
                st.rerun()
            else:
                st.error("Wrong answer.\n Better luck next time!")
                countdown()
                st.session_state.current_page = "q13"
                st.rerun()
def q13():
    
    st.subheader("Question 13")
    st.write("")
    q13 = st.radio("What is a common symptom of cold?", ["Options:", "Runny nose", "Happy thoughts", "Dancing", "None of the above"])
    if q13 != "Options:":
        if st.button("Next Question"):
            if q13 == "":
                st.success("Correct answer!")
                st.session_state.score += 1
                countdown()
                st.session_state.current_page = "q14"
                st.rerun()
            else:
                st.error("Wrong answer.\n Better luck next time!")
                countdown()
                st.session_state.current_page = "q14"
                st.rerun()
def q14():
    
    st.subheader("Question 14")
    st.write("")
    q14 = st.radio("Why should you cover your mouth when you cough?", ["Options:", "To look funny", "To prevent spreading germs", "To make a sound", "None of the above"])
    if q14 != "Options:":
        if st.button("Next Question"):
            if q14 == "To prevent spreading germs":
                st.success("Correct answer!")
                st.session_state.score += 1
                countdown()
                st.session_state.current_page = "q15"
                st.rerun()
            else:
                st.error("Wrong answer.\n Better luck next time!")
                countdown()
                st.session_state.current_page = "q15"
                st.rerun()
def q15():
    
    st.subheader("Question 15")
    st.write("")
    q15 = st.radio("What is a safe way to excercise?", ["Options:", "Jumping on the bed", "Playing sports or riding a bike", "Sitting all day", "None of the above"])
    if q15 != "Options:":
        if st.button("Next Question"):
            if q15 == "Playing sports or riding a bike":
                st.success("Correct answer!")
                st.session_state.score += 1
                countdown()
                st.session_state.current_page = "q16"
                st.rerun()
            else:
                st.error("Wrong answer.\n Better luck next time!")
                countdown()
                st.session_state.current_page = "q16"
                st.rerun()
def q16():
    st.info("Started Quiz!")
    st.subheader("Question 16")
    st.write("")
    q16 = st.radio("What does a dentist check", ["Options:", "Your eyes", "Your teeth", "Your hair", "None of the above"])
    if q16 != "Options:":
        if st.button("Next Question"):
            if q16 == "Your teeth":
                st.success("Correct answer!")
                st.session_state.score += 1
                countdown()
                st.session_state.current_page = "q17"
                st.rerun()
            else:
                st.error("Wrong answer.\n Better luck next time!")
                countdown()
                st.session_state.current_page = "q17"
                st.rerun()
def q17():
    st.info("Started Quiz!")
    st.subheader("Question 17")
    st.write("")
    q17 = st.radio("What should you do if you feel dizzy?", ["Options:", "Keep running", "Sit down and tell an adult", "Eat alot of candy", "None of the above"])
    if q17 != "Options:":
        if st.button("Next Question"):
            if q17 == "":
                st.success("Correct answer!")
                st.session_state.score += 1
                countdown()
                st.session_state.current_page = "q18"
                st.rerun()
            else:
                st.error("Wrong answer.\n Better luck next time!")
                countdown()
                st.session_state.current_page = "q18"
                st.rerun()
