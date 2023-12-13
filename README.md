# py_utube_downloader
Overview
This script downloads a YouTube video using the pytube library and saves it to a specified local directory.

Dependencies
Install the required dependencies using the following command:


pip install pytube
Usage
Open the script in your preferred Python IDE.

Replace the link variable with the YouTube video URL you want to download.

python
Copy code
link = "https://www.youtube.com/watch?v="
Run the script.

The script will print the title and views of the video, download the highest resolution stream, and save it to the specified local directory.
Download completed successfully. Video saved in: C:\Fullstack\WebGIS Videos
Customization
Download Path: You can customize the download_path variable to specify the directory where you want to save the downloaded video.


download_path = r'C:\your_path\videos'
Error Handling
If there are any issues during the download process, an error message will be displayed.

Disclaimer
This script is provided as-is. Use it responsibly and respect YouTube's terms of service.

