
#Variable assignment and printing
age=22;
height = 5.9;
name = "John Doe";  
is_student = True;
print("Name:", name);
print("Age:", age);
print("Height:", height);
print("Is Student:", is_student);

#simple calculatopr program
a =(input("Enter first number: "));
b =(input("Enter second number: "));

print("Choose operator:")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")
print("Enter operator (+, -, *, /): ");
operator = input();
a = float(a);
b = float(b);
if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operation")
    
#concatenating user input with strings
name=input("Enter your Name:");
print("Welcome",name,"!");

#Using f-strings for formatted output
name="raksha";
age=21;
print(f"My Name is {name}, I am Age {age}");


