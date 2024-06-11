// A conveyor belt has packages that must be shipped from one port to another within days days.

// The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

// Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.


/**
 * @param {number[]} weights
 * @param {number} days
 * @return {number}
 */
var shipWithinDays = function(weights, days) {
    // [5,6,7,8]
    // cap 8
        function get_days(capacity){
            let days = 1;
            let curr_cap = capacity
            let i =0
            while(i<weights.length && curr_cap>=weights[i]){
                curr_cap-=weights[i]
                i++
                if (curr_cap<weights[i]) {
                    days++
                    curr_cap=capacity
                }
                }
            return days
            }
    
            const min_cap = Math.max(...weights)
            const max_cap = weights.reduce((acc,curr)=> acc+curr) //foldr kinda from cpsc 110
    
            for (let c = min_cap; c<=max_cap; c++){
                if (get_days(c)<=days) return c;
            }
       
    };

console.log(shipWithinDays([1,2,3,4,5,6,7,8,9,10],5))

