import RSA
import SDES
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
    print("Original Message:", message)
    
    encryptionStartTime = time.perf_counter() # Start time
    encryptedMessage = RSA.encrypt(publicKey, message)
    encryptionEndTime = time.perf_counter() # End Time
    encryptionTotalTime = encryptionEndTime - encryptionStartTime # Calculating total encryption time
    RSATotalTime = RSATotalTime + encryptionTotalTime # Calculating total RSA time
    print("Encrypted Message:", encryptedMessage)

    decryptionStartTime = time.perf_counter() # Start time
    decryptedMessage = RSA.decrypt(privateKey, encryptedMessage)
    decryptionEndTime = time.perf_counter() # End time
    decryptionTotalTime = decryptionEndTime- decryptionStartTime # Calculating total decryption time
    RSATotalTime = RSATotalTime + decryptionTotalTime # Calculating total RSA time
    print("Decrypted Message:", decryptedMessage)

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
# Alice Bob And Menu Part

def rsa():
    print ("RSA")
    # Key generation
    publicKey, privateKey = RSA.keyGenerator()
    print("Public Key:", publicKey)
    print("Private Key:", privateKey)

    # Encryption and decryption
    message = input("Enter message to encrypt: ")
    encryptedMessage = RSA.encrypt(publicKey, message)
    print("Encrypted Message:", encryptedMessage)

    decryptedMessage = RSA.decrypt(privateKey, encryptedMessage)
    print("Decrypted Message:", decryptedMessage)

def sdes():
    print ("S-DES")
    # Key generation
    key = SDES.keyGenerator()
    print("Generated S-DES Key:", key)

    # Encryption and decryption
    message = input("Enter message to encrypt with S-DES: ")
    binaryMessage = SDES.stringToBinary(message)
    print("Binary Message:", binaryMessage)

    encryptedMessage = SDES.encrypt(binaryMessage, key)
    print("Encrypted Message:", encryptedMessage)

    decryptedMessage = SDES.decrypt(encryptedMessage, key)
    decryptedString = SDES.binaryToString(decryptedMessage)
    print("Decrypted Message:", decryptedString)

def aliceBob():
    print ("Alice-Bob Communication")
    
    # Key generation for alice and bob in RSA
    alicePublicKey, alicePrivateKey = RSA.keyGenerator()
    bobPublicKey, bobPrivateKey = RSA.keyGenerator()

    # Alice generates a secret key for S-DES
    aliceSdesSecretKey = SDES.keyGenerator()

    # Alice encrypts the secret key with RSA.ecrypt via using Bob's public key and sends it to Bob
    encryptedKey = RSA.encrypt(bobPublicKey, aliceSdesSecretKey)
    print("Encrypted S-DES Key sent from Alice to Bob:", encryptedKey)

    # Bob decrypts the secret key using RSA with his private key
    decryptedKey = RSA.decrypt(bobPrivateKey, encryptedKey)

    # Now both Alice and Bob have the shared secret key for S-DES
    print("Shared S-DES Key between Alice and Bob:", decryptedKey)

    # Now Alice and Bob can exchange messages using S-DES encryption and decryption
    messageSend = input("Enter message from Alice to Bob: ")

    # Alice ecnrypts message via SDES
    encryptedMessage = SDES.encrypt(SDES.stringToBinary(messageSend), decryptedKey)
    print("Encrypted Message sent from Alice to Bob:", encryptedMessage)

    # Bob decrypts message via SDES
    decryptedMessage = SDES.decrypt(encryptedMessage, decryptedKey)
    print("Decrypted Message received by Bob:", SDES.binaryToString(decryptedMessage))

while True:
    print("\nOptions:")
    print("Press 1 for RSA")
    print("Press 2 for S-DES")
    print("Press 3 for Alice-Bob")
    print("Press 4 for Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        rsa()
    elif choice == '2':
        sdes()
    elif choice == '3':
        aliceBob()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please choose again.")