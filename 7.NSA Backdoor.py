#!/usr/bin/python

from binascii import hexlify
from gmpy2 import *
import gmpy2
import math
import os
import sys
from Crypto.Util.number import*

# if sys.version_info < (3, 9):
#     math.gcd = gcd
#     math.lcm = lcm

# _DEBUG = False

# FLAG  = open('flag.txt').read().strip()
# FLAG  = mpz(hexlify(FLAG.encode()), 16)
# SEED  = mpz(hexlify(os.urandom(32)).decode(), 16)
# STATE = random_state(SEED)

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

# while True:
#     p, p_factors = get_smooth_prime(STATE, 1024, 16)
#     if len(p_factors) != len(set(p_factors)):
#         continue
#     # Smoothness should be different or some might encounter issues.
#     q, q_factors = get_smooth_prime(STATE, 1024, 17)
#     if len(q_factors) == len(set(q_factors)):
#         factors = p_factors + q_factors
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
# c = pow(3, FLAG, n)
# print(f'n = {n.digits(16)}')
# print(f'c = {c.digits(16)}')
n = int('0x72bae3105c52d6ca470aa6d21b1a8a9f2208951ca6cd71d1b484e38095e0558b32d9db2f926771dc4a93b6deebaf64d2978f0f4efc8f49db5571959e214c900a4bed54fa235ee72cec66c85bca819ea3fb1b4e3dd70e940d9067eb3d0a6a4abf6c152d7d1a19d0833532048ec84754c95eb8055b7e3817e65aea897e3e2a29764af08589a6271721c863df2386ceb9eea4f208ed8f45f0628d5ec3afcc416ab3dda4071a9fca2166e87f14a9475b1711a0b4ccdefab041a7e2a7b418155aed4a1bbc343a0c1a8d9af479ff7e62765bfb5f1762aa66c4b06ce44b5681977e027428b32811c8c539f0c631178ed60a863176cdd1fd73ee9cbe14eaa5e7010443cd',0)
c = int('0x4790c71b682f70a3e8aeaeb62b7b5c7381b27ab013d806631efd826da0bfc4ea7f343ad33ea0abdd14762acf5fcdf02b3e44646b8df7b09345ec2c43614a15e4e38bda58bf0b08f643e521d04f4d1eb06a4521351533b4140df785f12fa085db1e14dba803f00a25208167b359045d4491a49463f2423894dc69d92fc814229bf3d439b0d552732363af89605fc5bc035612b68c49d01c5ec185028d3d036332f6d5d7bccc1e65c7fe13aefb3c8a4ebeb8006092cb714b9040ec3147c0ec784cb6e6cae2456999afdc8fcacd3f3d2502d29b59be9f47e5ff192512ff6a37cf12837f3da1a1905de2d5a4ae7eea353c1b0c15c764bb10a45a21cdb84c3bf948ef',0)
p = 99755582215898641407852705728849845011216465185285211890507480631690828127706976150193361900607547572612649004926900810814622928574610545242732025536653312012118816651110903126840980322976744546241025457578454651121668690556783678825279039346489911822502647155696586387159134782652895389723477462451243655239
q = n//p
print(q)
print(c)
phi = (p-1)*(q-1)
tmp1 = 38251710328773353864629245699093278635133 + 49877791107949320703926352864424922505608232592642605945253740315845414063853488075096680950303773786306324502463450405407311464287305272621366012768326656006059408325555451563420490161488372273120512728789227325560834345278391839412639519673244955911251323577848293193579567391326447694861738731225621827619
tmp2 = 38251710328773353864629245699093278635133 + 7259405360219799847061861225551086441372489067857726566991253493918066548020102163313480833003101600059207304540449584489538757304054628817749657824044922487981710214063236702734145889165714638176260753206118223755250002401650679002985789801832614998413133586475252918339038632183100099580986372710436379813 
print(long_to_bytes(38251710328773353864629245699093278635133))

