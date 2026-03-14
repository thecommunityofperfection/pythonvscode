import streamlit as st

c1Votes = 0
c2Votes = 0
c3Votes = 0
c1, c2 = st.columns(2)

with c1:
    age = st.number_input("How old are you?", 0)
    if age >= 18:
        st.success("You are elegible to vote!")
        if st.button("Vote for candidate one"):
            c1Votes += 1
            st.success("Voted for candidate 1!")
        elif st.button("Vote for candidate 2"):
            c2Votes += 1
            st.success("Voted for candidate 2!")
        elif st.button("Vote for candidate 3"):
            c3Votes += 1
            st.success("Voted for candidate 3!")
    else:
        st.error("Voters below 18 are not allowed")
with c2:
    st.title("**Voting in Progress**")