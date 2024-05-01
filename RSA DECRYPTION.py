import RSAEncryption
import encryption
"""
Author:Aaron Brown
4/20/2024
 Decrypt encrypted files
"""
def RSA_Decryption(mssg,private):
    """
    decrypts a message encrypted using the RSA algorithm
    parmaters mssg private
    returns:decrypted



    """

    n,d=private
    decrypted = []
    for x in mssg:
        encryptedch=chr(pow(x,d,n)) #decrypt the ASCII value of that letter using inverse
        decrypted.append(encryptedch)

    return decrypted


hex_n=input("enter n in hexadecimal")
hex_d=input("enter d in hexadecimal")
mssg=input("enter a string of 2 to 5 letters: ")
d=int(hex_d,16)#convert decimal
n=int(hex_n,16)
private=(n,d)

encrypted=RSAEncryption.RSA_Encryption(mssg,private)

decrypted=RSA_Decryption(encrypted,private)
print(str(decrypted))


