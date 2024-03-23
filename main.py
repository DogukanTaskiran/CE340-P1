import RSA

public_key, private_key = RSA.keyGenerator()

message = "DENEME123!"
encryptedMessage = RSA.encrypt(public_key, message)
print("Encrypted:", encryptedMessage)

decryptedMessage = RSA.decrypt(private_key, encryptedMessage)
print("Decrypted:", decryptedMessage)