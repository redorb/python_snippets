import youtube_dl


if __name__ == "__main__":
    video_url = 'https://www.youtube.com/watch?v=0RaJkDX7M4w'
    ydl_opts = {'outtmpl': '%(id)s.%(ext)s'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
        