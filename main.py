import helpingFunctions
import rsa

#print("GDC Deneme 15 ve 12")
#helpingFunctions.euclidGCD(15,12)

#print("RSA Deneme")
#rsa.keyGenerator(11,5) 
# https://rsa-calculator.netlify.app/


public_key, private_key = rsa.keyGenerator()

print(">> Enter the Message <<")
message = input()
ciphertext = rsa.rsa_encrypt(str(message), public_key)
print("Ciphertext -> ", ciphertext)

print("**************************")

print(">> Enter the Ciphertext <<")
ciphertext = input()
message = rsa.rsa_decrypt(str(ciphertext), private_key)
print("Message:", message)