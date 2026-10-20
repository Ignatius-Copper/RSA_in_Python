import random
def generator_d(e,N):
    modulus=N
    x0,x1=0,1
    if N==1:
        return 0
    while e>1:
        q=e//N
        e,N=N,e % N
        x0,x1=x1-q*x0,x0
    if x1 < 0:
        x1 += modulus
    return x1
def check_on_common_numbers(q):
    check_number=False
    num=2
    if q <=1:
        return False
    while check_number !=True:
        if(q % num ==0):
            return False
        elif num*num>q:
            return True
        else:
            num+=1
def RSA_generator_keys():
    equals = True
    while equals == True:
        p = random.randint(10000, 1000000)
        q = random.randint(10000, 1000000)
        if p != q and check_on_common_numbers(p) and check_on_common_numbers(q):
            equals = False
            n = p * q
            break
    F=(p-1)*(q-1)
    e=generator_e(F)
    return e,n,F
def generator_e(N):
    while True:
     e=random.randint(1,N-1)
     b=e
     a = N
     if not check_on_common_numbers(e):
         continue
     while b!=0:
      a,b=b,a%b
     comprime=a
     if(comprime==1):
        return e

def RSA_encode(text,e,n):
    encryption=[]
    for i in text:
        char_word=pow(ord(i),e,n)
        encryption.append(char_word)
    return encryption
def RSA_decode(encode,d,n):
    decode_string=""
    for i in encode:
        letter_num=pow(i,d,n)
        letter=chr(letter_num)
        decode_string+=letter

    return decode_string
text=input("Input text: ")
keys=RSA_generator_keys()
e,n,F=keys
print(f"Public key n: {n}")
print(f"Public key e: {e}")
encode=RSA_encode(text,e,n)
d=generator_d(e,F)
decode=RSA_decode(encode,d,n)
print(encode)
print(decode)
