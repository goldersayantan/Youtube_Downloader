import yt_dlp
import os

def download_song(url):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s",
        "writethumbnail": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",  # High quality
            },
            {"key": "EmbedThumbnail"},
            {"key": "FFmpegMetadata"},
        ],
        "prefer_ffmpeg": True,
        "converttothumbnail": "jpg",
        "postprocessor_args": ["-id3v2_version", "3"],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info).rsplit(".", 1)[0] + ".mp3"
        print(f"✅ Downloaded: {info.get('title', 'audio')}")
        print(f"📂 Saved as: {filename}")
        return filename

if __name__ == "__main__":
    url = input("Enter YouTube video link: ").strip()
    if url:
        try:
            download_song(url)
        except Exception as e:
            print(f"❌ Error: {e}")
    else:
        print("⚠️ Please enter a valid YouTube link.")
