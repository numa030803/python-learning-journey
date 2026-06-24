from sys import argv
from os.path import exists

#from_file = 'rest.txt' # I hardcoded the filename here!
#to_file = "new_rest.txt" # I hardcoded the filename here!

# Code without hardcoding
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

# In 1 line we can write the code like this 
# in_file = open(from_file, "r").read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close() # we close files to save the data properly to the disks and it also prevents file corruption
in_file.close()