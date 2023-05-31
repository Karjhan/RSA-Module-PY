import math
import random


def greatestCommonDiv(num1, num2):
    if(num2 == 0):
        return num1
    return greatestCommonDiv(num2, num1 % num2)

def isPrime(number):
    if(number < 2):
        return False
    if(number == 2):
        return True
    for i in range(2, int(math.sqrt(number)+1)/2):
        if(number % i == 0):
            return False
    return True

def modInverse(number, modulus):
    for i in range(1,modulus):
        if(number * i) % modulus == 1:
            return i
    return -1

def padMessage(message, blockSize):
    padding_length = blockSize - 3 - len(message)
    padding = b'\x00\x02' + bytes([random.randint(1, 255) for _ in range(padding_length)]) + b'\x00'
    return padding + message

def unpadMessage(paddedMessage):
    padding_start = paddedMessage.find(b'\x00', 2) + 1
    return paddedMessage[padding_start:]