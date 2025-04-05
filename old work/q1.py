import streamlit as st

packing_list = []
bag = ""
while bag != "full":
    addItem = st.text_input("What item would you like to add to the bag?")
    if len(packing_list) > 15:
        st.error("You might be overpacking.")
        bag = "full"
    elif addItem in packing_list:
        st.error("You already have that item in your bag.")
    else:
        packing_list.append(addItem)
        st.write("You have added 1 item")
st.write("Your bag contains: ")
st.write(packing_list)