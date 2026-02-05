#Dictionary
dict={"name":"raksha","age":22,"city":"Mangalore"};
print(dict);

student={
    "name":"raksha",
    "age":22,
    "course":"Data Science"
}
print(student["name"])
student["age"]=22
student["city"]="Mangalore"
print(student)

marks={"Maths":85,"Science":90,"English":80};
print(marks.get("Maths"))
print(marks.get("History",0))
for subject, score in marks.items():
    print(subject, score)
    marks.update({"Maths":88})
print(marks)
marks.pop("English")
print(marks)


#loop through dictionary
purchase={
    "Alice":250,
    "Bob":150,
    "Charlie":300
}
for name, amount in purchase.items():
    print(f"{name} made a purchase of ${amount}")
    
    #Taking user input to create a dictionary
n=int(input("Enter number of customers:"))
user_purchases={}
for i in range(n):
    name=input("Enter customer name:")
    amount=int(input(f"Enter purchase amount for {name}:"))
    user_purchases[name]=amount
    print("Customer Purchases Data:", user_purchases)
    top_customer=max(user_purchases, key=user_purchases.get)
    print(f"Top Customer: {top_customer} with purchase amount ${user_purchases[top_customer]}")
    top_customer=min(user_purchases, key=user_purchases.get)
    print(f"Lowest Customer: {top_customer} with purchase amount ${user_purchases[top_customer]}")
    
    #sets
    A={1,2,3}
    B={3,4,5}
    print(A&B) #intersection
    print(A|B) #union
    print(3 in A)
    print(2 in B)