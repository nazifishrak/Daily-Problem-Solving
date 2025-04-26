/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {

    dic={}

    for (let x=0; x<nums.length; x++){
        let need=target-nums[x]
        if (need in dic) {
            return [dic[need], x];
        } else{
            dic[nums[x]]=x
        }
    }




    
};