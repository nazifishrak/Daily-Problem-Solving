/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
function isAlphanumeric(str) {
  return /^[a-zA-Z0-9]+$/.test(str);
}
    let st =''
    for(let i=0; i<s.length;i++){
        if(isAlphanumeric(s[i])) st+=s[i].toLowerCase()
    }
    for(let i=0,j=st.length-1; i<=j;i++, j--){
        if (st[i]!=st[j]) return false
    }
    return true
    
};