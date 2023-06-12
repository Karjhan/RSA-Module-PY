import utils
import random
def generatePrimeListForRSAKeys(keysize):
    lowerBound = 1 << (keysize//2 - 1)
    upperBound = 1 << (keysize//2 + 1)
    primes = [2]
    for i in range(3, upperBound+1, 2):
        for p in primes:
            if(i % p == 0):
                break
        else:
            primes.append(i)
    while (len(primes) > 0 and primes[0] < lowerBound):
        del primes[0]
    return primes

def generatePublicAndPrivateKeys(keysize):
    # generating p,q
    lowerBoundForN = 1 << (keysize - 1)
    upperBoundForN = (1 << keysize) - 1
    primes = generatePrimeListForRSAKeys(keysize)
    p = random.choice(primes)
    primes.remove(p)
    q = 2
    possibleValuesForQ = []
    for prime in primes:
        if (lowerBoundForN <= prime * p <= upperBoundForN):
            possibleValuesForQ.append(prime)
    if(len(possibleValuesForQ) > 0):
        q = random.choice(possibleValuesForQ)

    # writing n and phi(n)
    n = p * q
    coprimesWithNCount = (p - 1) * (q - 1)

    # generating e and d
    e = random.randrange(1, coprimesWithNCount)
    commonDiv = utils.greatestCommonDiv(e, coprimesWithNCount)
    d = utils.modInverse(e, commonDiv)
    while True:
        e = random.randrange(1, coprimesWithNCount)
        commonDiv = utils.greatestCommonDiv(e, coprimesWithNCount)
        d = utils.modInverse(e, coprimesWithNCount)
        if commonDiv == 1 and e != d and d != -1:
            break

    # returning public and private keys
    return ((e, n), (d, n))

def RSAEncryptPadding(text, publicKey):
    blockSize = publicKey[1].bit_length()//8
    paddedText = utils.padMessage(bytes(text, 'ascii'),blockSize)
    encryptedBlocks = []
    for i in range(0, len(paddedText), blockSize):
        block = int.from_bytes(paddedText[i:i + blockSize], 'big')
        encryptedBlocks.append(pow(block, publicKey[0], publicKey[1]))

    encryptedMessage = b''.join([block.to_bytes(blockSize, 'big') for block in encryptedBlocks])
    return encryptedMessage

def RSADecryptPadding(text, privateKey):
    blockSize = privateKey[1].bit_length()//8
    decrypted_blocks = []
    for i in range(0, len(text), blockSize):
        block = int.from_bytes(text[i:i + blockSize], 'big')
        decrypted_blocks.append(pow(block, privateKey[0], privateKey[1]))

    decryptedMessage = b''.join([block.to_bytes(blockSize, 'big') for block in decrypted_blocks])
    return utils.unpadMessage(decryptedMessage)

def RSAEncrypt(text, publicKey):
    encryptedMessage = []
    for i in range(len(text)):
        # encryptedMessage = encryptedMessage[:i] + (math.pow(ord(encryptedMessage[i]),publicKey[0]) % publicKey[1]) + encryptedMessage[i+1:]
        encryptedMessage.append(pow(ord(text[i]), publicKey[0], publicKey[1]))
    return encryptedMessage

def RSADecrypt(encrypted, privateKey):
    decryptedMessage = []
    for i in range(len(encrypted)):
        # decryptedMessage = decryptedMessage[:i] + chr(math.pow(decryptedMessage[i],privateKey[0],) % privateKey[1]) + decryptedMessage[i+1:]
        decryptedMessage.append(chr(pow(encrypted[i], privateKey[0],privateKey[1])))
    return ''.join(decryptedMessage)

