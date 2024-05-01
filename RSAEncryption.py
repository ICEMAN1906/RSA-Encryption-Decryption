import encryption

"""
Author:Aaron Brown
4/20/2024
 Encrypt encrypted files
"""
def RSA_Encryption(mssg,public):
    """
        encrypts a message encrypted using the RSA algorithm
        parmaters mssg public
        returns:decrypted



        """

    n,e=public

    encrypted = []
    for x in mssg:
        encryptedch=pow(ord(x),e,n) #encrypt the ASCII value of that letter using the RSA algorithm with
        encrypted.append(encryptedch)

    return encrypted


hex_n=input("enter n in hexadecimal")
hex_e=input("enter e in hexadecimal")
mssg=input("enter a string of 2 to 5 letters: ")
e=int(hex_e,16)#convert decimal
n=int(hex_n,16)
public_key=(n,e)

encrypted=RSA_Encryption(mssg,public_key)

print(encrypted)












