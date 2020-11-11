from Cryptodome.PublicKey import DSA
from Cryptodome.Signature import DSS
from Cryptodome.Hash import SHA256
import time
from Crypto.Random import get_random_bytes

message = get_random_bytes(32) # 32 bytes * 8 = 256 bits
# data = get_random_bytes(64) # 512
# data = get_random_bytes(128) #1024
# data = get_random_bytes(256) #2048 
# data = get_random_bytes(512) # 4096

def DSA_(message):
    key = DSA.generate(2048)
    print("key: ")
    print(key.export_key())
    key.publickey().export_key()
    message = bytes(message)
    hash_obj = SHA256.new(message)
    signer = DSS.new(key, 'fips-186-3')
    signature = signer.sign(hash_obj)
    return signature

i=0
for x in range(1000):
    start_time = time.time()
    # a = DSA_(message)
    # print(a)
    DSA_(message)
    end_time = time.time()
    d=(end_time - start_time) * 1000
    i=i+d
    i=i/1000
print('The average of 1000 running times  = %f ms ' %i)