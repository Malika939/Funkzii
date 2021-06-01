import random
def gen_number():
    s = str()
    s = '0444'
    a = [1, 4, 5, 7, 9, 0]
    for i in range (1, 6):
        n = random.choice(a)
        s += str(n)
    print (s)
gen_number()