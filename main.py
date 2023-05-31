import RSA_AlexVersion

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bit_length = int(input("Enter bit length for key: "))
    publicKey, privateKey = RSA_AlexVersion.generatePublicAndPrivateKeys(2**bit_length)
    normalMessage = input("Enter your message: ")
    encryptedMessage = RSA_AlexVersion.RSAEncryptPadding(normalMessage, publicKey)
    print(encryptedMessage)
    print(RSA_AlexVersion.RSADecryptPadding(encryptedMessage, privateKey).decode())
