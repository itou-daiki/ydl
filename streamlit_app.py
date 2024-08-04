import streamlit as st
from yt_dlp import YoutubeDL

st.set_page_config(page_title="easyYDL", layout="wide")

# App title and creator
st.title("easyYDL")
st.caption("Created by Dit-Lab.(Daiki Ito)")

# Introduction
st.markdown("""
## **概要**
このウェブアプリケーションでは、YouTube動画のDLを行うことができます（自己責任）。iPadなどのデバイスでも対応しています。""")

url = st.text_input("YouTubeのURLを入力してください")

if st.button("Download"):
    ydl_opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best",
        "outtmpl": "downloads/%(title)s.%(ext)s"
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

    st.success("ダウンロードが完了しました")

    if st.checkbox("Download as MP3"):
        ydl_opts = {
            "format": "bestaudio[ext=m4a]/best",
            "outtmpl": "downloads/%(title)s.%(ext)s",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192"
                }
            ]
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

        st.success("ダウンロードが完了しました")
# Copyright
st.subheader('© 2022-2024 Dit-Lab.(Daiki Ito). All Rights Reserved.')