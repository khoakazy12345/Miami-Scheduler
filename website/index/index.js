const url = "localhost:8080";

function courseToFirst() {
  var list = document.getElement('listOfCourses');
  list.outerHTML = "";
  fetchJSON(url);
  document.createElement("ul");
}

async function fetchJSON(url) {
  console.log(
    await fetch(url).then(res => {
      return res.json();
    })
  );
}
