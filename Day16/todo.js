function addTask() {
    let task = document.getElementById('task').value;
    if (task == "") return;
    let li = document.createElement('li');
    li.textContent = task + " ";
    let delbtn = document.createElement('button');
    delbtn.textContent = "X";
    const bt = document.createAttribute("class")
    bt.value = 'btn btn-danger m-3 text-end';
    const h3 = document.createAttribute("class")
    h3.value = 'h5 list-group-item';
    li.setAttributeNode(h3)
    delbtn.setAttributeNode(bt)
    delbtn.onclick = function () {
        li.remove();
    };
    li.appendChild(delbtn);
    document.getElementById('task_list').appendChild(li);
    document.getElementById('task').value = '';
}

// function addcard() {
//     let card = document.createElement("div");
//     card.style.border = "1px solid blue";
//     card.style.padding = "10px";
//     card.style.margin = "10px";
//     card.style.width = "200px";
//     let title = document.createElement("h3");
//     let price = document.createElement('p')
//     price.textContent = "Price: $599";
//     let btn = document.createElement("button");
//     btn.textContent = "Buy Now";
//     card.appendChild(price);
//     card.appendChild(title);
//     card.appendChild(btn);
//     const att = document.createAttribute("class");
//     att.value = "card bg-info text-center h3";
//     const bt = document.createAttribute("class");
//     bt.value = "btn btn-primary";
//     btn.setAttributeNode(bt);
//     card.setAttributeNode(att);
//     document.getElementById("rvi").appendChild(card);
// }


// create a todo list havinng add item delet item
// create a employee table with emp id name dept salary and also have a delete button