count = 1
while count <= 5:
    print(count)
    count +=1

count = 1
while count <= 3:
    print(count)
    count +=1

count = 5
while count >=1:
    print(count)
    count -=1
print("Countdone Complete!")

count = 1
while count<=10:
    if count ==4:
        break

    print(count)
    count +=1

print("Loop Stops!")

count = 0
while count < 5:
    count+=1
    if count ==3:
        continue

    print(count )

sales = [1200, 1500, 900, 2000, 1750]

for amount in sales:
    if amount < 1000:
        continue
    print(amount)

count = 0
for amount in sales:
    if amount<1000:
        continue
    count +=1
print(f"Number of qualifying sales: {count}")

total = 0
for amount in sales:
    if amount<1000:
        continue
    total += amount
print(f"Total qualifying sales: {total}")

for amount in sales:
    if amount>=1500:
        print(f"{amount}: Highest Sales")
    else:
        print(f"{amount}: Lowest Sales")

high_count = 0
low_count = 0
for amount in sales:
    if amount>=1500:
        high_count += 1
    else:
        low_count +=1
print(f"Highest Sales: {high_count}")
print(f"Lowest Sales: {low_count}")


high_count = 0
low_count = 0
high_total = 0
low_total = 0

for amount in sales:
    if amount>=1500:
        high_count +=1
        high_total += amount
    else:
        low_count +=1
        low_total += amount
print(f"High Sales count: {high_count}")
print(f"Low Sales count: {low_count}")
print(f"Highest Sales Total: {high_total}")
print(f"Low Sales count: {low_total}")

overall_sales = high_total + low_total
print(f"Over all Total sales: {overall_sales}")