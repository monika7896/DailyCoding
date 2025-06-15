// Top K Frequent in Array


function highfreq(arr, k) {
    const count = {};

    // Single loop to count frequencies
    for (const num of arr) {
        count[num] = (count[num] || 0) + 1;
    }

    // Sort unique values based on frequency and value (this is not a loop over full arr)
    return Object.keys(count)
        .sort((a, b) => {
            if (count[b] === count[a]) {
                return b - a; // higher number first if frequency same
            }
            return count[b] - count[a]; // higher frequency first
        })
        .slice(0, k)
        .map(Number);
}

let arr = [3, 1, 4, 4, 5, 2, 6, 1];
const k = 2;
console.log(highfreq(arr, k))
