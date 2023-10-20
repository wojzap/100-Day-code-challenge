with open("../../../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)


with open("C:/Users/Dragon/Desktop/new_file.txt", mode="w") as file:
    file.write("new")