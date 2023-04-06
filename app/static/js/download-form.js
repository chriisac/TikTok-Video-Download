let list = document.getElementById("downloadList");
let urlField = document.getElementById("url");
const listItems = [];
const listColumns = { "filename":0,
                      "progress":1,
                      "status"  :2};

class ItemDownload
{
  constructor(fileName, newId, progress, status)
  {
    this.id = newId;
    this.fileName = fileName;
    this.progress = progress;
    this.status   = status;
    list.insertAdjacentHTML("beforeend",`<tr id='${this.id}'>
                                              <td>${this.fileName}</td>
                                              <td>${this.progress}%</td>
                                              <td>${this.status}</td>
                                            </tr>`);

    this.tr = list.querySelectorAll("tr")[this.id];
  }

  updateDownloadProgress(percentage)
  {
    if(percentage >=0)
    {
      this.progress = percentage;
      this.tr.querySelectorAll("td")[listColumns.progress].innerHTML = this.progress + "%";
      return true;
    }
    return false;
  }

  updateDownloadStatus(status)
  {
    if(status)
    {
      this.status = status;
      this.tr.querySelectorAll("td")[listColumns.status].innerHTML = this.status;
      return true;
    }
    return false;
  }

}

function addNewDownload()
{
  let newId = list.getElementsByTagName("tr").length;
  let url = document.getElementById("url");
  let fileName = url.value.substr(url.value.lastIndexOf("/")+1) + ".mp4";
  listItems.push(new ItemDownload(fileName, newId));
}

async function sendURL()
{
  let myPromise = new Promise(function(resolve) {
    let req = new XMLHttpRequest();
    req.open('GET', "/add?url=" + urlField.value);
    req.onload = function() {
      if(req.status == 200)
      {
        resolve(req.response);
      }
      else
      {
        resolve("{}");
      }
    };
    req.send();
  });
  console.log(await myPromise);
}

async function updateDonwloadList()
{
  let myPromise = new Promise(function(resolve) {
    let req = new XMLHttpRequest();
    req.open("GET", "/list");
    req.onload = function() {
      if (req.status == 200)
      {
        resolve(req.response);
      }
      else
      {
        resolve("Error")
      }
    };
    req.send();
  });
  downloadList = JSON.parse(await myPromise);
  console.log(downloadList);

  for(let id in downloadList){
      if(id > listItems.length){
        listItems.push(new ItemDownload(downloadList[id].fileName,
                                        id,
                                        downloadList[id].progress,
                                        downloadList[id].status)
                                      );
      }
      else {
        listItems[id-1].updateDownloadProgress(downloadList[id].progress);
      }
  }

}
