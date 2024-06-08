class ListNode {
    constructor(val) {
        this.value = val;
        this.next = null;
    }
}

class LinkedList {
    constructor(arr) {
        if (arr.length === 0) {
            this.head = null;
            return;
        }

        this.head = new ListNode(arr[0]);
        let current = this.head;

        for (let i = 1; i < arr.length; i++) {
            current.next = new ListNode(arr[i]);
            current = current.next;
        }
    }

    print() {
        let curr = this.head;
        while (curr != null) {
            console.log(curr.value);
            curr = curr.next;
        }
    }
}

let list1 = new LinkedList([1,2,3,4,5,6,7]);
list1.print();
