// window.onload(alert("welcome"));

// a = 10
// console.log(a)

// b=30
// console.log(a+b)

// z = 10
// let x =30
// value can be updated but let variable can not be re initialized
// var w = 20
// const h = 10
//  const value can't be updated


// var x =30
// console.log(x)


// let a = 10
// let b = 34

// if (a > b ){
//     console.log("bhai a ki value badi hai")
// } else{
//     console.log(" a ki value choti rah gyi")
// }

// for (let i=1;i<9;i++){
//     console.log(`A is ${i}`)
// }

let s1 = "hello world";
let s2 = "ravi";
// console.log(s1+" " +s2)
// // string template
// let s3 = `this is john's ${s2} file`
// console.log(s3)


// console.log(s2.length)
// console.log(s1[0])
// console.log(s1.charAt(0))
// console.log(s1.charCodeAt(0)) //print the code/ascii of the character
// console.log(s1.endsWith("ld"))
// console.log(s1.codePointAt(0))
// console.log(s1.concat(" ",s2))
// console.log(s1.lastIndexOf('o'))
// console.log(s1.slice(0,5))
// console.log(s1.slice(6))
// console.log(s1.slice(-5))
// console.log(s1.indexOf('o'))
// console.log(s1.indexOf('o', s1.indexOf('o')+1))
// console.log(s1.search('o'))


// objects are variable can store both function as well as the variables, values storein the form of key:value called properties and functions are stores as key:function() called methods.

let obj = {
    "ravi":1,
    "rohit":122,
    "mohit":121
};



const car = {}

car.color = 'red';
car.model = 2025;
car.type = 'suv';
car.company = 'ford';
car.seater = 50;
car.avg = 12.65;

console.log(car);
console.log(obj)
console.log(obj.ravi)
console.log(obj.rohit)
console.log(car['avg'])
