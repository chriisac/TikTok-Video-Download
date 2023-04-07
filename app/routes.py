from flask import render_template
from flask import request
from app import app
from app import downloads_list



@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/list")
def list_downloads():
    return downloads_list.get()


@app.route("/add", methods=["GET"])
def add_download():
    url = request.args.get("url", "")
    if url != "":
        if downloads_list.add(url):
            return "success"
        else:
            return "failed"
    else:
        return "Error"


@app.route("/update", methods=["GET"])
def update_download():
    id = request.args.get("id", -1)
    if id != -1:
        downloads_list.list[int(id)].progress += 1
    return "success"
