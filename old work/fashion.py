import streamlit as st

st.title("Fashion App")
st.image("https://th.bing.com/th?id=OIP.DPrHsR2qvLz6Opxwz0G0iQHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2")

bill = 0
st.subheader("Men")

M1, M2, M3, M4 = st.columns(4)

with M1:
    st.image("https://m.media-amazon.com/images/I/61NxWlAdrpL._AC_UL480_FMwebp_QL65_.jpg")
    if st.checkbox("T-Shirts: $21"):
        st.success("Ok Done.")
        bill += 21

with M2:
    st.image("https://m.media-amazon.com/images/I/71xpzd0FFUL._AC_UL480_FMwebp_QL65_.jpg")
    if st.checkbox("Plaid shirt: $22"):
        st.success("Ok Done.")
        bill += 22

with M3:
    st.image("https://m.media-amazon.com/images/I/81eV4pJ5n4L._AC_UL480_FMwebp_QL65_.jpg")
    if st.checkbox("Ties: $23"):
        st.success("Ok Done.")
        bill += 23

with M4:
    st.image("https://m.media-amazon.com/images/I/91qYsOsY82L._AC_UL480_FMwebp_QL65_.jpg")
    if st.checkbox("Socks: $11"):
        st.success("Ok Done.")
        bill += 35

st.subheader("Women")

W1, W2, W3, W4 = st.columns(4)

with W1:
    st.image("https://m.media-amazon.com/images/I/61WizW55jxL._AC_UL480_FMwebp_QL65_.jpg")
    if st.checkbox("Dress: $7.50"):
        st.success("Ok Done.")
        bill += 7.50

with W2:
    st.image("https://m.media-amazon.com/images/I/71ZF-kpFhgL._AC_UL480_FMwebp_QL65_.jpg")
    if st.checkbox("Socks: $12"):
        st.success("Ok Done.")
        bill += 12

with W3:
    st.image("https://m.media-amazon.com/images/I/61WajSpamkL._AC_UL480_FMwebp_QL65_.jpg")
    if st.checkbox("Shorts: $11"):
        st.success("Ok Done.")
        bill += 11

with W4:
    st.image("https://m.media-amazon.com/images/I/91DdpLy1aBL._AC_UL480_FMwebp_QL65_.jpg")
    if st.checkbox("Jeans: $25"):
        st.success("Ok Done.")
        bill += 25
    
st.subheader("Children")

C1, C2, C3, C4 = st.columns(4)

with C1:
    st.image("https://m.media-amazon.com/images/I/91hjhrNowoL._AC_UL480_FMwebp_QL65_.jpg")
    if st.checkbox("Boys Polo Shirts: $26"):
        st.success("Ok Done.")
        bill += 26

with C2:
    st.image("https://m.media-amazon.com/images/I/61f2uQF9moL._AC_UL480_FMwebp_QL65_.jpg")
    if st.checkbox("Boys Joggers: $29"):
        st.success("Ok Done.")
        bill += 29

with C3:
    st.image("https://m.media-amazon.com/images/I/61c7gsJULkL._AC_UL480_FMwebp_QL65_.jpg")
    if st.checkbox("Girls Rain Pants: $39"):
        st.success("Ok Done.")
        bill += 39

with C4:
    st.image("https://m.media-amazon.com/images/I/61XduwUiCTL._AC_UL480_FMwebp_QL65_.jpg")
    if st.checkbox("Girls T-shirts: $20"):
        st.success("Ok Done.")
        bill += 20

if st.button("Check total bill"):
        st.write("Your total bill is",bill,"dollars")
