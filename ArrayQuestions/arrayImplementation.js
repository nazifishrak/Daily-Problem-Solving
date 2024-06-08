class MyArray {
    constructor(){
        this.length = 0;
        this.data = {};
    }


    // {
    //     0: "A",
    //     1: "B"
    // }

    get(index){
        console.log(this.data[index])
        return this.data[index]

    }

    push(item){
        this.data[this.length]= item
        this.length++
    }

    pop(){
        if (this.length === 0) return undefined;
        let last_item = this.data[this.length-1]
        delete this.data[this.length-1];
        this.length--
        return last_item
    }

    print(){
        for (let i =0; i<this.length; i++){
            console.log(`${i}:${this.data[i]}`)
        }
    }

    remove(index){
        let removed_item = this.data[index]
        for(let i = index; i< this.length; i++){
            this.data[i]= this.data[i+1]
        }
        delete this.data[this.length-1]
        this.length--
        return removed_item

    }
}

arr = new MyArray()
arr.push("A")
arr.push("B")
arr.push("C")
arr.push("D")
arr.push("E")
arr.push("F")
arr.print()
const popped = arr.pop()
console.log(`Popped item is :   ${popped}`)


arr.print()
arr.get(4)
arr.remove(3)
arr.print()
