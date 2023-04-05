let list = document.getElementById("downloadList");
const listItems = [];
const listColumns = { "filename":0,
                      "progress":1,
                      "status"  :2};

class ItemDownload
{
  constructor(fileName, newId)
  {
    this.id = newId;
    this.fileName = fileName;
    this.progress = "0";
    this.status   = "Downloading";
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
