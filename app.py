# import streamlit as st
# import yt_dlp
# import os

# AUDIO_QUALITIES = {
#     "48 kbps": "bestaudio[abr<=48]",
#     "128 kbps": "bestaudio[abr<=128]",
#     "320 kbps": "bestaudio[abr<=320]",
# }

# VIDEO_QUALITIES = {
#     "144p": 144,
#     "240p": 240,
#     "480p": 480,
#     "720p": 720,
#     "1080p": 1080,
# }

# def download_audio(url, format_selector):
#     ydl_opts = {
#         "format": format_selector,
#         "outtmpl": "%(title)s.%(ext)s",
#         "writethumbnail": True,
#         "postprocessors": [
#             {"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "320"},
#             {"key": "EmbedThumbnail"},
#             {"key": "FFmpegMetadata"}
#         ],
#         "prefer_ffmpeg": True,
#         "converttothumbnail": "jpg",
#         "postprocessor_args": ["-id3v2_version", "3"],
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(url, download=True)
#         filename = ydl.prepare_filename(info).rsplit(".", 1)[0] + ".mp3"
#         return filename, info.get("title", "audio")

# def download_video(url, height):
#     # Force H.264 + AAC for maximum compatibility
#     ydl_opts = {
#         "format": f"bestvideo[height<={height}][ext=mp4]+bestaudio[ext=m4a]/best[height<={height}][ext=mp4]",
#         "outtmpl": "%(title)s.%(ext)s",
#         "merge_output_format": "mp4",
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(url, download=True)
#         filename = ydl.prepare_filename(info).rsplit(".", 1)[0] + ".mp4"
#         return filename, info.get("title", "video")

# # --- Streamlit UI ---
# st.title("🎬 YouTube Downloader")

# url = st.text_input("Enter YouTube video URL:")
# choice = st.radio("Download as:", ["Audio", "Video"])

# if choice == "Audio":
#     quality = st.selectbox("Select audio quality:", list(AUDIO_QUALITIES.keys()))
# else:
#     quality = st.selectbox("Select video quality:", list(VIDEO_QUALITIES.keys()))

# if st.button("Download"):
#     if url.strip():
#         with st.spinner("Downloading..."):
#             try:
#                 if choice == "Audio":
#                     file_path, title = download_audio(url, AUDIO_QUALITIES[quality])
#                     mime = "audio/mpeg"
#                 else:
#                     file_path, title = download_video(url, VIDEO_QUALITIES[quality])
#                     mime = "video/mp4"

#                 with open(file_path, "rb") as f:
#                     st.download_button(
#                         label=f"⬇️ Download {title} ({quality} {choice})",
#                         data=f,
#                         file_name=os.path.basename(file_path),
#                         mime=mime,
#                     )

#                 os.remove(file_path)  # cleanup
#             except Exception as e:
#                 st.error(f"Error: {e}")
#     else:
#         st.warning("Please enter a valid YouTube URL.")


import streamlit as st
import yt_dlp
import os

AUDIO_QUALITIES = {
    "48 kbps": "bestaudio[abr<=48]",
    "128 kbps": "bestaudio[abr<=128]",
    "320 kbps": "bestaudio[abr<=320]",
}

VIDEO_QUALITIES = {
    "144p": 144,
    "240p": 240,
    "480p": 480,
    "720p": 720,
    "1080p": 1080,
}

def download_audio(url, format_selector):
    ydl_opts = {
        "format": format_selector,
        "outtmpl": "%(title)s.%(ext)s",
        "writethumbnail": True,
        "postprocessors": [
            {"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "320"},
            {"key": "EmbedThumbnail"},
            {"key": "FFmpegMetadata"}
        ],
        "prefer_ffmpeg": True,
        "converttothumbnail": "jpg",
        "postprocessor_args": ["-id3v2_version", "3"],
        "quiet": True,
        "nocheckcertificate": True,
        "geo_bypass": True,
        "youtube_include_dash_manifest": False,
        "http_headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/116.0.0.0 Safari/537.36"
        },
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info).rsplit(".", 1)[0] + ".mp3"
        return filename, info.get("title", "audio")

def download_video(url, height):
    ydl_opts = {
        "format": f"bestvideo[height<={height}][ext=mp4]+bestaudio[ext=m4a]/best[height<={height}][ext=mp4]",
        "outtmpl": "%(title)s.%(ext)s",
        "merge_output_format": "mp4",
        "quiet": True,
        "nocheckcertificate": True,
        "geo_bypass": True,
        "http_headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/116.0.0.0 Safari/537.36"
        },
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info).rsplit(".", 1)[0] + ".mp4"
        return filename, info.get("title", "video")

# --- Streamlit UI ---
st.title("🎬 YouTube Downloader")

url = st.text_input("Enter YouTube video URL:")
choice = st.radio("Download as:", ["Audio", "Video"])

if choice == "Audio":
    quality = st.selectbox("Select audio quality:", list(AUDIO_QUALITIES.keys()))
else:
    quality = st.selectbox("Select video quality:", list(VIDEO_QUALITIES.keys()))

if st.button("Download"):
    if url.strip():
        with st.spinner("Downloading..."):
            try:
                if choice == "Audio":
                    file_path, title = download_audio(url, AUDIO_QUALITIES[quality])
                    mime = "audio/mpeg"
                else:
                    file_path, title = download_video(url, VIDEO_QUALITIES[quality])
                    mime = "video/mp4"

                with open(file_path, "rb") as f:
                    st.download_button(
                        label=f"⬇️ Download {title} ({quality} {choice})",
                        data=f,
                        file_name=os.path.basename(file_path),
                        mime=mime,
                    )

                os.remove(file_path)  # cleanup
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid YouTube URL.")
