function findSum(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    console.log(sum)
    return sum;
}

let arr = [10, 20]
findSum(arr)
