from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os, json, base64
import sqlite3

# AES needs a 128-bit key (16 bytes)
key = bytes.fromhex('0123456789ABCDEF'*2)
iv = bytes.fromhex('0123456789ABCDEF'*2)
aesCipher = Cipher(algorithms.AES(key), modes.CTR(iv))
aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()

message = {'name' : {'first' : 'Bilbo', 'last' : 'Baggins'},
           'card number' : '1234-5678-9012-3456',
           'expiration date' : '04/20',
           'cvv' : '420'}

cleartext = json.dumps(message)

# Convert the message to bytes
messageBytes = cleartext.encode()

# Encrypt the message
ct = aesEncryptor.update(messageBytes) + aesEncryptor.finalize()

# convert to base 64
ct = base64.b64encode(ct)
print(ct)

# create a customer table with a customer id and a column for an encrypted credit card
conn = sqlite3.connect('customer.db')
c = conn.cursor()

# drop the table if it exists
c.execute("DROP TABLE IF EXISTS customer")

c.execute('''CREATE TABLE customer (
                 customer_id text, 
                 credit_card text,
                 PRIMARY KEY (customer_id)
             )'''
          )

# insert a customer id and the encrypted credit card
c.execute("INSERT INTO customer VALUES ('1', ?)", (ct,))

# retrieve the encrypted credit card
c.execute("SELECT credit_card FROM customer WHERE customer_id = '1'")
row = c.fetchone()

# decrypt the credit card
ct = base64.b64decode(row[0])
pt = aesDecryptor.update(ct) + aesDecryptor.finalize()

# convert pt to a string
pt = pt.decode()
print(pt)

conn.close()

