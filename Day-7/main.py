#with open("my_file.txt","r") as f:
#    lines = f.read()

#    print(lines)

# to read the contents already mentioned in file!!!!

with open("my_file.txt", "w") as file:      # We can use "a" to use append,, in this, already written content in
    # file don't get deleted
    file.write("Kaise ho thik ho??")

    # if the file doesn't exist previously then you can get it created automatically when we use w or a {not in "r"}

