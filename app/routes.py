from quart import render_template, request
from app import app
from app import downloads_list


@app.route("/")
@app.route("/index")
async def index():
    return await render_template("index.html")


@app.route("/list")
async def list_downloads():
    return downloads_list.get()


@app.route("/add", methods=["GET"])
async def add_download():
    url = request.args.get("url", "")
    if url != "":
        if await downloads_list.add(url):
            return "success"
        else:
            return "failed"
    else:
        return "Error"
