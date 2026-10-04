# Challenge_Login_Validator.py
# Lab Task: Challenge - Login Validator

# Predefined username and password
correct_username = "adminUser"
correct_password = "SecretPassword123"

print("--- Login System ---")
# Prompt user for input
input_username = input("Enter username: ")
input_password = input("Enter password: ")

# Check both credentials using comparison (==) and logical (and) operators
login_success = (input_username == correct_username) and (input_password == correct_password)

# Print final result
print("\nLogin Successful:", login_success)
