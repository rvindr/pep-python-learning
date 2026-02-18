// setTimeout(() => {
//     console.log('Hello...') 
// }, 2000);

// callback funciton -> function jo dusre function me call krke run karte h 

// function greet(name, callback){
//     console.log('Hi', name);
//     callback() 
// }

// function mrng(){
//     console.log('Good morning');

// }
// greet('ravi', mrng)



// function fetchData(callback){
//     setTimeout(() => {
//         console.log('Data fetching...');
//         callback();
//     }, 3000);
// }



// fetchData(()=>{
//     console.log('Processning callback funciton');
// })

// //callback Hell -> when function have another function and another function
// // to handle this we have promises
// setTimeout(()=>{
//     console.log('wake up for class');
//     setTimeout(() => {
//         console.log('ready for class')
//         setTimeout(()=>{
//             console.log('Going to class');

//         },1000)
//     }, 1000);
// }, 1000)


// // promises - status, fullfilled, rejected
// let promise = new Promise((resolve, reject)=>{
//     let success = true;
//     if (success){
//         resolve('Data received');
//     }else{
//         reject("Data processing failed");
//     }
// })

// promise
//     .then(res => console.log(res))
//     .catch(err => console.log(err));

// async function getData(){
//     try{
//         let response = await fetch('https://api.github.com/users/rvindr');
//         // console.log(response);
//         let data  = await response.json();
//         console.log(data);
//     }catch(err){
//         console.log(err);
//     }
// }

// async function getGit() {
//     let res = await fetch('https://api.github.com/users/rvindr');
//     let data = await res.json();
//     console.log(data)
// }

// fetch('https://api.github.com/users/rvindr')
//     .then(res => res.json())
//     .then(data => console.log(data))
//     .catch(err=> console.log(err))

// getData();
// getGit();

