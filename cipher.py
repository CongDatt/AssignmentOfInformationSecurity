from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter
import time
import base64
import binascii


# data = get_random_bytes(64) # 512
# data = get_random_bytes(128) #1024
# data = get_random_bytes(256) #2048 
# data = get_random_bytes(512) # 4096

data=get_random_bytes(32) #sử dụng hàm get_random_bytes trong Cryto lấy 32 byte ngẫu nhiên
key = get_random_bytes(16) # tạo ra khóa ngẫu nhiêu dài 16 bytes = 128 bít
def CipherAes(data,key):
	#ECB
	cipher = AES.new(key, AES.MODE_ECB)# tạo ra mã hóa bằng hàm AES với mode ECB
	ciphered_data = cipher.encrypt(pad(data, AES.block_size)) # mã hóa dữ liện trong data, sử dụng pad để đệm dữ liệu để vừa với block_size của mã hóa AES
	original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size) # giải mã và tháo phần dữ liệu đệm
	a=base64.b64encode(ciphered_data)# chuyen doi thanh base64
	print('ECB ciphered:',a)
	
	#CBC
	iv = get_random_bytes(AES.block_size) # khởi tạo vector lấy ngẫu nhiêu 16 bytes
	cipher = AES.new(key, AES.MODE_CBC,iv) #tạo ra mã hóa bằng hàm AES với mode CBC và iv
	ciphered_data = cipher.encrypt(pad(data, AES.block_size))# mã hóa dữ liện trong data, sử dụng pad để đệm dữ liệu để vừa với block_size của mã hóa AES
	a=base64.b64encode(ciphered_data)
	print('CBC ciphered:',a)
	cipher = AES.new(key, AES.MODE_CBC,iv) # để giải mã cần phải cung cấp lại mã hóa đã thực hiện
	original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size) # giải mã và tháo phần dữ liệu đệm
	#CFB
	iv = get_random_bytes(AES.block_size) # tương tự CBC
	cipher = AES.new(key, AES.MODE_CFB,iv)
	ciphered_data = cipher.encrypt(pad(data, AES.block_size))
	a=base64.b64encode(ciphered_data)
	print('CFB ciphered:',a)
	cipher = AES.new(key, AES.MODE_CFB,iv)
	original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)
	#OFB
	iv = get_random_bytes(AES.block_size) # tương tự CBC
	cipher = AES.new(key, AES.MODE_OFB,iv)
	ciphered_data = cipher.encrypt(pad(data, AES.block_size))
	a=base64.b64encode(ciphered_data)
	print('OFB ciphered:',a)
	cipher = AES.new(key, AES.MODE_OFB,iv)
	original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)
	#CTR
	iv = get_random_bytes(AES.block_size) #khởi tạo vector lấy ngẫu nhiêu 16 bytes
	ctr = Counter.new(128, initial_value=int(binascii.hexlify(iv),16)) # tạo biến đếm với với chiều dài và giá trị bắt đầu vừa với block_size 
	cipher = AES.new(key, AES.MODE_CTR,counter=ctr)#tạo ra mã hóa bằng hàm AES với mode CTR và counter đã tạo
	ciphered_data = cipher.encrypt(data)# mã hóa
	a=base64.b64encode(ciphered_data)
	print('CTR ciphered:',a)
	cipher = AES.new(key, AES.MODE_CTR,counter=ctr)# gọi lại mã hóa để giải mã
	original_data = cipher.decrypt(ciphered_data)# giải mã
	return;

i=0												
for x in range(1000):
	start_time = time.time()				#tính thời gian trung bình thực hiện hàm 1000 l
	CipherAes(data,key)
	end_time = time.time()
	d=(end_time - start_time) * 1000
	i=i+d
i=i/1000
print('The average of 1000 running times  = %f ms ' %i)

