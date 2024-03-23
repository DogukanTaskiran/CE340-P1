import RSA

publicKey, privateKey = RSA.keyGenerator()

message = "DENEME123!"
encryptedMessage = RSA.encrypt(publicKey, message)
print("Encrypted:", encryptedMessage)

decryptedMessage = RSA.decrypt(privateKey, encryptedMessage)
print("Decrypted:", decryptedMessage)