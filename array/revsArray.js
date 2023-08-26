function reverseArray(arr) {
    let reversed = [];
    for (let i = arr.length - 1; i >= 0; i--) {
        reversed.push(arr[i]);
    }
    console.log(reversed)
    return reversed;
}

let arr = [9, 8, 0]
reverseArray(arr)
