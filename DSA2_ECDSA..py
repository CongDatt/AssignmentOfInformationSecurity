from Cryptodome.PublicKey import DSA
from Cryptodome.Signature import DSS
from Cryptodome.Hash import SHA256
import os
import time

def DSA_task3():
    start = time.time()

    def DSA_(message):
        # Create a new DSA key
        key = DSA.generate(2048)
        print("key: ")
        print(key.export_key())
        f = open("public_key.pem", "wb")
        f.write(key.publickey().export_key())
        f.close()
        
        # Sign a message
        message = bytes(message, 'utf-8')
        hash_obj = SHA256.new(message)
        signer = DSS.new(key, 'fips-186-3')
        signature = signer.sign(hash_obj)

        return signature

    # input
    mes = input('Nhập đoạn text: ')
    signature = DSA_(mes)

    # Load the public key
    f = open("public_key.pem", "r")
    message = bytes(mes, 'utf-8')
    hash_obj = SHA256.new(message)
    pub_key = DSA.import_key(f.read())
    verifier = DSS.new(pub_key, 'fips-186-3')

    # Verify the authenticity of the message
    try:
        verifier.verify(hash_obj, signature)
        print("The message is authentic.")
    except ValueError:
        print("The message is not authentic.")

    for i in range(2,11): 
        key = DSA.generate(2048)
        f = open("public_key_t.pem", "wb")
        f.write(key.publickey().export_key())
        f.close()

        # Sign a message
        hash_obj = SHA256.new(message)
        signer = DSS.new(key, 'fips-186-3')
        signature = signer.sign(hash_obj)

        # Load the public key
        f = open("public_key_t.pem", "r")
        hash_obj = SHA256.new(message)
        pub_key = DSA.import_key(f.read())
        verifier = DSS.new(pub_key, 'fips-186-3')
        # os.remove("public_key_t.pem")
        # Verify the authenticity of the message
        try:
            verifier.verify(hash_obj, signature)
            print(i)
        except ValueError:
            print(i)

    #time
    end = time.time()
    print("running times: ")
    ti = (end - start)/10
    print(ti)

DSA_task3()