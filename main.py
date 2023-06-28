Certainly! Here's an example of a Python script that checks if a number is prime:

```python
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
```

And here's an example of JavaScript code that checks if a number is prime:

```javascript
function isPrime(number) {
    if (number <= 1) {
        return false;
    }
    for (let i = 2; i <= Math.sqrt(number); i++) {
        if (number % i === 0) {
            return false;
        }
    }
    return true;
}

let number = parseInt(prompt("Enter a number: "));
if (isPrime(number)) {
    console.log(number + " is a prime number.");
} else {
    console.log(number + " is not a prime number.");
}
```

Both examples prompt the user to enter a number, check if the number is prime using a function, and then display the result.
