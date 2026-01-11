class Queue {
    constructor() {
        this.elements = {};
        this.head = 0;
        this.tail = 0;
    }
    enqueue(element) {
        this.elements[this.tail] = element;
        this.tail++;
    }
    dequeue() {
        const item = this.elements[this.head];
        delete this.elements[this.head];
        this.head++;
        return item;
    }
    peek() {
        return this.elements[this.head];
    }
    get length() {
        return this.tail - this.head;
    }
    get isEmpty() {
        return this.length === 0;
    }
}

let q = new Queue();

for (let i = 1; i <= 7; i++) {
    q.enqueue(i);
    // q.dequeue(i);
    console.log(q)
    let headValue = q.head;

    // q.dequeue(i);

    console.log("er", headValue, "fghjk")

}
let len = q.tail - q.head

for (let i = 1; i <= len; i++) {
    q.dequeue(i);
    console.log("Ewrtdyfff", q)

}

console.log("hiii"); // 1
