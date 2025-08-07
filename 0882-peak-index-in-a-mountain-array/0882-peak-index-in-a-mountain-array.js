/**
 * @param {number[]} arr
 * @return {number}
 */
var peakIndexInMountainArray = function(arr) {
    
    // [0,10,5,2]
    // [0,1,0]

    let st =0, end = arr.length-1
    while (st<=end){
        let mid = Math.floor(st + (end-st)/2)
        // check if mid is the peak or not
        if (arr[mid]>arr[mid-1] && arr[mid]>arr[mid+1]) return mid
        // if the above isnt true
        // i wanna check where is the mid located, if on the
        //  increasing slope then the peak would be on the right,
        //  else it would be on the left
        
        // check if on the left slope
        if (arr[mid]>= arr[mid-1] && arr[mid]<= arr[mid+1]){
            st=mid+1
        } else{
            end=mid
        }

    }

};