import streamlit as st
import time

# create an app for your friends on how much they know you or know something or general quiz
# asks the user to enter his/her name on the questionnaire page
# the questionnaire page can be arranged in 3 or more columns (use your own ideas(-radio - selecbox))
# a button under after all to submit and this checks the right questions and add the scores and save the user score under the user name


if "current_page" not in st.session_state:
    st.session_state.current_page = "start"
    st.rerun()

def countdown():
    x = 0
    while x < 3:
        st.write(3-x)
        time.sleep(1)
        x += 1

def start():
    st.title("How much do you know about Python?")
    name = st.text_input("First, your name?")
    if name:
        button1, button2 = st.columns(2)
        with button1:
            if st.button("Start quiz 1"): 
                countdown()
                st.session_state.current_page = "q1"
                st.rerun()
        with button2:
            if st.button("Start quiz 2"): 
                countdown()
                st.session_state.current_page = "p1"
                st.rerun()
                
def q1():
    st.info("Started Quiz!")
    st.subheader("Question 1")
    st.divider()
    q1 = st.radio("What function outputs to the user's screen?", ["Options:", "output()", "write()", "print()", "text()"])
    if q1 != "Options:":
        if st.button("Next Question"):
            if q1 == "print()":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "q2"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "q2"
                st.rerun()

def q2():
    st.subheader("Question 2")
    st.divider()
    q2 = st.radio("How do you add a module to your code?", ["Options:", "module()", "package.add", "use()", "import"])
    if q2 != "Options:":
        if st.button("Next Question"):
            if q2 == "import":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "q3"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "q3"
                st.rerun()


def q3():
    global q3, score
    st.subheader("Question 3")
    st.divider()
    q3 = st.radio("What is used to add a block comment in python?", ["Options:", "<!-- -->", "//", "'''", "+++"])
    if q3 != "Options:":
        if st.button("Next Question"):
            if q3 == "'''":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "q4"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "q4"
                st.rerun()


def q4():
    global q4, score
    st.subheader("Question 4")
    st.divider()
    q4 = st.radio("What is the extension for a python file?", ["Options:", ".pth", ".py", ".pyt", ".python"])
    if q4 != "Options:":
        if st.button("Next Question"):
            if q4 == ".py":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "q5"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "q5"
                st.rerun()


def q5():
    global q5, score
    st.subheader("Question 5")
    st.divider()
    q5 = st.radio("How do you ask the user for a piece of information?", ["Options:", "input()", "ask()", "question()", "answer()"])
    if q5 != "Options:":
        if st.button("Next Question"):
            if q5 == "input()":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "q6"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "q6"
                st.rerun()


def q6():
    global q6, score
    st.subheader("Question 6")
    st.divider()
    q6 = st.radio("What stores information?", ["Options:", "box", "log", "store", "variable"])
    if q6 != "Options:":
        if st.button("Next Question"):
            if q6 == "variable":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "q7"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "q7"
                st.rerun()


def q7():
    global q7, score
    st.subheader("Question 7")
    st.divider()
    q7 = st.radio("Who created python?", ["Options:", "Isaac Watts", "David Bazsucki", "Guido van Rossum", "Mike Wazowski"])
    if q7 != "Options:":
        if st.button("Next Question"):
            if q7 == "Guido van Rossum":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "q8"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "q8"
                st.rerun()


def q8():
    global q8, score
    st.subheader("Question 8")
    st.divider()
    q8 = st.radio("What is '//' in python?", ["Options:", "Double Division", "Modulus", "Floor division", "Division"])
    if q8 != "Options:":
        if st.button("Next Question"):
            if q8 == "Floor division":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "q9"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "q9"
                st.rerun()


def q9():
    global q9, score
    st.subheader("Question 9")
    st.divider()
    q9 = st.radio("What is the '%' operator in python?", ["Options:", "Modulus", "Exponential", "Floor Division", "Percentage"])
    if q9 != "Options:":
        if st.button("Next Question"):
            if q9 == "Modulus":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "q10"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "q10"
                st.rerun()


