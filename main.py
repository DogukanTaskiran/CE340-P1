import RSA
import SDES

publicKey, privateKey = RSA.keyGenerator()

message = "DENEME123!"
encryptedMessage = RSA.encrypt(publicKey, message)
print("Encrypted:", encryptedMessage)

decryptedMessage = RSA.decrypt(privateKey, encryptedMessage)
print("Decrypted:", decryptedMessage)

print()
print("SDES Keys")

# Debugger to see values of keys (Geçici deneme)
sdesKeys = SDES.generateSubkeys([1, 0, 1, 0, 0, 0, 0, 0, 1, 0])
print(sdesKeys)

# Example usage:
plaintext = [1, 0, 1, 0, 0, 0, 1, 1]  # Example 8-bit plaintext block
permuted_plaintext = SDES.initialPermutation(plaintext)
print("Initial Permutation:", permuted_plaintext)

# Example usage for inverse permutation:
ciphertext = [0, 1, 1, 0, 1, 0, 0, 1]  # Example 8-bit ciphertext block
inverse_permuted_ciphertext = SDES.inversePermutation(ciphertext)
print("Inverse Permutation:", inverse_permuted_ciphertext)

message = input("Enter the message: ")
key = input("Enter the key (10-bit binary): ")

# Convert string message to binary
binary_message = SDES.string_to_binary(message)
key_binary = [int(bit) for bit in key]

print("Encrypting using key:", key)  # Anahtarı print et

    # Encrypt the message
encrypted_message = SDES.encrypt(binary_message, key_binary)
print("Encrypted Message:", SDES.binary_to_string(encrypted_message))

    # Decrypt the message
decrypted_message = SDES.decrypt(encrypted_message, key_binary)
print("Decrypted Message:", SDES.binary_to_string(decrypted_message))