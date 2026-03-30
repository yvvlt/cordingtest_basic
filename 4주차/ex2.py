str_ = ""

def factorial_(n):
    global str_
    if (n == 1) :
        str_ += str(1)
        return 1
    else:
        str_ += (str(n) + " * ")
        return n * factorial_(n-1)
    
result = factorial_(5)

print("5! :" + str_, " = ", result)