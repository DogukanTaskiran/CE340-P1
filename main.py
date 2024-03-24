import RSA
import SDES

# RSA

publicKey, privateKey = RSA.keyGenerator()

message = "DENEME123!"
encryptedMessage = RSA.encrypt(publicKey, message)
print("Encrypted:", encryptedMessage)

decryptedMessage = RSA.decrypt(privateKey, encryptedMessage)
print("Decrypted:", decryptedMessage)

print()

# S-DES

    # Generate a random key
key = SDES.keyGenerator()
print("Generated Key:", key)

    # Message to encrypt
message = "Hello, World!"
print("Original Message:", message)

    # Convert message to binary
binary_message = SDES.stringToBinary(message)
print("Binary Message:", binary_message)

    # Encrypt the message
encrypted_message = SDES.encrypt(binary_message, key)
print("Encrypted Message:", encrypted_message)

    # Decrypt the message
decrypted_message = SDES.decrypt(encrypted_message, key)
print("Decrypted Message:", decrypted_message)

    # Convert decrypted binary message to string
decrypted_string = SDES.binaryToString(decrypted_message)
print("Decrypted String:", decrypted_string)
