// Create and initialize an array
let items = ['GFG', 'Geeks', 'G4G'];

// Display the array items
console.log(items);

// Create a new empty array
let new_Array = [];

// forEach loop to push elements
// into new array
// 	items.forEach(function (item) {
// 		new_Array.push(item);
// 	});
console.log(items.length)
for (let i = 0; i < items.length; i++) {
    new_Array.push(items[i])

}

// Display the new array of items
console.log(new_Array);
