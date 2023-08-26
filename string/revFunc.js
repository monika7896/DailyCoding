// Function to reverse any sequence
// starting with pointer begin and
// ending with pointer end
function reverse(s, begin, end) {
    while (begin < end) {
        let charArray = [...s];
        let temp = charArray[begin];
        charArray[begin] = charArray[end];
        charArray[end] = temp;
        begin++;
        end--;
        s = charArray.join("");
    }
    return s;
}

function reverseWords(s) {
    let word_begin = -1;

    // /* temp is for word boundary */
    let i = 0;

    /*STEP 1 of the above algorithm */
    while (i < s.length) {

        /*This condition is to make sure that the
        string start with valid character (not
        space) only*/
        if ((word_begin == -1) && (s[i] != ' ')) {
            word_begin = i;
        }
        if (word_begin != -1
            && ((s[i + 1] == ' ') || (i + 1 == s.length))) {
            s = reverse(s, word_begin, i);
            word_begin = -1;
        }
        i++;
    } /* End of while */

    /*STEP 2 of the above algorithm */
    s = reverse(s, 0, s.length - 1);
    return s;
}

// Driver Code
let s = "i like this program very much";

// Function call
s = reverseWords(s);
console.log(s);


// This code is contributed by akashish__
