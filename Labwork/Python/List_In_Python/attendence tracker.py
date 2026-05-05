# E-Commerce Cart System
cart_prices = [1200, 2500, 1200, 1800, 900, 2500]
# 1. Remove duplicate items
unique_prices = list(set(cart_prices))
print("Unique Cart Prices:", unique_prices)
# 2. Calculate total
total = sum(unique_prices)
print("Total Amount:", total)
# 3. Apply 10% discount if total > 5000
if total > 5000:
    discount = total * 0.10
else:
    discount = 0
amount_after_discount = total - discount
print("Discount Applied:", discount)
# 4. Add 18% GST
gst = amount_after_discount * 0.18
final_amount = amount_after_discount + gst
print("GST (18%):", gst)
print("Final Payable Amount:", final_amount)