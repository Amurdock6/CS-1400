# ALEXANDER MURDOCK 
# CS-1400-002

print("Is it food [y/n]?")
food = input()

# Handles the "is it food?" part of the flow chart
if food == "Y" or food == "y" or food == "yes" or food == "Yes":
    print("From a Can [y/n]?")
    can = input()
    # Handles the "From a can" part of the flow chart
    if can == "Y" or can == "y" or can == "yes" or can == "Yes":
        print("Eat half.")
    elif can == "N" or can == "n" or can == "no" or can == "No":
        print("Ignore it.")

elif food == "N" or food == "n" or food == "no" or food == "No":
    print("Is it a cat tree [y/n]?")
    catTree = input()

    # Handles the "Is it a cat tree?" part of the flowchart
    if catTree == "Yes" or catTree == "yes" or catTree == "Y" or catTree == "y":
        print("Did it come in a box [y/n]?")
        box = input()
        if box == "Yes" or box == "yes" or box == "Y" or box == "y":
            print("Sit in the box.")
        elif box == "No" or box == "no" or box == "N" or box == "n":
            print("Ignore it.")
    # Handles the "is it a human" section of flow chart
    elif catTree == "No" or catTree == "no" or catTree == "N" or catTree == "n":
        print("Is it a human [y/n]?")
        human = input()
        # Handles the does it want to pet me part of flow chart
        if human == "Yes" or human == "yes" or human == "Y" or human == "y":
            print("Does it want to pet me [y/n]?")
            pet = input()
            # handles the does it want to pet me part of the flow chart
            if pet == "Y" or pet == "y" or pet == "Yes" or pet == "yes":
                print("Cough up a hairball.")
            elif pet == "No" or pet == "no" or pet == "N" or pet == "n":
                print("Jump in its lap.")
        elif human == "No" or human == "n" or human == "N" or human == "n":
            print("Is it a laptop [y/n]?")
            laptop = input()
            # Handles the is it a laptop part of flow chart
            if laptop == "Y" or laptop == "y" or laptop == "Yes" or laptop == "yes":
                print("In use [y/n]?")
                inUse = input()
                # Handles the in use section of flow chart
                if inUse == "Y" or inUse == "y" or inUse == "Yes" or inUse == "yes":
                    print("Lay on keyboard.")
                elif inUse == "N" or inUse == "n" or inUse == "No" or inUse == "no":
                    print("Knock it off the table.")
            #  if it's not a laptop then we will get the else output below
            elif laptop == "N" or laptop == "n" or laptop == "No" or laptop == "no": 
                print("Sleep.")
