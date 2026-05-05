# Inventory Management System
stock = [0, 5, 12, 0, 8, 25, 3, 15]
# 1. Remove items with 0 stock
available_stock = []
for item in stock:
    if item != 0:
        available_stock.append(item)
print("Available Stock:", available_stock)
# 2. Add restock of 50 units to items below 10
for i in range(len(available_stock)):
    if available_stock[i] < 10:
        available_stock[i] = available_stock[i] + 50
print("Stock after Restocking:", available_stock)
# 3. Find total inventory count
total_inventory = sum(available_stock)
print("Total Inventory Count:", total_inventory)