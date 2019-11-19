'''
This program shifts letters in an alphabet using the Caesar shift
--Program written by Son Nguyen
'''

#Prompt the user for the key and the text
key = int(input("How much do you wish to shift by?: "))
plainText = input("Plaintext: ")

#Define the alphabet and its length as constants
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_LENGTH = len(ALPHABET)

#Define the length of the text and initialize the cipherText
textLength = len(plainText)
cipherText = ""

#Loop i through each letter of the text
for i in range(textLength):
    #Check if the text is just a whitespace, then add the space
    if plainText[i] == " ":
        cipherText = cipherText + " " 

    #Loop through the alphabet if it's a letter and shift through the alphabet
    else: 
        for j in range(ALPHABET_LENGTH):
            if plainText[i] == ALPHABET[j]:
                n = j + key - 26
                cipherText = cipherText + ALPHABET[n]
            elif plainText[i] == ALPHABET[j].upper():
                n = j + key - 26
                cipherText = cipherText + ALPHABET[n].upper()

#Display the plain text and the encoded text
print("Plaintext: " + plainText)
print("Ciphertext: " + cipherText)


