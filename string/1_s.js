// Javascript code for the above approach
// Reverse words in a given string using constant space: using the slicing method and join functions:
let text = "i like this program very much";
// let str = text.split(" ");
// console.log(text.length)
// str.reverse();
let revStr = ""
for (let i = text.length - 1; i >= 0; i--) {
    // console.log(text[i])
    revStr += text[i]
}
// str = str.join(" ");
console.log(revStr);

// This code is contributed by garg28harsh.
