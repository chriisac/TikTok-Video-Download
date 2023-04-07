from flask import Flask
from app import downloadManager

app = Flask(__name__)

downloads_list = downloadManager.DownloadList()

from app import routes
