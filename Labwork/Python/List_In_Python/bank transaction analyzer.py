# Bank Transaction Analyzer
transactions = [15000, -5000, 20000, -12000, 8000, -3000, 25000]
# 1. Calculate total balance
total_balance = sum(transactions)
print("Total Balance:", total_balance)
# 2. Find largest withdrawal
withdrawals = []
for t in transactions:
    if t < 0:
        withdrawals.append(t)
largest_withdrawal = min(withdrawals)
print("Largest Withdrawal:", largest_withdrawal)
# 3. Count number of deposits greater than ₹10,000
deposit_count = 0
for t in transactions:
    if t > 10000:
        deposit_count += 1
print("Deposits greater than ₹10,000:", deposit_count)