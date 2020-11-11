from Crypto.PublicKey import ECC
import time

# source : https://pycryptodome.readthedocs.io/en/latest/src/public_key/ecc.html

i=0
for x in range(1000):
    start_time = time.time()

    key = ECC.generate(curve='P-256')
    f = open('myprivatekey.pem','wt')
    f.write(key.export_key(format='PEM'))
    f.close()
    f = open('myprivatekey.pem','rt')
    key = ECC.import_key(f.read())

    end_time = time.time()
    d=(end_time - start_time) * 1000
    i=i+d
    i=i/1000
print('The average of 1000 running times = %f ms ' %i)