def q10():
    global q10, score
    st.subheader("Question 10")
    st.divider()
    q10 = st.radio("All loops run forever", ["Options:", "True", "False"])
    if q10 != "Options:":
        if st.button("Next Question"):
            if q10 == "False":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "q11"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "q11"
                st.rerun()


def q11():
    global q11, score
    st.subheader("Question 11")
    st.divider()
    q11 = st.radio("How many 'z' does this code output? \n\nx = 0 \n\nwhile x <= 5:\n\n   x += 1\n\n   print('z')", ["Options:", "7", "4", "6", "5"])
    if q11 != "Options:":
        if st.button("Next Question"):
            if q11 == "6":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "q12"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "q12"
                st.rerun()


def q12():
    global q12, score
    st.subheader("Question 12")
    st.divider()
    q12 = st.radio("What type of programming language is python?", ["Options:", "Front end", "Back end", "Both", "Neither"])
    if q12 != "Options:":
        if st.button("Finish Quiz"):
            if q12 == "Back end":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "finish"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "finish"
                st.rerun()


def finish():
    st.info("Congrats! You have finished Sam's python quiz.\n\n Would you like to retake it?")
    if st.button("Retake Quiz"):
        st.session_state.current_page = "start"
        st.rerun()
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
def p1():
    st.info("Started Quiz!")
    st.subheader("Question 1")
    st.divider()
    q1 = st.radio("When was I born?", ["Options:", "June 16, 2010", "August 5, 2009", "January 19, 2010", "May 7, 2009"])
    if q1 != "Options:":
        if st.button("Next Question"):
            if q1 == "January 19, 2010":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "p2"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "p2"
                st.rerun()

def p2():
    st.subheader("Question 2")
    st.divider()
    q2 = st.radio("What is my favorite food?", ["Options:", "Pasta", "Fried Plantain", "Jollof Rice", "Beans"])
    if q2 != "Options:":
        if st.button("Next Question"):
            if q2 == "Pasta" or q2 == "Fried Plantain":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "p3"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "p3"
                st.rerun()


def p3():
    global q3, score
    st.subheader("Question 3")
    st.divider()
    q3 = st.radio("Where do I live?", ["Options:", "Canada", "United States", "England", "Nigeria"])
    if q3 != "Options:":
        if st.button("Next Question"):
            if q3 == "Canada":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "p4"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "p4"
                st.rerun()


def p4():
    global q4, score
    st.subheader("Question 4")
    st.divider()
    q4 = st.radio("Where was I born?", ["Options:", "Australia", "Canada", "Nigeria", "England"])
    if q4 != "Options:":
        if st.button("Next Question"):
            if q4 == "England":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "p5"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "p5"
                st.rerun()


def p5():
    global q5, score
    st.subheader("Question 5")
    st.divider()
    q5 = st.radio("How old am I?", ["Options:", "16", "14", "15", "17"])
    if q5 != "Options:":
        if st.button("Next Question"):
            if q5 == "15":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "p6"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "p6"
                st.rerun()


def p6():
    global q6, score
    st.subheader("Question 6")
    st.divider()
    q6 = st.radio("How many siblings do I have?", ["Options:", "3", "1", "0", "2"])
    if q6 != "Options:":
        if st.button("Next Question"):
            if q6 == "1":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "p7"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "p7"
                st.rerun()


def p7():
    global q7, score
    st.subheader("Question 7")
    st.divider()
    q7 = st.radio("What was my first job?", ["Options:", "Newspaper Handout", "Small Restaurant", "Movie Survey", "Garbage Collector"])
    if q7 != "Options:":
        if st.button("Next Question"):
            if q7 == "Newspaper Handout":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "p8"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "p8"
                st.rerun()


