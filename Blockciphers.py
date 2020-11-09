from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto import Random
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter
import time
import base64
import binascii



data=get_random_bytes(32)
key = get_random_bytes(16)
def CipherAes(data,key):
	#ECB
	cipher = AES.new(key, AES.MODE_ECB)
	ciphered_data = cipher.encrypt(pad(data, AES.block_size))
	original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)
	
	#CBC
	iv = get_random_bytes(AES.block_size)
	cipher = AES.new(key, AES.MODE_CBC,iv)
	ciphered_data = cipher.encrypt(pad(data, AES.block_size))
	#CFB
	iv = get_random_bytes(AES.block_size)
	cipher = AES.new(key, AES.MODE_CFB,iv)
	ciphered_data = cipher.encrypt(pad(data, AES.block_size))
	#OFB
	iv = get_random_bytes(AES.block_size)
	cipher = AES.new(key, AES.MODE_OFB,iv)
	ciphered_data = cipher.encrypt(pad(data, AES.block_size))
	#CTR
	iv = get_random_bytes(AES.block_size)
	ctr = Counter.new(128, initial_value=int(binascii.hexlify(iv),16))
	cipher = AES.new(key, AES.MODE_CTR,counter=ctr)
	ciphered_data = cipher.encrypt(pad(data, AES.block_size))
	return
i=0
for x in range(1000):
	start_time = time.time()
	CipherAes(data,key)
	end_time = time.time()
	d=(end_time - start_time) * 1000
	i=i+d
i=i/1000
print('Run time avera  = %f ms ' %i)

