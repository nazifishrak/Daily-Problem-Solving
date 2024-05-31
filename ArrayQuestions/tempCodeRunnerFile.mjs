import { ProblemBuilder } from "../ProblemBuilder.mjs";

const findMaxSumSubArray = new ProblemBuilder(
    "Find the Maximum Sum Subarray",
    "Medium",
    "Given an array of integers, find the contiguous subarray with the largest sum."
)

const solution = (arr,k)=>{
    let p1=0, p2=k;
    let maxSum =0;
    let currSum = 0;
    for (p1; p1<k; p1++){
        maxSum +=arr[p1]
        currSum = maxSum
    }
    p1 = 0
    while (p2<arr.length){
        
        currSum = currSum+arr[p2]-arr[p1]
        if (currSum>maxSum){
            maxSum = currSum
            p1++
            p2++
        } else{
            p1++
            p2++
        }
    }
    return maxSum


}

findMaxSumSubArray.setSolution(solution)

findMaxSumSubArray.printSolution([1, 2, 3, 4, 5, 6, 7, 8, 9],3)

