import bcrypt

# The plain-text password you want to secure
password = "password123"

# Generate a salt with a cost factor of 10
# This matches the '$10$' difficulty multiplier from your original hash
salt = bcrypt.gensalt(rounds=10)

# Hash the password
# Both inputs must be encoded as bytes
hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

# Convert the byte string back to a regular string for database storage
hash_to_store = hashed_password.decode('utf-8')

print(f"Generated Hash: {hash_to_store}")