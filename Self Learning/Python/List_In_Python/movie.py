# Temperature Monitoring System
temperatures = [32, 35, 40, 42, 46, 38, 30, 48, 41, 36]
# 1. Find hottest and coldest day
hottest = max(temperatures)
coldest = min(temperatures)
print("Hottest Temperature:", hottest, "°C")
print("Coldest Temperature:", coldest, "°C")
# 2. Replace temperatures above 45°C with "Heat Alert"
for i in range(len(temperatures)):
    if temperatures[i] > 45:
        temperatures[i] = "Heat Alert"
print("Updated Temperatures:", temperatures)
# 3. Count number of extreme days (> 40°C)
extreme_days = 0
for t in temperatures:
    if t != "Heat Alert" and t > 40:
        extreme_days += 1
print("Number of extreme days (> 40°C):", extreme_days)