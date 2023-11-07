import string
import random
from pytube import YouTube

download_path = "your_path"

def download(url):
    youtube_content = YouTube(url)
    audio_streams = youtube_content.streams.filter(only_audio=True)
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    file_name = f"music_{random_string}.mp3"
    audio_streams[len(audio_streams) - 1].download(output_path=download_path, filename=file_name)

def main():
    url = input("Your Url: ")
    download(url)

if __name__ == '__main__':
    main()
