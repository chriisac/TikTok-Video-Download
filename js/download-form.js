let NListItems = 0;

function addNewDownload()
{
  let url = document.getElementById("url");
  let list = document.getElementById("downloadList");
  let fileName = url.value.substr(url.value.lastIndexOf("/")+1) + ".mp4";
  list.insertAdjacentHTML("beforeend","<tr id='"+(NListItems++)+"'><td>" + fileName +"</td><td>0%</td><td>Downloading</td></tr>");
}
