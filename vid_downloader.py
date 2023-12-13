from pytube import YouTube

# Hardcode the YouTube video URL
link = "https://www.youtube.com/watch?v=6r_QBgq-seA"

try:
    yt = YouTube(link)
    print("Title: ", yt.title)
    print("Views: ", yt.views)

    # Download the highest resolution stream
    yd = yt.streams.get_highest_resolution()
    download_path = r'C:\Fullstack\WebGIS Videos'
    yd.download(download_path)

    print("Download completed successfully. Video saved in:", download_path)

except Exception as e:
    print("Error:", str(e))