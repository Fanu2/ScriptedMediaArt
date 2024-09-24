import yt_dlp as youtube_dl

def download_video(url, output_file):
    ydl_opts = {
        'outtmpl': output_file,
        'format': 'best',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

video_url = 'https://x.com/i/status/1824680477875228808'  # Replace with the actual video URL
download_video(video_url, '/home/jasvir/Downloads/downloaded_video.mp4')
