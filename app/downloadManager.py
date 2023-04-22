import asyncio
import aiohttp
import aiofiles
import requests

from app import tiktok

CHUNK_SIZE = 1024 * 1024
DOWNLOAD_FOLDER = "Downloads/"
HEADERS = {'User-Agent': 'TikTok 26.2.0 rv:262018 (iPhone; iOS 14.4.2; en_US) Cronet'}
TIKTOK_API_URL = "https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/feed/?aweme_id="


class Download:
    def __init__(self, download_id, file_name, url):
        self.id = download_id
        self.fileName = file_name
        self.progress = 0
        self.status = "Initializing"
        self.url = url
        self.stream = ""

    async def download(self):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url) as response:
                    async with aiofiles.open(DOWNLOAD_FOLDER + self.fileName, 'wb') as f:
                        downloaded = 0
                        async for chunk in response.content.iter_any():
                            if chunk:
                                downloaded += chunk.__sizeof__()
                                progress = float("{:0.2f}".format((downloaded * 100) / response.content_length))
                                if progress > 100.0:
                                    progress = 100.0
                                self.progress = progress
                                await f.write(chunk)
                        self.status = "Complete"
        except aiohttp.ClientError as e:
            self.status = "Error"
            print(f"Error downloading {self.url}: {e}")
        except OSError as e:
            self.status = "Error"
            print(f"Error writing to file {self.fileName}: {e}")

    def update_file_name(self, name):
        self.fileName = name

    def update_progress(self, new_progress):
        self.progress = new_progress

    def update_status(self, new_status):
        self.status = new_status



async def get_tiktok_video_data(url):
    data = {}
    try:
        id_vid = url.rsplit("/video/")[1]
        if len(id_vid) > 19:
            id_vid = id_vid.rsplit("?")[0]

        async with aiohttp.ClientSession() as session:
            async with session.get(TIKTOK_API_URL + id_vid, headers=HEADERS) as response:
                response.raise_for_status()
                json_data = await response.json()
                data["url"] = json_data["aweme_list"][0]["video"]["play_addr"]["url_list"][0]

        data["filename"] = id_vid + ".mp4"
    except aiohttp.ClientError as e:
        print(f"An error occurred: {e}")

    return data


class DownloadList:
    def __init__(self):
        self.id = 0
        self.list = {}

    async def add(self, url):
        self.id += 1
        if url.find("tiktok"):
            tiktok_video = await get_tiktok_video_data(url)
            if tiktok_video == {}:
                print("Error getting tiktok video data")
                return False
            self.list[self.id] = Download(self.id, tiktok_video["filename"], tiktok_video["url"])
            return True
        filename = url.split("/")[-1]
        self.list[self.id] = Download(self.id, filename, url)
        return True

    def get(self):
        list_to_json = {}
        for item in self.list:
            list_to_json[item] = self.list[item].__dict__
        return list_to_json


async def download_files(download_list):
    while True:
        downloads = download_list.get()
        for download_id in downloads:
            if download_list.list[download_id].status == "Initializing":
                download_list.list[download_id].status = "Downloading"
                asyncio.ensure_future(download_list.list[download_id].download())
        await asyncio.sleep(1)
