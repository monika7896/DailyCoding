// A JavaScript program to find a peak element

// Find the peak element in the array
function findPeak(arr, n) {

    // first or last element is peak element
    // if only one element
    if (n == 1) return arr[0];
    // if oth greater than 1th
    if (arr[0] >= arr[1]) return arr[0];
    // if lat greater than 2nd last
    if (arr[n - 1] >= arr[n - 2])
        return arr[n - 1];

    // check for every other element
    for (var i = 1; i < n - 1; i++) {
        console.log("array")
        // check if the neighbors are smaller
        if (arr[i] >= arr[i - 1] && arr[i] >= arr[i + 1]) return arr[i];
    }
}

// Driver Code
var arr = [99, 93, 20, 4, 91, 100];
var n = arr.length;
console.log("Index of a peak point is " + findPeak(arr, n));

	// This code is contributed by rdtank.
