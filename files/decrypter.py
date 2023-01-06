import os
import pyaes

## open the encrypted file
file_name = "victimchan.txt.ransomchankiller"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## key to decrypt it 
key = b"ransomwarechan"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remove the file
os.remove(file_name)

## and create the decrypted file
new_file = "victimchan.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
