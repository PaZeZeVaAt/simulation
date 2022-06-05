import os
import codecs
import time
from time import ctime
import sys
import math
from threading import Thread

import numpy as np
import random
import matplotlib.pyplot as plt
from pytz import country_timezones

HW_FILE = "hw"
KEYPLUS = "88 "
KEYMINUS = "99 "
NOISE = 1
ATTEMPTS = 1
NUMBER_OF_THREADS = 1
start = 0
PRIMES_NUM = 74
PRIMES_BATCHES = 15
SUM_ATTEMPTS = 0

SEQUENCE = []

PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 587]

BATCH_SIZES = [2, 3, 4, 4, 5, 5, 5, 5, 5, 7, 7, 8, 7, 6, 1] 

BOUNDS = [6, 9, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 8, 6, 1]

BATCHES = [[3, 5], 
[7, 11, 13], 
[17, 19, 23, 29], 
[31, 37, 41, 43], 
[47, 53, 59, 61, 67], 
[71, 73, 79, 83, 89], 
[97, 101, 103, 107, 109], 
[113, 127, 131, 137, 139], 
[149, 151, 157, 163, 167], 
[173, 179, 181, 191, 193, 197, 199], 
[211, 223, 227, 229, 233, 239, 241], 
[251, 257, 263, 269, 271, 277, 281, 283], 
[293, 307, 311, 313, 317, 331, 337], 
[347, 349, 353, 359, 367, 373], 
[587]]

ROUNDS = [[13, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 12, 14], 
[12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 13], 
[12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 13], 
[12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 13], 
[12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 13], 
[12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 13], 
[11, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 12], 
[11, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 12], 
[10, 8, 7, 6, 5, 4, 3, 2, 1, 9, 11], 
[10, 8, 7, 6, 5, 4, 3, 2, 9, 11], 
[10, 8, 7, 6, 5, 4, 3, 2, 9, 11], 
[10, 8, 7, 6, 5, 4, 9, 11]]

NUM_OF_ATTEMPTS = [1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 11, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 20, 20, 22, 26, 40, 40, 40, 40, 40, 41, 41, 41, 42, 42, 43, 45, 48, 56, 85, 85, 86, 86, 86, 87, 87, 88, 89, 90, 93, 96, 102, 119, 179, 180, 181, 181, 182, 183, 184, 186, 188, 191, 195, 202, 214, 250, 376, 378, 379, 380, 383, 385, 389, 393, 398, 407, 421, 447, 522, 525, 526, 528, 532, 535, 540, 546, 553, 565, 584, 621, 725, 728, 731, 734, 739, 746, 754, 764, 781, 807, 858, 1001, 1007, 1011, 1016, 1023, 1032, 1043, 1057, 1080, 1117, 1186, 1193, 1198, 1204, 1212, 1223, 1236, 1253, 1281, 1323, 1406, 1414, 1420, 1427, 1436, 1449, 1464, 1485, 1518, 1526, 1533]


# Bob's secret key for checking
B = [1, -5, -3, 0, -6, -6, 4, 0, -1, -1, 2, 4, 4, 4, -1, -2, 3, 2, -2, -1, -1, -2, 6, 0, -1, 1, 0, 10, 4, -2, -2, -2, -2, 1, 4, 2, 2, -3, 0, 1, 0, 4, 0, 0, -7, 1, 0, 1, 0, -1, 1, 8, 0, 0, 0, 2, -2, 1, -5, 2, -2, -1, -1, -1, 0, 1, 2, 0, -1, -2, 0, 0, 0, 0]
BSAVE = [1, -5, -3, 0, -6, -6, 4, 0, -1, -1, 2, 4, 4, 4, -1, -2, 3, 2, -2, -1, -1, -2, 6, 0, -1, 1, 0, 10, 4, -2, -2, -2, -2, 1, 4, 2, 2, -3, 0, 1, 0, 4, 0, 0, -7, 1, 0, 1, 0, -1, 1, 8, 0, 0, 0, 2, -2, 1, -5, 2, -2, -1, -1, -1, 0, 1, 2, 0, -1, -2, 0, 0, 0, 0]

ZEROES = [0] * len(B)
INCREASED = [0] * len(B)
CURRENT_LI = 0
EXPECTED_SEQ = []
KEYGEN = './attackKG511.main '
ATTACK = './attackHW511.main '

sk = [0] * len(B)
sk_minus = [0] * len(B)

class returnValue:
    def __init__(self):
        self.result = None

def check():
    global sk, BSAVE
    wrong = 0
    for i in range(len(B)):
        if(sk[i] != BSAVE[i]):
            wrong+=1
    return wrong

def decision(sk, li, hw_plus, hw_minus):
    hw_plus = hw_plus[:-1].split(":")
    hw_minus = hw_minus[:-1].split(":")
    # check X values
    for i in range(0, len(hw_plus), 1):
        if(hw_plus[i].count('1') < NOISE) and (len(hw_plus[i])>0):
            return -1
    for i in range(0, len(hw_minus), 1):
        if(hw_minus[i].count('1') < NOISE)  and (len(hw_minus[i])>0):
            return +1

    return 0

def are_eq(a, b):
    return set(a) == set(b) and len(a) == len(b)

    
def startDF(cmd, num_of_attempts, result):
    # global EXPECTED_SEQ, CURRENT_LI
    result.result = ""
    for _ in range(num_of_attempts):
        callHW = ""
        while(callHW == ""):
            callHW = os.popen(cmd).read()
            split = callHW[:-1].split("\n")
            # check if the sequence of ell_i are equivalent
            # seq = split[0].split(", ")
            # if(are_eq(seq[:-1], EXPECTED_SEQ)) and (B[CURRENT_LI] != 0):
            #     print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ EQUAL")
            # else:
            #     print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ UNEQUAL")                      
        result.result += ":" + split[1]

