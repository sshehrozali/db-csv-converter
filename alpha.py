# Function to check for valid text
def test_alpha(input_alpha):

    # Iterate through each character of string
    for i in range(len(input_alpha)):
        
        # Return False, if error found
        if input_alpha[i].isdigit() == True:
            return False

        # Return False, if error found
        if input_alpha[i] == '-':
            return False

    # Return True, if no error found
    return True
