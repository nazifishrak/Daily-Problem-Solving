// Longest Subarray of 1's After Deleting One Element
// Given a binary array nums, you should delete one element from it.

// Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
// Example 1:

// Input: nums = [1,1,0,1]
// Output: 3
// Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
// Example 2:

// Input: nums = [0,1,1,1,0,1,1,0,1]
// Output: 5
// Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
// Example 3:

// Input: nums = [1,1,1]
// Output: 2
// Explanation: You must delete one element.

// const template = (arr) =>{
//     // init left and right pointers 
//     const l=0, r=0, n = arr.length, ans =0
//     for(; r<n; r++){
//         for(; invalidWindow(); l++){

//         }

//         ans = combination(old_ans, new_calc)

//     }
//     return ans
// }


function longestSubArray(arr) {
    let l=0, r=0, n=arr.length, ans =0, count =0;
    function invalidWindow(){
        return count>1
    }
    for (; r<n; r++){
        if(arr[r]==0) count++
        
        for (; invalidWindow(); l++){
            if (arr[l]==0) count--

        }
        ans = Math.max(ans, r-l+1)

    }
    return ans-1
}

console.log(longestSubArray([1, 1, 0, 1])); // Output: 3
console.log(longestSubArray([0, 1, 1, 1, 0, 1, 1, 0, 1])); // Output: 5
console.log(longestSubArray([1, 1, 1])); // Output: 2
console.log(longestSubArray([0, 1, 1, 0, 1])); // Output: 3
console.log(longestSubArray([0, 0, 0])); // Output: 0
console.log(longestSubArray([1, 1, 1, 1, 1])); // Output: 4
console.log(longestSubArray([1])); // Output: 0
console.log(longestSubArray([0])); // Output: 0