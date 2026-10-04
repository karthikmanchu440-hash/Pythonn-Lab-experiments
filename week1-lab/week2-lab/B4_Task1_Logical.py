# B4_Task1_Logical.py
# Lab Task B4: Logical Operators

percentage = float(input("Enter student's percentage: "))
attendance = float(input("Enter student's attendance: "))

# A student qualifies only when percentage is above 75 AND attendance is above 90.
is_eligible = (percentage > 75) and (attendance > 90)

print("Is the student eligible?", is_eligible)
