import hashlib

password = input()  # Taking the password as input

# Encode the password string using UTF-8 before hashing
password_encoder = password.encode()

# Create a hash object and update it with the encoded password
hash_object = hashlib.sha256()
hash_object.update(password_encoder)

# Retrieve the hexadecimal digest of the hashed password
hashed_password = hash_object.hexdigest()

print(hashed_password)  # Print the hashed password
