function maxArea(heights) {
    let maxArea = 0;
    for (let p1 = 0; p1 < heights.length; p1++) {
        for (let p2 = p1 + 1; p2 < heights.length; p2++) {
            let length = Math.min(heights[p1], heights[p2]);
            let width = p2 - p1;
            let area = length * width;
            maxArea = Math.max(maxArea, area);
        }
    }
    return maxArea;
}

// Testing the function
console.log(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])); // Expected output: 49

function maxAreaOptimised(heights){
    let maxArea = 0;
    let p1 = 0
    let p2 = heights.length -1

    while (p1<p2){
        let length = Math.min(heights[p1], heights[p2])
        let width = p2 - p1
        area = length * width
        maxArea = Math.max(area,maxArea)

        if (heights[p1]< heights[p2]){
            p1++
        } else {
            p2--
        }
    }

    return maxArea
}

console.log(maxAreaOptimised([1, 8, 6, 2, 5, 4, 8, 3, 7])); // Expected output: 49