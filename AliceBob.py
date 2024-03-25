import RSA
import SDES

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

def main():
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

if __name__ == "__main__":
    main()
