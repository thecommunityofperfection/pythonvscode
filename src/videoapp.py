import streamlit as st
import pandas as pd
import webbrowser
import os
from pandas import DataFrame
from typing import Dict, List, Tuple

st.set_page_config(page_title="Video Hub", page_icon="▶️")

# Helper to ensure file and views DataFrame are valid
csv_path: str = "csv/videoviews.csv"
os.makedirs("csv", exist_ok=True)

try:
    videoviews: DataFrame = pd.read_csv(csv_path)
except FileNotFoundError:
    videoviews = pd.DataFrame([{}])
    videoviews.to_csv(csv_path, index=False)

def increment_view_count(title: str) -> None:
    if title not in videoviews.columns:
        videoviews[title] = 0
    videoviews.at[0, title] += 1
    videoviews.to_csv(csv_path, index=False)

def render_video(col: st.delta_generator.DeltaGenerator, title: str, image_url: str, video_url: str, key: str) -> None:
    with col:
        st.image(image_url)
        st.write(title)
        if st.button("Play Video", key=key):
            webbrowser.open(video_url)
            increment_view_count(title)

# Sidebar menu
menu: str = st.sidebar.selectbox("Menu", ["Video Categories", "Video Ratings"])

if menu == "Video Categories":
    categories: str = st.sidebar.radio("Choose Videos", ["All", "Education", "Animals", "Sports", "Space", "Religion"], index=0)
    st.sidebar.write("**:red[Made by Sam]**")

    category_videos: Dict[str, List[Tuple[str, str, str]]] = {
        "Education": [
            ("How to classify circles", "https://th.bing.com/th/id/R.79d5abac40a65c765a9cf7d91df243d7?rik=u5rHeN6Q2X0yHQ&pid=ImgRaw&r=0", "https://www.youtube.com/watch?v=-QHff5pRdM8"),
            ("Learn about shapes", "https://th.bing.com/th/id/OIP.8OgL4oacIGO0F8TZse6btwHaEK?rs=1&pid=ImgDetMain", "https://www.youtube.com/watch?v=g1Od5idlo_k"),
            ("How to measure a circle", "https://th.bing.com/th/id/OIP.bkfc7qadbmlsSdax6fIwJAAAAA?rs=1&pid=ImgDetMain", "https://youtu.be/D4nGkWOPb6M"),
            ("What are clouds?", "https://i.ytimg.com/vi/e2JMt_YJveM/maxresdefault.jpg", "https://youtu.be/e2JMt_YJveM"),
        ],
        "Animals": [
            ("Wild Africa", "https://i.ytimg.com/vi/r1hpXoACWiI/maxresdefault.jpg", "https://www.youtube.com/watch?v=r1hpXoACWiI"),
            ("Polar", "https://i.ytimg.com/vi/s3Kzt5_Jixg/maxresdefault.jpg", "https://www.youtube.com/watch?v=s3Kzt5_Jixg"),
            ("360° Antarctica", "https://i.ytimg.com/vi/nywsA8wCCfY/maxresdefault.jpg", "https://www.youtube.com/watch?v=nywsA8wCCfY"),
            ("Mountain Wildlife", "https://i.ytimg.com/vi/8gh996lWwfU/maxresdefault.jpg", "https://www.youtube.com/watch?v=8gh996lWwfU"),
        ],
        "Sports": [
            ("Best dunks of all time", "https://i.ytimg.com/vi/1z2gp8lePbI/maxresdefault.jpg", "https://www.youtube.com/watch?v=1z2gp8lePbI"),
            ("Liverpool Vs. Chelsea", "https://i.ytimg.com/vi/lrA_9Lx-0nU/maxresdefault.jpg", "https://www.youtube.com/watch?v=lrA_9Lx-0nU"),
            ("Red Sox Vs. Orioles", "https://i.ytimg.com/vi/qr7a1flcf8E/maxresdefault.jpg", "https://www.youtube.com/watch?v=qr7a1flcf8E"),
            ("Novak Djokovic Vs. Jannik Sinner", "https://vcptennis.com/wp-content/uploads/2023/11/EPIC-Novak-Djokovic-vs-Jannik-Sinner-Match-Highlights-Nitto-1140x694.jpg", "https://vcptennis.com/epic-novak-djokovic-vs-jannik-sinner-match-highlights-nitto-atp-finals-2023/"),
        ],
        "Space": [
            ("Black holes", "https://i.ytimg.com/vi/s7Oq8_9QlHQ/maxresdefault.jpg", "https://www.youtube.com/watch?v=s7Oq8_9QlHQ"),
            ("All about the sun", "https://th.bing.com/th/id/OIP.nCq07TL3xc5X8orOsrtvsgHaEK?rs=1&pid=ImgDetMain", "https://www.youtube.com/watch?v=VkW54j82e9U"),
            ("Images from space", "https://i.ytimg.com/vi/Ya38Ie20XxA/maxresdefault.jpg", "http://www.youtube.com/watch?v=Ya38Ie20XxA"),
            ("All about constellations for kids", "https://i.ytimg.com/vi/adKrNga8-Qs/maxresdefault.jpg", "https://www.youtube.com/watch?v=adKrNga8-Qs"),
        ],
        "Religion": [
            ("Top 10 biggest religions", "https://i.ytimg.com/vi/3TT-ScMkbRc/maxresdefault.jpg", "https://www.youtube.com/watch?v=3TT-ScMkbRc"),
            ("History of Hinduism", "https://i.ytimg.com/vi/x3pgmlU9UfI/maxresdefault.jpg", "https://www.youtube.com/watch?v=x3pgmlU9UfI"),
            ("Christianity Explained", "https://i.ytimg.com/vi/wDBBHyQYpb8/maxresdefault.jpg", "https://www.youtube.com/watch?v=wDBBHyQYpb8"),
            ("Islam in 5 Minutes", "https://i.ytimg.com/vi/6eZLijW8K64/maxresdefault.jpg", "https://www.youtube.com/watch?v=6eZLijW8K64"),
        ],
    }

    for category, videos in category_videos.items():
        if categories == "All" or categories == category:
            st.subheader(f"{category} Category")
            cols = st.columns(4)
            for i, (title, img, url) in enumerate(videos):
                render_video(cols[i % 4], title, img, url, key=f"{category}_{i}")

elif menu == "Video Ratings":
    st.title("📊 Video View Count Stats")
    if videoviews.empty or videoviews.columns.empty:
        st.warning("No video views tracked yet.")
    else:
        st.bar_chart(videoviews.T.rename(columns={0: "Views"}))