def collectHW(li, type, num_of_attempts):
    global NUMBER_OF_THREADS, ATTACK, SUM_ATTEMPTS
    SUM_ATTEMPTS += num_of_attempts
    if(type ==  "_plus"):
        param = KEYPLUS
    if(type ==  "_minus"):
        param = KEYMINUS   
    # 1st param := which li to attack
    param += str(li)
    # param += " 0 "
    # 2nd param := how many attemmpts
    # param += str(NUM_OF_ATTEMPTS[li]) + " "
    cmd = ATTACK + param
    # print("calling " + cmd)
    # print("collecting hamming weights " + str(NUM_OF_ATTEMPTS[li]) + "x ...")
    threads = []
    
    attemptsT = math.ceil(num_of_attempts/NUMBER_OF_THREADS)
    
    result = [returnValue() for i in range(NUMBER_OF_THREADS)]

    threads = [Thread(target=startDF, args=(cmd, attemptsT, result[i])) for i in range(NUMBER_OF_THREADS) ]
    for t in threads:
        t.start()
    for t in threads:
        t.join() 

    hw = ""
    for i in range(NUMBER_OF_THREADS):
        hw += result[i].result
    return hw

def main():
    global BATCHES, BOUNDS, start, CURRENT_LI, EXPECTED_SEQ, ROUNDS, sk, B, ZEROES, BSAVE, SUM_ATTEMPTS

    # generate array of batches from PRIMES and BATCH_SIZES   
    # offset = 0
    # for j in range(len(BATCH_SIZES)):
    #     BATCHES.append([PRIMES[i] for i in range(offset, offset + BATCH_SIZES[j])])
    #     offset += BATCH_SIZES[j]
    
    if(len(BATCHES)!=len(BOUNDS)):
        print("number of batches != number of bounds!")
        quit(0)

    print("-----------------------------")
    print(ctime())
    count = 0
    timesum = 0
    start = time.time()	
    for k in range(0, len(ROUNDS)):
        end = time.time()
        print("Round " + str(k) + " : execution time (secs):",)
        print(end-start)
        timesum += end-start
        start = end
        for j in ROUNDS[k]:
            done = False
            for ell in BATCHES[j]:
                if(done):
                    break
                # else:
                #     print("current batch : ")
                #     print(j)
                if(ZEROES[PRIMES.index(ell)] == 0):
                    li = PRIMES.index(ell)    
                    CURRENT_LI = li
                    local_attempts = ATTEMPTS
                    noKeyP = noKeyM = True
                    while True:    
                        # print("sk[li] = " + str(sk[li]))
                        hw_minus = ""
                        hw_plus = ""
                        # print("count = " + str(count) + " with " + str(NUM_OF_ATTEMPTS[count]*local_attempts) + " attemps ...")                        
                        if(sk[li] <= 0):
                            # skip keygen+ in case of increasing num of attempts
                            if(noKeyP):
                                noKeyP = False
                                sk_minus = [x*-1 for x in sk]
                                param = KEYPLUS
                                # key gen plus
                                sk_minus[li] = sk_minus[li] + 1
                                param += ' '.join(str(x) for x in sk_minus)
                                cmd = KEYGEN + param   
                                # call key gen
                                # print("calling " + cmd)
                                # print("generating sk+ for count = " + str(count) + " ...")
                                os.popen(cmd).read()
                            # collect HW+
                            hw_plus = collectHW(count, "_plus", NUM_OF_ATTEMPTS[count] *local_attempts)
                        if(sk[li] >= 0):
                            # skip keygen- in case of increasing num of attempts
                            if(noKeyM):        
                                noKeyM = False           
                                sk_minus = [x*-1 for x in sk] 
                                param = KEYMINUS
                                # key gen minus
                                sk_minus[li] = sk_minus[li] - 1
                                param += ' '.join(str(x) for x in sk_minus)
                                cmd = KEYGEN + param   
                                # call key gen
                                # print("calling " + cmd)
                                # print("generating sk- for count = " + str(count) + " ...")
                                os.popen(cmd).read()
                            # collect HW-
                            hw_minus = collectHW(count, "_minus", NUM_OF_ATTEMPTS[count] *local_attempts)
                        noKey = False
                        sys.stdout.flush()

                        # start decision
                        ret = decision(sk, li, hw_plus, hw_minus)
                        if(B[li] == 0) and (ret != 0):
                            print("############################################### error")
                            print("at batch : " + str(j) + " and ell_i = " + str(li))
                            print("B[li] == 0 and (ret != 0)")
                            quit(0)                         
                        if(B[li] != 0) and (ret == 0):
                            print("############################################### increasing num of attempts")
                            local_attempts += 1
                            INCREASED[li] += 1
                            # quit(0)
                        else:
                            # expected case
                            if(ret != 0):
                                B[li] += -ret
                                sk[li] += ret
                                count += 1
                                # SEQUENCE.append(ell)
                                # print(SEQUENCE)
                                done = True
                                break
                            else:
                                # "remove" ell since = 0
                                # done = True
                                ZEROES[PRIMES.index(ell)] = 1
                                break
                    sys.stdout.flush()
        print("Sum of attempts : " + str(SUM_ATTEMPTS))
    print(INCREASED)
    print(BSAVE)
    print(B)
    print()
    print(str(check()) + "/" + str(len(B)) + " bits wrong")


    end = time.time()
    print("execution time (secs):",)
    print(timesum + end-start)


if __name__ == "__main__":
    main()