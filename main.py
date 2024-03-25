import RSA
import SDES
import AliceBob
import time

# Requirement 6
# RSA part

print("RSA PART")

# Requirement 4.a and 4.b
for i in range (0,10):
    
    RSATotalTime = 0
    KeyTotalTime = 0
    encryptionTotalTime = 0
    decryptionTotalTime = 0
    
    # Requirement 1 RSA Key Generation
    keyStartTime = time.perf_counter() # Start time
    publicKey, privateKey = RSA.keyGenerator()
    keyEndTime = time.perf_counter() # End time
    KeyTotalTime = keyEndTime - keyStartTime # Calculating total key time
    RSATotalTime = RSATotalTime + KeyTotalTime # Calculating total RSA time

    # Requirement 2 RSA Encryption and Decryption
    message = "MESSAGE123#message"

    encryptionStartTime = time.perf_counter() # Start time
    encryptedMessage = RSA.encrypt(publicKey, message)
    encryptionEndTime = time.perf_counter() # End Time
    encryptionTotalTime = encryptionEndTime - encryptionStartTime # Calculating total encryption time
    RSATotalTime = RSATotalTime + encryptionTotalTime # Calculating total RSA time
    print("Encrypted:", encryptedMessage)

    decryptionStartTime = time.perf_counter() # Start time
    decryptedMessage = RSA.decrypt(privateKey, encryptedMessage)
    decryptionEndTime = time.perf_counter() # End time
    decryptionTotalTime = decryptionEndTime- decryptionStartTime # Calculating total decryption time
    RSATotalTime = RSATotalTime + decryptionTotalTime # Calculating total RSA time
    print("Decrypted:", decryptedMessage)

    print()

# Float value of time in seconds
print(f"Average RSA key generation: {KeyTotalTime/10} seconds")
print(f"Average RSA encryption: {encryptionTotalTime/10} seconds")
print(f"Average RSA decryption: {decryptionTotalTime/10} seconds")
print(f"Average RSA in total: {RSATotalTime/10} seconds")
print()


# S-DES part

print("S-DES part")
DESTotalTime = 0
DESKeyTotalTime = 0
DESencryptionTotalTime = 0
DESdecryptionTotalTime = 0
print()

# Requirement 4.c and 4.d
for i in range (0,10):

    print()

    # Requirement 3
    # Generate a random key
    DESKeyStartTime = time.perf_counter() # Start time
    key = SDES.keyGenerator()
    DESKeyEndTime = time.perf_counter() # End time
    DESKeyTotalTime = DESKeyEndTime- DESKeyStartTime # Calculating total of key
    DESTotalTime = DESTotalTime + DESKeyTotalTime # Calculating total DES 
    print("Generated Key:", key)

    # Message to encrypt
    message = "sayHiToS-DES"
    print("Original Message:", message)

    # Convert message to binary
    binary_message = SDES.stringToBinary(message)
    print("Binary Message:", binary_message)

    # Encrypt the message
    DESencryptionStartTime = time.perf_counter() # Start time
    encrypted_message = SDES.encrypt(binary_message, key)
    DESencryptionEndTime = time.perf_counter() # End time
    DESencryptionTotalTime = DESencryptionEndTime - DESencryptionStartTime # Calculating total encryption time
    DESTotalTime = DESTotalTime + DESencryptionTotalTime # Calculating total DES time
    print("Encrypted Message:", encrypted_message)

    # Decrypt the message
    DESdecryptionStartTime = time.perf_counter() # Start time
    decrypted_message = SDES.decrypt(encrypted_message, key)
    DESdecryptionEndTime = time.perf_counter() # End time
    DESdecryptionTotalTime = DESdecryptionEndTime - DESdecryptionStartTime # Calculating total time of decryption DES
    DESTotalTime = DESTotalTime + DESdecryptionTotalTime
    print("Decrypted Message:", decrypted_message)

    # Convert decrypted binary message to string
    decrypted_string = SDES.binaryToString(decrypted_message)
    print("Decrypted String:", decrypted_string)

print()
print(f"Average SDES key generation: {DESKeyTotalTime/10} seconds")
print(f"Average SDES encryption: {DESencryptionTotalTime/10} seconds")
print(f"Average SDES decryption: {DESdecryptionTotalTime/10} seconds")
print(f"Average SDES in total: {DESTotalTime/10} seconds")
print()

# Requirement 5
# Alice Bob Part

print()
AliceBob.main()