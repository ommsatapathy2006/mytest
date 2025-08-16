class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        self.result = a * b
        return self.result

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        self.result = a / b
        return self.result

def main():
    calc = Calculator()
    print("Simple Calculator using OOP")
    print("Operations: add, subtract, multiply, divide, quit")

    while True:
        operation = input("\nEnter operation: ").lower()
        if operation == "quit":
            print("Exiting calculator.")
            break
        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            print("Invalid operation. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if operation == 'add':
            print("Result:", calc.add(num1, num2))
        elif operation == 'subtract':
            print("Result:", calc.subtract(num1, num2))
        elif operation == 'multiply':
            print("Result:", calc.multiply(num1, num2))
        elif operation == 'divide':
            print("Result:", calc.divide(num1, num2))

if __name__ == "__main__":
    main()
