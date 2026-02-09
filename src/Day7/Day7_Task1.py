name=input("Enter your name: ")
goal=input("Enter your daily goal: ")
with open("daily_goals.txt", "a") as file:
    file.write(f"Name: {name}, Goal: {goal}\n")
    print("Daily goal saved successfully.")