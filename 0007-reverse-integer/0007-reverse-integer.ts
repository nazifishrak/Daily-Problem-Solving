function reverse(x: number): number {

    // 1 2 3 --> 3 2 1
    let output =0
    let sign=Math.sign(x)
    x=Math.abs(x)
    let inp=x
    while (inp/10 !=0){
        output=(output*10)+(inp%10)
        inp=Math.floor(inp/10)
    }
    let ans= output*sign
    if((ans >= -(2**31)) && (ans<=2**31-1)){
        return ans;
    } else {
        return 0;
    }
    


};

