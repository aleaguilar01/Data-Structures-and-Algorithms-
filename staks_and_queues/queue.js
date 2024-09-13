class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor () {
    this.first = null;
    this.last = null;
    this.size = 0;
  }

  enqueue(val){
    const newNode = new Node(val)
    if(this.size === 0) {
      this.first = newNode;
      this.last = newNode;
    } else {
      this.last.next = newNode;
      this.last = newNode;
    }
    this.size++;
    return this;
  }

  dequeue(){
    if(this.lenght === 0) return undefined
    const removedNode = this.first
    if(this.lenght === 1) {
      this.first = null;
      this.last = null;
    } else {
      this.first = this.first.next;
      removedNode.next = null;
    }
    this.size--;
    return removedNode;
  }

}