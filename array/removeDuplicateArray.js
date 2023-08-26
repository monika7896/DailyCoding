function removeDuplicates(arr) {
    let uniqueArr = [];
    for (let i = 0; i < arr.length; i++) {
        console.log(uniqueArr.indexOf(arr[i]) === -1)
        if (uniqueArr.indexOf(arr[i]) === -1) {
            uniqueArr.push(arr[i]);
        }
    }
    console.log(uniqueArr)
    return uniqueArr;
}
let arr = [9, 7, 9, 6]
removeDuplicates(arr)
