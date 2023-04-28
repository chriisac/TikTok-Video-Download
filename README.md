# TikTok Video Downloader

This is a simple TikTok video downloader built with Python using Quart framework. It allows you to download TikTok videos by providing the video URL. The downloaded videos will be saved in a local directory specified as a constant in the `app.py` file.

## Requirements

- Python 3.6+
- Quart framework

## Installation

1. Clone the repository: `https://github.com/chriisac/TikTok-Video-Download.git`
2. Navigate to the project directory: `cd TikTok-Video-Download`
3. Create a new virtual environment: `python3 -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate` (for Linux/Mac), or `.\venv\Scripts\activate` (for Windows)
5. Start the server: `python main.py`

## Usage

- Open your web browser and go to `http://localhost:5000` to access the web interface.
- Enter the TikTok video URL in the input field and click the "Download" button.
- The downloaded video will be saved in the `Downloads` directory.
