from app import app
from app import downloadManager
from app import downloads_list
import multiprocessing
import time


@app.after_request
def test(response):
    downloadManager.download_files(downloads_list)
    return response

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

