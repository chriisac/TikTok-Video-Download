from quart import Quart
from app import downloadManager
import asyncio


app = Quart(__name__)

downloads_list = downloadManager.DownloadList()

from app import routes

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(downloadManager.download_files(downloads_list))
    app.run(debug=True, use_reloader=False, loop=loop)
