#validate username and password.

# List of username-password pairs to test
credentials = [
    ('user1', 'pass123'),
    ('admin', 'admin123'),
    ('guest', 'guest'),
    ('test', '12345')
]

# Valid credentials (example)
valid_username = 'admin'
valid_password = 'admin123'

for username, password in credentials:
    if username == valid_username and password == valid_password:
        print(f"Problem 16 - Username: {username}, Password: {password} -> Valid Login")
    else:
        print(f"Problem 16 - Username: {username}, Password: {password} -> Invalid Login")

# Output inside code:
# Problem 16 - Username: user1, Password: pass123 -> Invalid Login
# Problem 16 - Username: admin, Password: admin123 -> Valid Login
# Problem 16 - Username: guest, Password: guest -> Invalid Login
# Problem 16 - Username: test, Password: 12345 -> Invalid Login