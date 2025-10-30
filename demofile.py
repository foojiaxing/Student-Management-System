import os
f = open("demofile.txt", "r")
print(f.read())

# Close Files
f = open("demofile.txt", "r")
f.write("Now the file has content")
f.close()

# Check if the file exist
import os
if