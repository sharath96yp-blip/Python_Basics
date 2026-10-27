for i in range(5):
    print ("Welcomback")

for i in range(3):
    print(i)

for i in range(1,6):
    print(i)

for i in range(1,6):
    print(f"{i}*2 = {i*2}")

sales = [1200, 1500, 900, 2000, 1750]
total_sales = 0
for amount in sales:
    total_sales = total_sales + amount
print(f"Total Sales: ${total_sales}")
avg_sales = total_sales / len(sales)
print(f"AVG Sales: ${avg_sales}")
print(f"AVG Sales: ${avg_sales:.2f}")

higest_sales = max(sales)
print(f"Higest Sales: {higest_sales}")

lowest_sales = min(sales)
print(f"Lowest Sales: {lowest_sales}")

count = 0
for amount in sales:
    if amount>1500:
        count = count+1
print(f"Number of sales more than 1500: {count}")

count = 0
for amount in sales:
    if amount>=1500:
        count = count+1
print(f"Number of sales more than 1500: {count}")

count = 0
for amount in sales:
    if amount<1500:
        count = count+1
print(f"Number of sales more than 1500: {count}")

low_sales = []
for amount in sales:
    if amount<1500:
        low_sales.append(amount)

print(f"Low sales: {low_sales}")

low_sales_total = sum(low_sales)
print(f"Total low sales: ₹{low_sales_total}")

low_sales_avg = sum(low_sales) / len(low_sales)
print(f"Average Low Sales: {low_sales_avg}")
print(f"Average Low Sales: {low_sales_avg:.2f}")

count = 0
for amount in sales:
    if amount >=1200:
        count = count+1
print(f'Number of qualifying sales: {count}')

count = 0
for amount in sales:
    if amount >=1200:
        count +=1
print(f'Number of qualifying sales: {count}')

high_sales_total = 0
for amount in sales:
    if amount > 1500:
        high_sales_total += amount
print(f'Total high sales: {high_sales_total}')