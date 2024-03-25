import RSA
import SDES

def rsa_key_gen():
    public_key, private_key = RSA.keyGenerator()
    print("Public Key:", public_key)
    print("Private Key:", private_key)

def rsa_encrypt_decrypt():
    message = input("Enter message to encrypt: ")
    public_key, private_key = RSA.keyGenerator()
    encrypted_message = RSA.encrypt(public_key, message)
    print("Encrypted Message:", encrypted_message)
    decrypted_message = RSA.decrypt(private_key, encrypted_message)
    print("Decrypted Message:", decrypted_message)

def sdes_key_gen():
    key = SDES.keyGenerator()
    print("Generated S-DES Key:", key)

def sdes_encrypt_decrypt():
    key = SDES.keyGenerator()
    message = input("Enter message to encrypt with S-DES: ")
    binary_message = SDES.stringToBinary(message)
    print("Binary Message:", binary_message)
    encrypted_message = SDES.encrypt(binary_message, key)
    print("Encrypted Message:", encrypted_message)
    decrypted_message = SDES.decrypt(encrypted_message, key)
    decrypted_string = SDES.binaryToString(decrypted_message)
    print("Decrypted Message:", decrypted_string)

def alice_bob_communication():
    alice_public, alice_private = RSA.keyGenerator()
    bob_public, bob_private = RSA.keyGenerator()

    # Alice generates a secret key for S-DES
    sdes_key = SDES.keyGenerator()

    # Alice encrypts the secret key with RSA and sends it to Bob
    encrypted_key = RSA.encrypt(bob_public, sdes_key)
    print("Encrypted S-DES Key sent from Alice to Bob:", encrypted_key)

    # Bob decrypts the secret key using RSA
    decrypted_key = RSA.decrypt(bob_private, encrypted_key)

    # Now both Alice and Bob have the shared secret key for S-DES
    print("Shared S-DES Key between Alice and Bob:", decrypted_key)

    # Now Alice and Bob can exchange messages using S-DES encryption and decryption
    message_to_send = input("Alice, enter message to send to Bob: ")
    encrypted_message = SDES.encrypt(SDES.stringToBinary(message_to_send), decrypted_key)
    print("Encrypted Message sent from Alice to Bob:", encrypted_message)

    decrypted_message = SDES.decrypt(encrypted_message, decrypted_key)
    print("Decrypted Message received by Bob:", SDES.binaryToString(decrypted_message))

# Main function to handle user input and execute desired functionality
def main():
    while True:
        print("\nOptions:")
        print("1. RSA Key Generation")
        print("2. RSA Encryption/Decryption")
        print("3. S-DES Key Generation")
        print("4. S-DES Encryption/Decryption")
        print("5. Alice-Bob Communication")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            rsa_key_gen()
        elif choice == '2':
            rsa_encrypt_decrypt()
        elif choice == '3':
            sdes_key_gen()
        elif choice == '4':
            sdes_encrypt_decrypt()
        elif choice == '5':
            alice_bob_communication()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
