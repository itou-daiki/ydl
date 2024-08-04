import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="easyYDL", layout="wide")

# App title and creator
st.title("easyYDL")
st.caption("Created by Dit-Lab.(Daiki Ito)")

# Introduction
st.markdown("""
## **概要**
このウェブアプリケーションでは、YouTube動画のDLを行うことができます（自己責任）。iPadなどのデバイスでも対応しています。""")

url = st.text_input("YouTubeのURLを入力してください")
format = st.radio("ダウンロード形式を選択してください", ('mp4', 'mp3'))

if st.button("ダウンロード"):
    if url:
        try:
            with st.spinner("ダウンロード中..."):
                output_path = "downloads"
                os.makedirs(output_path, exist_ok=True)
                
                ydl_opts = {
                    'format': 'bestaudio/best' if format == 'mp3' else 'bestvideo+bestaudio/best',
                    'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }] if format == 'mp3' else [],
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
            st.success(f"ダウンロードが完了しました！ {output_path} フォルダを確認してください。")
        except Exception as e:
            st.error(f"エラーが発生しました: {str(e)}")
    else:
        st.warning("URLを入力してください。")

# Copyright
st.subheader('© 2022-2024 Dit-Lab.(Daiki Ito). All Rights Reserved.')