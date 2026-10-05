import matplotlib.pyplot as plt

# Monthly sales data
months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

sales = [
    45000, 52000, 48000, 61000, 58000, 65000,
    62000, 70000, 68000, 75000, 72000, 80000
]

# Find highest and lowest sales
highest_sales = max(sales)
lowest_sales = min(sales)

highest_month = months[sales.index(highest_sales)]
lowest_month = months[sales.index(lowest_sales)]

# Display results
print("Highest Sales:")
print(highest_month, "₹", highest_sales)

print("\nLowest Sales:")
print(lowest_month, "₹", lowest_sales)

# Create charts
plt.figure(figsize=(12, 5))

# Line chart
plt.subplot(1, 2, 1)
plt.plot(months, sales, marker='o', color='blue')
plt.title("Monthly Sales Revenue - Line Chart")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.grid(True)

# Bar chart
plt.subplot(1, 2, 2)
plt.bar(months, sales, color='green')
plt.title("Monthly Sales Revenue - Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")

plt.tight_layout()
plt.show()
