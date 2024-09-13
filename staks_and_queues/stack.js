class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Stack {
  constructor(){
    this.first = null;
    this.last = null;
    this.size = 0;
  }

  push(value) {
    let node = new Node(value);
    if (this.size === 0) {
      this.first = node;
      this.last = node;
    } else {
      let previousFirst = this.first;
      this.first = node;
      this.first.next = previousFirst;
    }
    this.size++;
    return this.size;
  }

  pop(){
    if(this.size === 0) return null;
    if (this.size === 1) {
      this.first = null;
      this.last = null;
    } else {
      const removedNode = this.first;
      this.first = this.first.next;
      removedNode.next = null;      
    }
    this.size--;
    return removedNode;
  }

}