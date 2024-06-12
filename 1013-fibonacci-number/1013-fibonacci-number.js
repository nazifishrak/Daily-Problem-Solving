/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    let memo = {};
    
    function fibHelper(n) {
        if (n <= 0) return 0; // Base case for non-positive integers
        if (n === 1 || n === 2) return 1;
        if (memo[n]) return memo[n];
        
        memo[n] = fibHelper(n - 1) + fibHelper(n - 2);
        return memo[n];
    }
    
    return fibHelper(n);
};
