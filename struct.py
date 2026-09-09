import struct

# Create data
name = b"John"
age = 20

# Pack data into binary format
data = struct.pack("4sI", name, age)

print("Packed data:", data)

# Unpack the data
name, age = struct.unpack("4sI", data)

print("Name:", name.decode())
print("Age:", age)
