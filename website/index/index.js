

let i = 0;
function addNode(the){
    let tag = document.createElement('li');
    let div = document.createElement('div');
    div.style.width = "50px"
    div.style.height = "50px";

    let course = the.textContent;
    let text = document.createTextNode(`CSE`);
    fetchJSON(`http://localhost:8080/courses/${course}`);

    div.setAttribute("id",`CSE${i++}`);
    div.appendChild(text);
    div.className = "circle"; 
    console.log(div);

    div.addEventListener('click',(e)=>{
        e.stopPropagation();
        addNode(div);
    });

    tag.appendChild(div);
    
    let main = document.getElementById(the.id);

    let ulArr = main.getElementsByTagName('ul');
    let list = document.createElement('ul');


    if(ulArr[0] != undefined)
        list = ulArr[0];
    
    list.className = 'nodeList';
    list.appendChild(tag);
    main.appendChild(list);

        
   }

function courseToFirst(){
    let courseName = document.getElementById('courseName');
    document.getElementById('firstCircle').textContent=courseName.value;
}

async function fetchJSON(url){
    console.log(await fetch(url).then((res) =>{
        return res.json();
    }));
}