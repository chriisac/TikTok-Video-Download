import asyncio
from app import app
from app import downloadManager
from app import downloads_list


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(downloadManager.download_files(downloads_list))
    app.run(debug=True, use_reloader=False, loop=loop)
    loop.close()