def p8():
    global q8, score
    st.subheader("Question 8")
    st.divider()
    q8 = st.radio("What is my favorite novel??", ["Options:", "The Hunger Games", "Powerless", "The Ballad of Songbirds and Snakes", "Winnie the Pooh"])
    if q8 != "Options:":
        if st.button("Next Question"):
            if q8 == "Powerless":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "p9"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "p9"
                st.rerun()


def p9():
    st.subheader("Question 9")
    st.divider()
    q9 = st.radio("What is my favorite game?", ["Options:", "Blox Fruits", "Fortnite", "Valorant", "Rocket League"])
    if q9 != "Options:":
        if st.button("Next Question"):
            if q9 == "Blox Fruits":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "p10"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "p10"
                st.rerun()


def p10():
    st.subheader("Question 10")
    st.divider()
    q10 = st.radio("Sam is my first name", ["Options:", "True", "False"])
    if q10 != "Options:":
        if st.button("Next Question"):
            if q10 == "False":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "p11"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "p11"
                st.rerun()


def p11():
    st.subheader("Question 11")
    st.divider()
    q11 = st.radio("What do I want to be when I grow up?", ["Options:", "Artist", "Programmer", "Engineer", "Architect"])
    if q11 != "Options:":
        if st.button("Next Question"):
            if q11 == "Programmer":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "p12"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "p12"
                st.rerun()


def p12():
    st.subheader("Question 12")
    st.divider()
    q12 = st.radio("What am I allergic to?", ["Options:", "Peanuts", "Dogs", "Cats", "Grass"])
    if q12 != "Options:":
        if st.button("Finish Quiz"):
            if q12 == "Peanuts":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "p13"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "p13"
                st.rerun()

def p13():
    st.subheader("Question 13")
    st.divider()
    q13 = st.radio("What is my favorite fruit?", ["Options:", "Banana", "Pineapple", "Dragonfruit", "Blackberry"])
    if q13 != "Options:":
        if st.button("Finish Quiz"):
            if q13 == "Blackberry":
                st.success("Correct answer!")
                countdown()
                st.session_state.current_page = "finish"
                st.rerun()
            else:
                st.error("Wrong answer!")
                countdown()
                st.session_state.current_page = "finish"
                st.rerun()


def pfinish():
    st.info("Congrats! You have finished Sam's python quiz.\n\n Would you like to retake it?")
    if st.button("Retake Quiz"):
        st.session_state.current_page = "start"
        st.rerun()

if st.session_state.current_page == "start":
    start()
elif st.session_state.current_page == "p1":
    p1()
elif st.session_state.current_page == "p2":
    p2()
elif st.session_state.current_page == "p3":
    p3()
elif st.session_state.current_page == "p4":
    p4()
elif st.session_state.current_page == "p5":
    p5()
elif st.session_state.current_page == "p6":
    p6()
elif st.session_state.current_page == "p7":
    p7()
elif st.session_state.current_page == "p8":
    p8()
elif st.session_state.current_page == "p9":
    p9()
elif st.session_state.current_page == "p10":
    p10()
elif st.session_state.current_page == "p11":
    p11()
elif st.session_state.current_page == "p12":
    p12()
elif st.session_state.current_page == "p13":
    p13()
elif st.session_state.current_page == "pfinish":
    pfinish()
# if st.session_state.current_page == "start":
#     start()
elif st.session_state.current_page == "q1":
    q1()
elif st.session_state.current_page == "q2":
    q2()
elif st.session_state.current_page == "q3":
    q3()
elif st.session_state.current_page == "q4":
    q4()
elif st.session_state.current_page == "q5":
    q5()
elif st.session_state.current_page == "q6":
    q6()
elif st.session_state.current_page == "q7":
    q7()
elif st.session_state.current_page == "q8":
    q8()
elif st.session_state.current_page == "q9":
    q9()
elif st.session_state.current_page == "q10":
    q10()
elif st.session_state.current_page == "q11":
    q11()
elif st.session_state.current_page == "q12":
    q12()
elif st.session_state.current_page == "finish":
    finish()
