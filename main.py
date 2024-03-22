import helpingFunctions
import rsa
import desKey

rsa.rsa_encryption("DENEME123!")

encryptedInput = None
dInput = None
nInput = None

print("↓ Please write the Encrypted Message ↓")
encryptedInput = input()
print("↓ Please write the d ↓")
dInput = input()
print("↓ Please write the n ↓")
nInput = input()

rsa.rsa_decryption(int(encryptedInput),int(dInput), int(nInput))