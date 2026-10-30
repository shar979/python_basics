import yt_dlp
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors' :[
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }
    ],
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.dowload(['https://www.youtube.com/watch?v=dQw4w9WgXcQ'])