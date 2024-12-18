def input_validation(inputChoice):
    try:
        # type casting input choice to integer
        inputChoice = int(inputChoice)
        # check if the input is between 1 and 4
        if 1 <= inputChoice <= 4:
            return inputChoice
        else:
            print("Invalid option! Please choose a valid option (1-4).")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
    return None
