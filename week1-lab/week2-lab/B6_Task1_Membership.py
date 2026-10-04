# B6_Task1_Membership.py
# Lab Task B6: Membership Operators

fruits = ["apple", "banana", "cherry", "orange", "grape"]

fruit_to_check = input("Enter a fruit name to check: ")

# Normalize the input to lowercase to handle uppercase inputs sensibly
normalized_fruit = fruit_to_check.lower()

print(f"Is '{fruit_to_check}' in the list?", normalized_fruit in fruits)
print(f"Is '{fruit_to_check}' not in the list?", normalized_fruit not in fruits)
