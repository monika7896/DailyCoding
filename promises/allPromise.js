// Write a program to create a Promise that resolves after a given timeout.

// function timeoutPromise(timeout) {
    
//     return new Promise((resolve, reject)=>{
//         setTimeout(()=>{
//             resolve(`Promise resolved after ${timeout} ms`);
//     }, timeout);

//     })
     
// };

// timeoutPromise(1000)
// .then((result)=>{
//     console.log(result);
// })
// .catch((error)=>{
//     console.error("eroor");
// })

// Write a program to create a Promise that rejects with a given error message.


// function errorPromise(errorMessage) {
//     return new Promise((resolve ,reject)=>{
//             reject(new Error(errorMessage));
//     })
// };

// errorPromise("Oops, something went wrong!").then((values)=>{console.log(values)
    
// }) 
// .catch(error => {
//     console.error(error.message);
//   });

// Write a program to create a Promise that resolves or rejects based on the result of a given condition.

// function conditionalPromise(condition) {
// return new Promise((resolve ,reject)=>{
//     if(condition){
//     resolve("kanha")
// }
// else
//       reject(new Error("Condition not met"));
// })
// };

// conditionalPromise(true).then((values)=>{
//     console.log(values)
// })
// .catch((error)=>{
//     console.error(error.message)
// })

// Write a program to create a Promise that resolves with a random number between 1 and 10.

// function randomPromise() {
//     return new Promise((resolve ,reject)=>{
//     const randomNumber = Math.floor(Math.random() * 10) + 1;
//     resolve(randomNumber);
        
//     })

// }
// randomPromise().then((value)=>{
//      console.log(value)

// })
// .catch((error)=>{
//          console.error(error)

// })

// Write a program to create a Promise that fetches data from an API and resolves with the response data.
// Write a program to create a Promise that resolves after a given timeout.

// function timeoutPromise(timeout) {
    
//     return new Promise((resolve, reject)=>{
//         setTimeout(()=>{
//             resolve(`Promise resolved after ${timeout} ms`);
//     }, timeout);

//     })
     
// };

// timeoutPromise(1000)
// .then((result)=>{
//     console.log(result);
// })
// .catch((error)=>{
//     console.error("eroor");
// })

// Write a program to create a Promise that rejects with a given error message.


// function errorPromise(errorMessage) {
//     return new Promise((resolve ,reject)=>{
//             reject(new Error(errorMessage));
//     })
// };

// errorPromise("Oops, something went wrong!").then((values)=>{console.log(values)
    
// }) 
// .catch(error => {
//     console.error(error.message);
//   });

// Write a program to create a Promise that resolves or rejects based on the result of a given condition.

// function conditionalPromise(condition) {
// return new Promise((resolve ,reject)=>{
//     if(condition){
//     resolve("kanha")
// }
// else
//       reject(new Error("Condition not met"));
// })
// };

// conditionalPromise(true).then((values)=>{
//     console.log(values)
// })
// .catch((error)=>{
//     console.error(error.message)
// })

// Write a program to create a Promise that resolves with a random number between 1 and 10.

// function randomPromise() {
//     return new Promise((resolve ,reject)=>{
//     const randomNumber = Math.floor(Math.random() * 10) + 1;
//     resolve(randomNumber);
        
//     })

// }
// randomPromise().then((value)=>{
//      console.log(value)

// })
// .catch((error)=>{
//          console.error(error)

// })

// Write a program to create a Promise that fetches data from an API and resolves with the response data.

// function fetchPromise(url) {
//     return new Promise((resolve ,reject)=>{
//             fetch(url)
//             .then((response)=>{
//                 if(response.ok){
//                   resolve(response.json());

//                 }else
//        reject(new Error("Network response was not ok"));
                
//             }).catch((error)=>{
//                 reject(new Error("erooor"))
//             })
//     });
// };

// fetchPromise("https://jsonplaceholder.typicode.com/todos/1")
// .then((data)=>{console.log(data)
 
// })
// .catch((error)=>{console.error(error)}
// )






