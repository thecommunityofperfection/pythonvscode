import streamlit as st
import pandas as pd
import webbrowser
st.set_page_config(page_title = "Video Hub", page_icon = "▶️")
menu = st.sidebar.selectbox("Menu", ["Video Categories", "Video Ratings"])
videoviews = pd.read_csv("videoviews.csv")




if menu == "Video Categories":
    categories = st.sidebar.pills("Choose Videos", ["All", "Education", "Animals", "Sports", "Space", "Religion"], default = "All")
    st.sidebar.write("**:red[Made by Sam]**")




    if categories == "All" or categories == "Education":
        st.subheader("Education Category")




        e1, e2, e3, e4 = st.columns(4)




        with e1:
            vid1 = 0
            st.image("https://th.bing.com/th/id/R.79d5abac40a65c765a9cf7d91df243d7?rik=u5rHeN6Q2X0yHQ&pid=ImgRaw&r=0")
            st.write("How to classify circles")
            if st.button(label = "Play Video", key = "1"):
                webbrowser.open("https://www.youtube.com/watch?v=-QHff5pRdM8")
                videoviews["H"] = 0
                videoviews.loc["H"] += 1
                


        with e2:
            st.image("https://th.bing.com/th/id/OIP.8OgL4oacIGO0F8TZse6btwHaEK?rs=1&pid=ImgDetMain")
            st.write("Learn about shapes")
            if st.button(label = "Play Video", key = "2"):
                webbrowser.open("https://www.youtube.com/watch?v=g1Od5idlo_k")
        with e3:
            st.image("https://th.bing.com/th/id/OIP.bkfc7qadbmlsSdax6fIwJAAAAA?rs=1&pid=ImgDetMain")
            st.write("How to measure a circle")
            if st.button(label = "Play Video", key = "3"):
                webbrowser.open("https://youtu.be/D4nGkWOPb6M")
        with e4:
            st.image("https://i.ytimg.com/vi/e2JMt_YJveM/maxresdefault.jpg")
            st.write("What are clouds?")
            if st.button(label = "Play Video", key = "4"):
                webbrowser.open("https://youtu.be/e2JMt_YJveM")

    if categories == "All" or categories == "Animals":
        st.subheader("Animals Category")




        a1, a2, a3, a4 = st.columns(4)




        with a1:
            st.image("https://i.ytimg.com/vi/r1hpXoACWiI/maxresdefault.jpg")
            st.write("Wild Africa")
            if st.button(label = "Play Video", key = "5"):
                webbrowser.open("https://www.youtube.com/watch?v=r1hpXoACWiI")
        with a2:
            st.image("https://i.ytimg.com/vi/s3Kzt5_Jixg/maxresdefault.jpg")
            st.write("Polar")
            if st.button(label = "Play Video", key = "6"):
                webbrowser.open("https://www.youtube.com/watch?v=s3Kzt5_Jixg")
        with a3:
            st.image("https://i.ytimg.com/vi/nywsA8wCCfY/maxresdefault.jpg")
            st.write("360° Antarctica")
            if st.button(label = "Play Video", key = "7"):
                webbrowser.open("https://www.youtube.com/watch?v=nywsA8wCCfY")
        with a4:
            st.image("https://i.ytimg.com/vi/8gh996lWwfU/maxresdefault.jpg")
            st.write("Mountain Wildlife")
            if st.button(label = "Play Video", key = "8"):
                webbrowser.open("https://www.youtube.com/watch?v=8gh996lWwfU")

    if categories == "All" or categories == "Sports":
        st.subheader("Sports Category")




        s1, s2, s3, s4 = st.columns(4)




        with s1:
            st.image("https://i.ytimg.com/vi/1z2gp8lePbI/maxresdefault.jpg")
            st.write("Best dunks of all time")
            if st.button(label = "Play Video", key = "9"):
                webbrowser.open("https://www.youtube.com/watch?v=1z2gp8lePbI")
        with s2:
            st.image("https://i.ytimg.com/vi/lrA_9Lx-0nU/maxresdefault.jpg")
            st.write("Liverpool Vs. Chelsea")
            if st.button(label = "Play Video", key = "10"):
                webbrowser.open("https://www.youtube.com/watch?v=lrA_9Lx-0nU")
        with s3:
            st.image("https://i.ytimg.com/vi/qr7a1flcf8E/maxresdefault.jpg")
            st.write("Red sox Vs. Orioles")
            if st.button(label = "Play Video", key = "11"):
                webbrowser.open("https://www.youtube.com/watch?v=qr7a1flcf8E")
        with s4:
            st.image("https://vcptennis.com/wp-content/uploads/2023/11/EPIC-Novak-Djokovic-vs-Jannik-Sinner-Match-Highlights-Nitto-1140x694.jpg")
            st.write("Novak Djokovic Vs. Jannik Sinner")
            if st.button(label = "Play Video", key = "12"):
                webbrowser.open("https://vcptennis.com/epic-novak-djokovic-vs-jannik-sinner-match-highlights-nitto-atp-finals-2023/")

    if categories == "All" or categories == "Space":
        st.subheader("Space Category")




        p1, p2, p3, p4 = st.columns(4)




        with p1:
            st.image("https://i.ytimg.com/vi/s7Oq8_9QlHQ/maxresdefault.jpg")
            st.write("Black holes")
            if st.button(label = "Play Video", key = "13"):
                webbrowser.open("https://www.youtube.com/watch?v=s7Oq8_9QlHQ")
        with p2:
            st.image("https://th.bing.com/th/id/OIP.nCq07TL3xc5X8orOsrtvsgHaEK?rs=1&pid=ImgDetMain")
            st.write("All about the sun")
            if st.button(label = "Play Video", key = "14"):
                webbrowser.open("https://www.youtube.com/watch?v=VkW54j82e9U")
        with p3:
            st.image("https://th.bing.com/th/id/R.e7c496a735e0cae05196b0459b6b35eb?rik=cqMFYxp1cUbKcw&riu=http%3a%2f%2fi.ytimg.com%2fvi%2fYa38Ie20XxA%2fmaxresdefault.jpg&ehk=fLZDDJI%2bXx2WEYv36IbjfgOmEfIglK0KwnKpQWTNkwk%3d&risl=&pid=ImgRaw&r=0")
            st.write("Images from space")
            if st.button(label = "Play Video", key = "15"):
                webbrowser.open("http://www.youtube.com/watch?v=Ya38Ie20XxA")
        with p4:
            st.image("https://i.ytimg.com/vi/adKrNga8-Qs/maxresdefault.jpg")
            st.write("All about constellations for kids")#16
            st.button(label = "Play Video", url = "https://www.youtube.com/watch?v=adKrNga8-Qs-")

    if categories == "All" or categories == "Religion":
        st.subheader("Religion Category")




        r1, r2, r3, r4 = st.columns(4)




        with r1:
            st.image("https://i.ytimg.com/vi/3TT-ScMkbRc/maxresdefault.jpg")
            st.write("Top 10 biggest religions")
            if st.button(label = "Play Video", key = "17"):
                webbrowser.open("https://www.youtube.com/watch?v=3TT-ScMkbRc")
        with r2:
            st.image("https://i.ytimg.com/vi/VtQ9x6rKvoY/maxresdefault.jpg")
            st.write("World religion day")
            if st.button(label = "Play Video", key = "18"):
                webbrowser.open("https://www.youtube.com/watch?v=VtQ9x6rKvoY")
        with r3:
            st.image("https://i.ytimg.com/vi/ge071m9bGeY/maxresdefault.jpg")
            st.write('Evolution of Religion')
            st.button(label = "Play Video", url = "https://www.youtube.com/watch?v=ge071m9bGeY")
        with r4:
            st.image("https://i.ytimg.com/vi/TA8pefvKJjA/maxresdefault.jpg")
            st.write("Learn about Religions")
            if st.button(label = "Play Video", key = "20"):
                webbrowser.open("https://www.youtube.com/watch?v=TA8pefvKJjA")