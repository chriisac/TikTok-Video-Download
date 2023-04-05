let list = document.getElementById("downloadList");
const listItems = [];

class ItemDownload
{
  constructor(fileName, id)
  {
      list.insertAdjacentHTML("beforeend",`<tr id='${id}'>
                                              <td>${fileName}</td>
                                              <td>0%</td>
                                              <td>Downloading</td>
                                            </tr>`);
  }
}


function addNewDownload()
{
  let newId = list.getElementsByTagName("tr").length;
  let url = document.getElementById("url");
  let fileName = url.value.substr(url.value.lastIndexOf("/")+1) + ".mp4";
  listItems.push(new ItemDownload(fileName, newId));
}
