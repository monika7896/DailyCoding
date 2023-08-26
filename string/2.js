function reverseWords(str) {
    let wordsArr = str.split(" ");
    console.log(wordsArr.length - 1)

    let reversedArr = [];
    for (let i = wordsArr.length - 1; i >= 0; i--) {
        reversedArr.push(wordsArr[i]);
    }
    return reversedArr.join(" ");
}

// Example usage:
const originalStr = "Hello my world ";
const reversedStr = reverseWords(originalStr);

console.log(reversedStr); // Output: "world Hello"
