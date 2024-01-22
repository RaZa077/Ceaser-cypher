
#A Caesar Cipher program
def welcome():
    '''this function welcomes the user'''
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text using Caesar Cipher.")

def enter_message():
    '''this function prompts user to enter a message and whether to encrypt or decrypt and its shift '''
    valid_modes = {'e', 'd'}
    mode = input("Would you like to encrypt (e) or decrypt (d)? : ").lower()
    
    while mode not in valid_modes:
        #checking the input and prompting user to input a valid mode until it is e or d 
        print("Invalid Mode")
        mode = input("Would you like to encrypt (e) or decrypt (d)?: ").lower()

    if mode == "e":
        message = input("What message would you like to encrypt:").upper()
    if mode == 'd':
        message = input("What message would you like to decrypt:").upper()

    shift = input("What is the shift number: ")
    while not shift.isdigit() or not (1 <= int(shift) <= 25):
        print("Invalid Shift")
        shift = input("What is the shift number: ")

    return mode, message.upper(), int(shift)

def encrypt(message, shift):
    '''this function encrypts a message'''
    encrypted = ""
    for char in message.upper():
        if char.isalpha():
            shiftvalue = ord(char) + int(shift)
            if shiftvalue > ord('Z'):
                    shiftvalue -= 26
            elif shiftvalue < ord('A'):
                    shiftvalue += 26
            encrypted += chr(shiftvalue)
        else:
            encrypted += char
    return encrypted

def decrypt(message, shift):
    '''this function decrypts a message'''
    return encrypt(message, -shift)

def process_file(filename, mode,shift):
    """This function encrypts or decrypts messages from a given file """
    messages = []
    #Open the specified file in read ('r') mode using a with statement
    with open(filename, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Remove leading and trailing whitespaces from the line and store it as 'message'
            message = line.strip()
            # Check the specified mode for either encryption ('e') or decryption ('d')
            if mode == 'e':
                # If encrypting, convert the message to uppercase and append the encrypted message to the list
                messages.append(encrypt(message.upper(), shift))
            elif mode == 'd':
                # If decrypting, convert the message to uppercase and append the decrypted message to the list
                messages.append(decrypt(message.upper(), int(shift)))
    return messages

def is_file(filename):
    """This function checks whether the file exists or not """
    try:
        with open(filename, 'r'):
            pass
        return True
    except FileNotFoundError:
        return False

def write_messages(messages):
    """This Function takes a single parameter with a list of strings and it writes the output in results.txt"""
    # Open 'results.txt' in write ('w') mode using a with statement
    with open("results.txt", "w") as file:
        # Iterate through each message in the list
        for message in messages:
            # Write the message followed by a newline character to the file
            file.write(message + "\n")
    print("Output written to 'results.txt' successfully.")

def message_or_file():
    """This Function doesnt take any parameters, but returns three values, the mode ("e" or "d" based on whether the user would like to encrypt or decrypt), a message if the user would like to process messages using the console (or None) and a filename if the user would like to process data in a file (or None). """
    valid_modes = {'e', 'd'}
    mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()

    while mode not in valid_modes:
        #asking user to input a valid mode until the 
        print("Invalid Mode")
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()

    source = input("Would you like to read from a file (f) or the console (c)?: ").lower()
    
    while source not in ("c","f"):
        print("Invalid Source")
        source = input("Would you like to read from a file (f) or the console (c)?: ").lower()

    if source == 'c':
        if mode == "e":
            message = input("What message would you like to encrypt: ").upper()
        elif mode =="d":
            message = input("What message would you like to decrypt: ").upper()
        return mode, message, None
    elif source == 'f':
        filename = input("Enter a filename: ")
        while True:
            check_file = is_file(filename)
            if check_file == True:
                return mode, None, filename
            print ("Invalid Filename")
            filename = input("Enter a filename: ")

def main():
    """This function encrypts and decrypts text using the Caesar Cipher. either it is from a file or a console """
    welcome()
    while True:
        mode, message, filename = message_or_file()
        shift = input("What is the shift number: ")
        while not shift.isdigit() or not (1 <= int(shift) <= 25):
            #asking user to input a valid shift until the shift is digit or the shift value is more than 1 and less than 25
            print("Invalid Shift")
            shift = input("What is the shift number: ")

        if filename:
            messages = process_file(filename,mode,shift)
            write_messages(messages)
        else:
            if mode == 'e':
                encrypted_message = encrypt(message, int(shift))
                print(f"\nEncrypted Message: {encrypted_message}")
            elif mode == 'd':
                decrypted_message = decrypt(message, int(shift))
                print(f"\nDecrypted Message: {decrypted_message}")

        another_message = input("\nWould you like to encrypt or decrypt another message? (y/n): ").lower()
        while another_message not in ("y", "n"):
            print("Invalid input. Please enter 'y' or 'n'.")
            another_message = input("\nWould you like to encrypt or decrypt another message? (y/n): ").lower()

        if another_message == "n":
            print("Thanks for using the program, goodbye!")
            break
        elif another_message == "y":
            continue

main()
