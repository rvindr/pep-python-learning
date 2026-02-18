/*
function clicked() {
    let num = document.getElementById("num").value;
    let text = "";
    if (isNaN(num) || num<1 || num>10) {
        text = "Input not valid";
    }
    else {
        text = "Valid";
    }
    document.getElementById("text").innerHTML = text;
}
*/

/*
function clicked2() {
    let x = document.forms['myForm']['fname'].value;
    
    if (x == "") {
        alert("Name must be filled");
        return false;   
    }
} 
*/  

/*
let box = document.getElementById("box");

box.addEventListener("mouseover", function() {
    box.innerHTML = "Mouse is over the box";
});
box.addEventListener("mouseout", function() {
    box.innerHTML = "Mouse is now out of box";
});
document.addEventListener("mousemove", function(event) {
    document.getElementById('txt').innerHTML = "X: " + event.clientX + " Y: " + event.clientY;
});
*/

/*
setInterval(showTime, 1000);

function showTime() {
    const d = new Date();
    document.getElementById('txt').innerHTML = d.getHours() + ":" + d.getMinutes() + ":" + d.getSeconds();
}
*/

/*
//setInterval: sets a clock interval which executes a function repeatedly, with a fixed time delay between each call
//setTimeout: sets a timer which executes a function once the timer expires
//clearInterval: clears a timer set with setInterval()
//clearTimeout: clears a timer set with setTimeout()
document.getElementById('btn').addEventListener('click', function() {
    setTimeout(showmsg, 2000);
});

function showmsg() {
    document.getElementById('txt').innerHTML = "Hello LPU!";
}
*/

/*
let interval;
let cunt = 0;

const btnstart = document.getElementById('start');
const btnstop = document.getElementById('stop');

document.getElementById('start').addEventListener('click', function() {
    interval = setInterval(counter,1000);
});

document.getElementById('stop').addEventListener('click', function() {
    clearInterval(interval);
});

function counter() {
    cunt++;
    document.getElementById('txt').innerHTML=cunt;
}
*/

/*
function add(a,b){
    return a+b;
}
console.log(add(3,4))
const add2 = function(a,b){return a+b;}
console.log(add2(10,4))
const add3 = (a,b) => a+b; 
console.log(add3(3,40))
*/

/*
x = sum(1,2,3,4,5,6,7)
function sum() {
    let s = 0
    for (let i=0; i<arguments.length;i++) {
        // console.log(arguments[i]);
        s += arguments[i];
    }
    console.log(s);
}

y = add(1,2,3,4,5,6,7)
function add(...args) {
    let s=0;
    for (let a of args){
        s+=a;
    }
    return s;
}
console.log(y);     
*/


// const uni = ["LPU","CU","DU"];
// console.log(typeof(uni)); // object
// console.log(uni);
// console.log(uni[0]);
// // document.getElementById('txt').innerHTML=uni.toString();
// uni.pop();
// uni.push('CTU');
// uni.shift(); // to remove element from the start
// uni.unshift('SRMU'); // to add element at the start
// uni.splice(2,0,"DBU","CTU")
// console.log(uni);

// let txt = "";
// uni.forEach(myfun);
// document.getElementById('txt').innerHTML = txt;
// function myfun(val, index, array) {
//     txt += val + "<br>";
// }

// const uni1 = uni.map(myfun);
// function myfun(val, index, arr) {
//     return val + " University";
// }
// console.log(uni1);

// const age = [14,18,19,40,29,28];

// const over18 = age.filter(myfun);
// function myfun(val, index, arr) {
//     return val>=18;
// }
// console.log(over18);

// const even = age.filter(myfun1);
// function myfun1(val, index, arr) {
//     return val%2==0;
// }
// console.log(even);

const age = [14,18,19,30,10,8,29,28];
const res = age.reduce(myfun);
function myfun(output, val, index, arr) {
    return output + val;
}
console.log(res);