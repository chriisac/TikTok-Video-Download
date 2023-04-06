from flask import Flask

app = Flask(__name__)

from app import downloadManager
downloadsList = downloadManager.DownloadList()

from app import routes

