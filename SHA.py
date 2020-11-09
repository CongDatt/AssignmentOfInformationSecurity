from Crypto.Hash import SHA1
from Crypto.Hash import SHA256
from Crypto.Hash import SHA3_256
from Crypto import Random
from Crypto.Random import get_random_bytes
import time

data = get_random_bytes(32) # 32 ~ 256 bits

def sha1(data):
    c = SHA1.new()
    c.update(data)
    return c.hexdigest()

def sha256(data):
    c = SHA256.new()
    c.update(data)
    return c.hexdigest()

def sha3_256(data):
    c = SHA3_256.new()
    c.update(data)
    return c.hexdigest()

i=0
for x in range(1000):
    start_time = time.time()
    sha_1 = sha1(data)
    sha_2 = sha256(data)
    sha_3 = sha3_256(data)
    print('SHA-1 :'+sha_1)
    print('SHA-2 :'+sha_2)
    print('SHA-3 :'+sha_3)
    end_time = time.time()
    d=(end_time - start_time) * 1000
    i=i+d
    i=i/1000
print('Run time avera  = %f ms ' %i)




# a = sha1('hello')
# a = sha1('hello')
# print("SHA-1 : "+a)
# print("SHA256 : "+b)
# print("SHA3_256 : "+c)