// // Sorting an array of objects by a specific property:


// const people = [
//   { name: 'zAlice', age: 30 },
//   { name: 'Bob', age: 25 },
//   { name: 'Charlie', age: 35 }
// ];
// console.log(people.sort((a,b)=>a.age-b.age));
// console.log(people.sort((a, b) => a.name.localeCompare(b.name)));

// // Removing duplicate elements from an array:

// const numbers = [1, 2, 3, 2, 1, 4, 5, 4];
// function distinctArr(numbers){
//   const  uniqueNumbers =[...new Set(numbers)]
//     return uniqueNumbers
    
// };
// // const uniqueNumbers = [...new Set(numbers)];
// console.log(distinctArr(numbers)),
// Grouping elements in an array based on a specific condition:

// let numbers = [1, 2, 3, 4, 5];
// // Output: { odd: [1, 3, 5], even: [2, 4] }
// const oddAndEvenNumbers=numbers.reduce((result,number) => 
// {
// result[number % 2=== 0 ? 'even':'odd'].push(number)
// return result;
// },{odd:[],even:[]});
// console.log(oddAndEvenNumbers)
// const oddAndEvenNumbers = numbers.reduce((result, number) => {
//   result[number % 2 === 0 ? 'even' : 'odd'].push(number);
//   return result;
// }, { odd: [], even: [] });


// function groupArr(n){
//     let resp={}
//     let odd=[];
//     let even=[]
//     for(let i =0;i<n.length ;i++){
//             if(n[i]%2!=0)
//                 odd.push(n[i])
            
//              if(n[i]%2==0)
//             even.push(n[i])
//     }
//     resp.odd=odd
//     resp.even=even
//     return resp
// };
// console.log(groupArr(numbers))

// Finding the most common element in an array:

// const fruits = ['apple', 'banana', 'orange', 'apple', 'banana'];
// function findMostCommonElement(arr) {
//   let counts = {};
//   let maxCount = 0;
//   let maxElement;

//   for (let i = 0; i < arr.length; i++) {
//     let element = arr[i];
//     counts[element] = (counts[element] || 0) + 1;
//     if (counts[element] > maxCount) {
//       maxCount = counts[element];
//       maxElement = element;
//     }
//   }

//   return maxElement;
// }
//          console.log(findMostCommonElement(fruits))
         
        //  Flattening a nested array:
        
//         const numbers = [[1, 2], [3, 4, 5], [6]];
// let flatArray=[].concat(...numbers)
// console.log(flatArray)

// Shuffling an array:

// const numbers = [1, 2, 3, 4, 5];
// const shuffledNumbers =numbers.sort(()=> Math.random()-0.5)

// // const shuffledNumbers = numbers.sort(() => Math.random() - 0.5);

// console.log(shuffledNumbers)
// Finding the intersection of two arrays:

// const array1 = [1, 2, 3, 4, 5];
// const array2 = [4, 5, 6, 7, 8];

// const intersection = array1.filter(value => array2.includes(value));

// console.log(intersection)









