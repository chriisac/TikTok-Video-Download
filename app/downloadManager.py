import asyncio
import aiohttp
import aiofiles

CHUNK_SIZE = 1024*1024
DOWNLOAD_FOLDER = "Downloads/"


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
                    async with aiofiles.open(DOWNLOAD_FOLDER+self.fileName, 'wb') as f:
                        downloaded = 0
                        async for chunk in response.content.iter_any():
                            if chunk:
                                downloaded += chunk.__sizeof__()
                                progress = float("{:0.2f}".format((downloaded*100)/response.content_length))
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


class DownloadList:
    def __init__(self):
        self.id = 0
        self.list = {}

    def add(self, url):
        self.id += 1
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
