data = data2 = "";

# Getting the file names
file1 = input("File 1 name: ")
file2 = input("File 2 name: ")
file3 = input("File name to create: ")

# Reading data from file1
with open(file1) as fp:
	data = fp.read()

# Reading data from file2
with open(file2) as fp:
	data2 = fp.read()

# Merging 2 files
# To add the data of file2
# from next line
data += "\n"
data += data2

with open (file3, 'w') as fp:
	fp.write(data)
