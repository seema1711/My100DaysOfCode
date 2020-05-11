console.log('hello');
// alert('this is an emergency');

// Variables
var b = 'seema'
console.log(b);

var someNumber = 23;
console.log(someNumber);

// var age = prompt("what is your age?");
// document.getElementById('someText').innerHTML = age;

// Numbers in JS
var num1 = 5;
console.log(num1*10);
num1+=1;
console.log(num1);

// Divide, multiply, remainders
console.log(num1%2);

/* functions
1. Create a function
2. call a function
*/
function fun() {
  console.log('this is a function');
}
fun();

/* Create a function that takes a name and prompt hello followed by your name
For example:
Name: Seema
Return: Hello Seema
*/
function greeting(yourName) {
  var result = 'Hello ' + yourName;   // String Concatenation
  console.log(result);
}
var name = prompt('What is your name?');
greeting(name);

// Adding 2 numbers using function
function sumNumbers(a,b) {
  console.log(a+b);
}
sumNumbers(1,22);

// While loops
var num = 0;
while (num < 100) {
    num++;
    console.log(num);
}

// For loops
for (let i = 0; i < 100; i++) {
  console.log(i);
}

// Data types
let yourAge = 18; // number
let yourName = 'bob'; //string
let name2 = {first: 'Jane',last: 'Austin'}; //object or dictionaries in Python
let truth = false; //boolean
let fruit = ['apple','mango','guava']; //array or list in Python
let random; //undefined
let nothing = null; //null value

// Strings in JS
let fruits = 'apple';
let moreFruits = 'banana\nmango';
console.log(moreFruits);

console.log(fruits.length);
console.log(fruits.indexOf('ap'));
console.log(fruits.slice(1,5));
console.log(fruits.replace('app',123));
console.log(fruits.toUpperCase());
console.log(fruits.toLowerCase());
console.log(fruits.charAt(1));
