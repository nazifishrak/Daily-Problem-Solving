const {LinkedList, ListNode} = require('./linkedListBase');

let list1 = new LinkedList([1,2,3,4,5,6,7]);
list1.print();


function reverseLinkedList(head){
    let prev = null;
    let curr = head;
    let next = null;

    while(curr != null){
        next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

let reversedList = reverseLinkedList(list1.head);
reversedList.print();