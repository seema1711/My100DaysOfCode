let fruits = ['apple','banana','mango','orange'];
let fruits2 = new Array('apple','banana','mango','orange');
console.log(fruits+fruits2);

fruits[0] = 'strawberry';

for (var i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}

// Array common methods
console.log(fruits.toString());                  // toString
console.log(fruits.join('-'));                  //join()
console.log(fruits,fruits.pop(),fruits);        // pop()
console.log(fruits.push('berries'),fruits);     //push()
fruits[4] = 'new fruit';
console.log(fruits);
fruits.shift(); //removes first element from a list
console.log(fruits);

fruits.unshift('kiwi'); //add element to an Array
console.log(fruits);
let veggies = ['potato','brinjal','bitter gourd'];
let allGroceries = fruits.concat(veggies);
console.log(allGroceries);
console.log(allGroceries.slice(1,4));
console.log(allGroceries.reverse());

let someNumbers = [2,5,6,324,26,545,32,6]
console.log(someNumbers.sort());
