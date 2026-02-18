// lexical env
function ravi() {
    // console.log("Hi ravinder");
    return "Hi ravi!";
}

function multi(a, b) {
    return a * b
}
console.log(ravi());
console.log(multi(2, 2));


//  hoisting
// when js file executed then firslty all `var` variables ko memory allot hoti h
// var support hoisting let and const not
// whenever we create variable using var, it can be accessed by the window, but let and const not be accessable by window
var a = 10;
console.log(a);

let b = 300;
const c = 909;
// window.onload(alert("hello"))
console.log(window);

function clicked() {
    alert("Bhai ispe click mat kar");
}


document.getElementById("txt").innerHTML = "<h1 class='btn btn-danger'>LPU</h1>";
document.getElementById("txt").innerText = "LPU";

a = document.getElementsByTagName("h2")
console.log(a);
a[0].innerText = "tag name se access";

b = document.getElementsByClassName('uni')
console.log(b)
b[1].innerText = "Class se"

// query selectory
x = document.querySelector('.uni')
y = document.querySelectorAll('.uni')
console.log(x)
console.log(y)


//  what is the difference between node list and html collection


function change() {
    document.getElementById('para').innerText = "change ho gya";
}


function txtin() {
    n = document.getElementById("name").value;
    document.querySelector('#txt1').innerText = n;
}

function imgadd() {
    document.querySelector('img').src = "https://ums.lpu.in/assets/img/logos/lpu-logo.svg";
}


document.querySelector('#txt').style.color = "green"

function hide() {
    document.querySelector('h2').style.visibility = 'hidden'
    document.querySelector('#hs').innerText = 'show'
}

function show() {
    document.querySelector('h2').style.visibility = 'visible'
    document.querySelector('#hs').innerText = 'hide'
}

function hsbtn() {
    if (document.querySelector('h2').style.visibility == 'hidden') {
        show()
    } else {
        hide()
    }
}

function tble() {
    t = document.getElementById("printTable").value;
    cl = document.getElementsByClassName('container')
    console.log(cl)
    console.log(cl[0])

    cl[0].innerHTML = '<table id="tb" class="table"></table>';
    tb = document.querySelector('#tb')
    tbl =""
    for (let i = 1; i < 11; i++) {
        tbl += `<tr> <td>${t}</td> <td>*</td> <td>${i}</td><td>=</td>  <td>${t * i}</td> </tr>`
    }
    tb.innerHTML = tbl;
}


function printtable(){
    n = document.getElementById("num").value;
    tb = document.getElementById("tablebody");
    tb.innerHTML = "" // clean the table body
    for (let i=1;i<=10;i++){
        let row = document.createElement("tr");  //creating a row
        let col = document.createElement("td"); // creating a column
        col.textContent = n + " x " + i + " = "+(n*i);
        row.appendChild(col);
        tb.appendChild(row)

    }
}