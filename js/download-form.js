let list = document.getElementById("downloadList");
const listItems = [];

class ItemDownload
{
  constructor(fileName, newId)
  {
    this.id = newId;
    this.fileName = fileName;
    this.progress = "0";
    list.insertAdjacentHTML("beforeend",`<tr id='${this.id}'>
                                              <td>${this.fileName}</td>
                                              <td>${this.progress}%</td>
                                              <td>Downloading</td>
                                            </tr>`);
  }

  updateDownloadProgress(percentage)
  {
    this.progress = percentage;
    list.querySelectorAll("tr")[this.id].querySelectorAll("td")[1].innerHTML = this.progress + "%";
    return true;
  }

}

function addNewDownload()
{
  let newId = list.getElementsByTagName("tr").length;
  let url = document.getElementById("url");
  let fileName = url.value.substr(url.value.lastIndexOf("/")+1) + ".mp4";
  listItems.push(new ItemDownload(fileName, newId));
}
