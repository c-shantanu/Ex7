#PEP8 
# Python program to accept a filename from the user and print the extension

file_name = input("Please enter file name: ") 
file_extension = file_name.split("." ) # Splitting to get extension
print(file_extension[-1]) # Printing  extension of file 
