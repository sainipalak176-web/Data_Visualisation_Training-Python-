set1={45,67,89,34,78}
print("first set:",set1)
#--------------------------------
print("------------------------")
set2={23,56,89,90,34}
print("second set:",set2)
#--------------------------------
print("--------------------------")
#union operation on sets 
set3=set1.union(set2)
print("union of set1 and set2 is:",set3)

#output
#first set: {34, 67, 89, 45, 78}
#------------------------
#second set: {34, 23, 56, 89, 90}
#--------------------------
#union of set1 and set2 is: {34, 67, 45, 78, 23, 56, 89, 90}