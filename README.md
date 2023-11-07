
# Simple YouTube Music Downloader

This is a straightforward Python script that allows users to download audio from YouTube videos as MP3 files. It utilizes the [pytube](https://pytube.io/) library for fetching video content and converting it into an audio format.

## Usage

1. Clone or download the repository to your local machine.
2. Modify the `download_path` variable to specify the directory where you want to save downloaded music.
3. Run the script and provide the YouTube URL of the video you want to download.

## How it Works

1. The script takes a YouTube URL as input.
2. It fetches the available audio streams for the video.
3. It generates a random name for the downloaded file and saves it as an MP3 in the specified directory.

## Requirements

- Python 3.x
- [pytube](https://pytube.io/)

## Usage Example

```python
python youtube_downloader.py
```

Enter the YouTube URL when prompted, and the script will download the audio for you.

## Note

Please be aware of YouTube's terms of service when using this script. Only download content that you have the right to access.

---

Feel free to customize and expand upon this description to include any additional information or features about your script!
