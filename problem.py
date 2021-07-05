import math
import random

LEN = 10000

def is_prime(n):
    if n <=2:
        return False
    else:
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

def execute_input(input):
    prime_count = 0
    prime_sum = 0
    for i in input:
        if is_prime(i):
            prime_sum += i
            prime_count += 1
    if prime_count == 3 and prime_sum == 37:
        raise RuntimeError

def generate_input(len):
    seq = []
    for i in range(len):
        n = random.randrange(1000)
        while n in set(poison) or is_prime(n):
            n = random.randrange(1000)
        seq.append(n)
    return seq

def generate_faulty_input(len):
    seq = []
    poison = [7, 13, 17]
    for i in range(len):
        n = random.randrange(1000)
        while n in set(poison) or is_prime(n):
            n = random.randrange(1000)
        seq.append(n)
    fault_index = {}
    for i in range(3):
        j = random.randrange(len)
        while j in fault_index:
            j= random.randrange(len)
        seq[j] = poison[i]
    return seq

def write_input(fault):
    if fault:
        seq = generate_faulty_input(LEN)
        out = open("fail_linear.txt", "w")
        for i in seq:
            out.write(f"{i}\n")
        out.close()
    else:
        seq = generate_input(LEN)
        out = open("pass.txt", "w")
        for i in seq:
            out.write(f"{i}\n")
        out.close()