name = "Sharath"
target_role = "AI-Engineer"
daily_learning_hours = 2 

print(name)
print(target_role)
print(daily_learning_hours)

product = "Laptop"
quantity = 10
price = 45000.75
is_available = True

print(type(product))
print(type(quantity))
print(type(price))
print(type(is_available))

price = 500
quantity = 3
total = price * quantity
print(total)

sales = 1200
expenses = 450
profit = sales - expenses
print(profit)

total_marks = 425
subjects = 5
average = total_marks / subjects
print(average)

print(17 % 5)
total_revenue = 17 * 50
daily_average = total_revenue / 5

print(total_revenue)
print(daily_average)

name = "Sharath"
hours = 2

print(f"My name is {name}")
print(f"I study Python for {hours} hours daily")
product = "Laptop"
price = 45000

print(f"The {product} costs ₹{price}")
name = input("Enter your name: ")
print(f"Welcome, {name}!")



price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity
print(f"Total amount : ${total}")
print(f"Product price: ${price}")
print(f"Total amount: ${total:.2f}")

discount = float(input("Enter the discount: "))
if discount < 0 or discount > 100:
    print("Invalid discount percent")
else: 
    final_amount = total - (total * discount/100)
    print(f"Discount: {discount}%")
    print(f"Final amount: ${final_amount:.2f}")

