function missing_number(arr, count) {
    let output = [];
    for (let i = 0; i <= count; i++) {
        if (!arr.includes(i)) {
            output.push(i);
        }
    }
    return output;
}

const count = 10;
const arr = [1, 2, 4, 5];
console.log(missing_number(arr, count));
