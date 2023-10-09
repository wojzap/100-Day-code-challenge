#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt", mode="r") as names:
    list_of_names = names.readlines()
    list_of_names_clean = []
    for name in list_of_names:
        clean_name = name.strip("\n")
        list_of_names_clean.append(clean_name)

with open("Input/Letters/starting_letter.txt", mode="r") as letter:
    letter_blueprint = letter.read()

for name in list_of_names_clean:
    personalized_letter = letter_blueprint.replace("[name]", f"{name}")
    with open(f"Output/ReadyToSend/letter_to_{name}.txt", mode="w") as final_letter:
        final_letter.write(personalized_letter)