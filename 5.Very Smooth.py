#!/usr/bin/python

from binascii import hexlify
from gmpy2 import *
import math
import os
import sys
from Crypto.Util.number import*
from math import gcd
def pollar(n):
    a = 2
    j = 2
    while True:
        a = pow(a,j,n)
        d = gcd(a-1,n)
        if(d >1 and d<n):
            return d
        j = j+1
    return "none"
# if sys.version_info < (3, 9):
#     math.gcd = gcd
#     math.lcm = lcm

# _DEBUG = False

# # FLAG  = open('flag.txt').read().strip()
# # FLAG  = mpz(hexlify(FLAG.encode()), 16)
# # SEED  = mpz(hexlify(os.urandom(32)).decode(), 16)
# # STATE = random_state(SEED)

# def get_prime(state, bits):
#     return next_prime(mpz_urandomb(state, bits) | (1 << (bits - 1)))

# def get_smooth_prime(state, bits, smoothness=16):
#     p = mpz(2)
#     p_factors = [p]
#     while p.bit_length() < bits - 2 * smoothness:
#         factor = get_prime(state, smoothness)
#         p_factors.append(factor)
#         p *= factor

#     bitcnt = (bits - p.bit_length()) // 2

#     while True:
#         prime1 = get_prime(state, bitcnt)
#         prime2 = get_prime(state, bitcnt)
#         tmpp = p * prime1 * prime2
#         if tmpp.bit_length() < bits:
#             bitcnt += 1
#             continue
#         if tmpp.bit_length() > bits:
#             bitcnt -= 1
#             continue
#         if is_prime(tmpp + 1):
#             p_factors.append(prime1)
#             p_factors.append(prime2)
#             p = tmpp + 1
#             break

#     p_factors.sort()

#     return (p, p_factors)

# e = 0x10001


# while True:
#     p, p_factors = get_smooth_prime(STATE, 1024, 16)
#     if len(p_factors) != len(set(p_factors)):
#         continue
#     # Smoothness should be different or some might encounter issues.
#     q, q_factors = get_smooth_prime(STATE, 1024, 17)
#     if len(q_factors) != len(set(q_factors)):
#         continue
#     factors = p_factors + q_factors
#     if e not in factors:
#         break

# if _DEBUG:
#     import sys
#     sys.stderr.write(f'p = {p.digits(16)}\n\n')
#     sys.stderr.write(f'p_factors = [\n')
#     for factor in p_factors:
#         sys.stderr.write(f'    {factor.digits(16)},\n')
#     sys.stderr.write(f']\n\n')

#     sys.stderr.write(f'q = {q.digits(16)}\n\n')
#     sys.stderr.write(f'q_factors = [\n')
#     for factor in q_factors:
#         sys.stderr.write(f'    {factor.digits(16)},\n')
#     sys.stderr.write(f']\n\n')

# n = p * q

# m = math.lcm(p - 1, q - 1)
# d = pow(e, -1, m)

# c = pow(FLAG, e, n)
# print(f'n = {n.digits(16)}')
# print(f'c = {c.digits(16)}')
n = int('0x6c5f4a08d820579e606aeb3800d1602c53825167d01bd7c87f43041afdc82877c50bbcc7830a0bf8c718fc9016e4a9e73ff0dfe1edd38688acb6add89b2bd6264d61e2ce0c9b3b0813b46b0eb1fcfc56b9f7f072ba2e1e986e6420f8ad9063e10fa9bca464b23fcf0135f95dc11a89bfddf2e81572c196f4362ea551aee18b343638d9d703b234e788bff4ddc3e885da77c7940a0fa670ddc1604646871f0739199fa7fa01f9ed7d84fb9f0cc82965450e7c97153fec84ef8e10a7fceb37a90e847a012528c733070e9ab751215b13a7e2d485089c0c4d00b81dbab382ef7681c717c76c2b14ce6495ef121540653561c3dd519c5f6e2ead18e9d90f3769a029',0)
c = int('0x42cbc15285a307d86ac5184c89d6bea5ebdc0a7546debedfe40af69fa6813eaf11ef86543349062587621b845e82817cf7f154c067733ee8b23a75e45861ee0c45a07e702dcb199adffa4ca0892fcd85abfe9e9b59c2ac2df7811a656a3fda16f385972107481409e33e820a19864233b8a35bc49734dc337786dc06c0460a4ec9fc06d16fd66a43654390a526ab0a6239b14427a9868399f6e4863ac04539690357e9a4fa67450286febd9a97dd07864f516f6756c2ffad0b1ba5882980f0089605f0def91120a80a448f77ec272be41de0e11695ba7d0c8899b1d9e8905a1b5e95a755e584dead086f35844052f261e8dcd0d6cffdce38cd5181235dfa0745',0)
e = 65537
p = pollar(n)
q = n//p

m = math.lcm(p - 1, q - 1)
d = pow(e, -1, m)
print(long_to_bytes(pow(c,d,n)))

