# https://www.vnsecurity.net/ctf%20-%20clgt%20crew/
# 2015/03/16/codegate-good-crypto.html

key=[0xa4,0x3d,0xf6,0xf3,0x74]
a, c, m = 0x000343fd, 0x269ec3, 0xFFFFFF
secret_key_bytes=5

for seed in range(1<<24):
    correct = True
    x = seed
    
    for i in range(secret_key_bytes):
        x = (a * x  + c) & m   
        # shift 16 bits to right
        # the same as check the second most significant byte 
        if (x>>16)!=key[i]:
            correct = False
            break
        
    if correct:
        print("Found it: ", hex(seed))
        print("Verify: ")
            
        for i in range(secret_key_bytes):
            seed = (a* seed + c) & m
            print(hex(seed>>16),hex(seed))