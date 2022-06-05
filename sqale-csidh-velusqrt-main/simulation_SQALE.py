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

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

HW_FILE = "hw"
NUMBER_OF_WORDS = 32
NUMBER_OF_CHARS = 4162
KEYPLUS = "88 "
KEYMINUS = "99 "
NOISE=1.8
NOISE_MAX = 10
THRESHOLD=1.8
NUMBER_OF_THREADS=1
FACTOR = 1
FACTOR_ARRAY = []

# using countermeasures ?
WITH_CM = False

# plot figures ?
PLOT = True

# number of bits to guess
N = 221

# calculated using torsion-prob-sqale-2048.py
NUM_OF_ATTEMPTS = [12, 14, 16, 17, 18, 19, 20, 20, 21, 22, 23, 23, 24, 24, 24, 25, 25, 26, 26, 26, 27, 27, 27, 27, 28, 28, 28, 28, 29, 29, 29, 29, 29, 30, 30, 30, 30, 30, 31, 31, 31, 31, 31, 31, 31, 32, 32, 32, 32, 32, 32, 32, 33, 33, 33, 33, 33, 33, 33, 33, 33, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]

# Bob's secret key for checking
B = [-1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, -1]

DF = './attack-2048-df.main '
WD2 = './attack-2048-wd2.main '
CM = './attack-2048-df-CM.main '

sk = [0] * len(B)
sk_minus = [0] * len(B)

class returnValue:
    def __init__(self):
        self.result = None

def check():
    wrong = 0
    for i in range(N):
        if(sk[i] != B[i]):
            wrong+=1
    return wrong

def plotSRtoSNR(li):
    # just plot precalculated values without/with CM
    justPlot = True
    plotCM = True

    if(justPlot):
        x = [430.00247531158, 108.68935455524964, 48.993034702490384, 26.336243088106894, 16.872253821117056, 11.725298372548147, 8.673022830690227, 6.617268130100988, 5.1854414237785065, 4.222751335070725, 3.5132306827650277, 2.957237303811203, 2.5112209069960194, 2.1867075593723344, 1.9214491670075426, 1.6596059520915263, 1.489803412631384, 1.3184760262127175, 1.1962150894712815, 1.0695438875556136, 0.9762247487028647, 0.9014566615082806, 0.8190337956658406, 0.7445473943356427, 0.678772586010979, 0.6406852063403232, 0.5812968344396925, 0.5623566884358433, 0.5054617960040517, 0.4729056710987051, 0.44341407883632156, 0.40626944085415456, 0.3979499298940857, 0.3681667877655744, 0.3482478787741615, 0.32969142555694814, 0.31551140171058883, 0.2953003929967889, 0.27675470027182314, 0.26912553148474605, 0.25406207679870335, 0.24352093818453469, 0.23364086293126918, 0.22217355109752546, 0.21008152918799908, 0.20435675764897993, 0.19259339358305672, 0.18578290108131937, 0.17926530059839493, 0.1704869633797687, 0.16848040181827764, 0.16017204431913276, 0.15112795326782966, 0.14954625940605226, 0.14010979709840532, 0.13788961699543117, 0.1309068909487433, 0.12634435201880753, 0.12285191688216265, 0.11666532630187568, 0.11520808918844035, 0.11130141977413215, 0.10771568653701981, 0.10576103408212364, 0.10183904869184585, 0.09972905283552755, 0.09580882775505255, 0.09062136593104383, 0.08891852518963174, 0.08963501965837521, 0.08403154869930023, 0.08187575752839792, 0.08101051266208356, 0.07634623330418522, 0.07513471143495165, 0.07347698889220708, 0.07249802570037922, 0.07107700098697217, 0.06919877300886933, 0.06710875930133461, 0.06453522140188632, 0.06460791380739753, 0.06207836115934306, 0.060852447057126134, 0.058970475236761286, 0.05793430089574185, 0.05480359514364162, 0.055072970032623396, 0.053305853625208725, 0.05331722862546081, 0.05209189551701248, 0.050943582622918045, 0.048711133517044924, 0.04799646970814792, 0.0475981901501235, 0.046338726148843795, 0.04572523572548971, 0.04454633134596715, 0.043383985493169665]

        if(plotCM):
            # with CM
            y = [0.45, 0.58, 0.49, 0.46, 0.53, 0.45, 0.52, 0.51, 0.49, 0.56, 0.55, 0.43, 0.47, 0.44, 0.48, 0.41, 0.53, 0.43, 0.52, 0.46, 0.47, 0.48, 0.49, 0.52, 0.58, 0.44, 0.51, 0.53, 0.38, 0.43, 0.46, 0.54, 0.43, 0.48, 0.56, 0.43, 0.46, 0.5, 0.6, 0.41, 0.46, 0.47, 0.57, 0.51, 0.37, 0.52, 0.47, 0.56, 0.55, 0.54, 0.47, 0.48, 0.54, 0.41, 0.44, 0.38, 0.51, 0.56, 0.55, 0.47, 0.49, 0.44, 0.43, 0.61, 0.48, 0.48, 0.44, 0.43, 0.4, 0.51, 0.53, 0.5, 0.48, 0.4, 0.49, 0.5, 0.47, 0.57, 0.5, 0.48, 0.48, 0.58, 0.48, 0.43, 0.46, 0.48, 0.52, 0.47, 0.57, 0.49, 0.49, 0.47, 0.51, 0.58, 0.51, 0.59, 0.47, 0.44, 0.53]
        else:
            # without CM    
            y = [1.0, 0.99, 0.99, 0.98, 1.0, 0.99, 1.0, 0.99, 0.97, 0.98, 0.99, 1.0, 1.0, 0.98, 0.99, 0.96, 0.99, 0.94, 0.98, 0.97, 0.96, 0.94, 0.96, 0.87, 0.91, 0.87, 0.88, 0.87, 0.81, 0.78, 0.82, 0.83, 0.74, 0.73, 0.69, 0.71, 0.72, 0.64, 0.68, 0.8, 0.6, 0.63, 0.76, 0.65, 0.58, 0.62, 0.65, 0.6, 0.58, 0.58, 0.66, 0.58, 0.48, 0.58, 0.54, 0.44, 0.53, 0.52, 0.58, 0.49, 0.49, 0.6, 0.44, 0.62, 0.45, 0.62, 0.53, 0.47, 0.49, 0.57, 0.58, 0.49, 0.6, 0.52, 0.54, 0.45, 0.56, 0.43, 0.47, 0.46, 0.53, 0.56, 0.54, 0.5, 0.6, 0.52, 0.53, 0.48, 0.41, 0.47, 0.47, 0.53, 0.49, 0.55, 0.57, 0.54, 0.54, 0.6, 0.58]


        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')          
        plt.gray()
        plt.rcParams.update({'font.size': 30})      
        plt.ylabel(r'Success rate',fontsize=50) 
        plt.axhline(y=0.5, color='r', linestyle='-')
        plt.xlabel(r'SNR',fontsize=50)    


        axes = plt.axes()

        ax = plt.gca()
        ax.invert_xaxis()    
        axes.yaxis.grid(True)  
        plt.xscale('log')
        plt.plot(x, y, marker="o",  markersize=10)

        plt.yticks(np.arange(0.4, 1.1, 0.1), ["0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"])     
        plt.show()
    else:
        history_runs=100

        np.hypoPlus=[]
        np.hypoMinus=[]
        np.hypoNoise=[]

        pos_count = 0
        count = 0

        sumPlus = 0
        sumMinus = 0

        np.history_snr1=[]
        np.history_snr2=[]
        np.history_snr3=[]
        np.history_snr4=[]        

        np.pos_count=[]
        np.minus_count=[]

        sk_minus = [x*-1 for x in sk]
        param = KEYPLUS
        # key gen plus
        sk_minus[li] = sk_minus[li] + 1
        param += ' '.join(str(x) for x in sk_minus)
        cmd = WD2 + param   
        # call key gen
        # print("calling " + cmd)
        # print("generating sk+ for l_i = " + str(li) + " ...")
        os.popen(cmd).read()
        
        sk_minus = [x*-1 for x in sk] 
        param = KEYMINUS
        # key gen minus
        sk_minus[li] = sk_minus[li] - 1
        param += ' '.join(str(x) for x in sk_minus)
        cmd = WD2 + param   
        # call key gen
        # print("calling " + cmd)
        # print("generating sk- for l_i = " + str(li) + " ...")
        os.popen(cmd).read()    

        for i in range(1, history_runs):
            
            
            np.snr1=[]
            np.snr2=[]
            np.snr3=[]
            np.snr4=[]

            # print(i)
            sys.stdout.flush()
            std_noise= i*(NOISE_MAX/history_runs)
            print('Noise')
            print(std_noise)
            num_runs = 100
            pos_count = 0
            count = 0

            for _ in range(num_runs):

                hw_minus = collectHW(li, "_minus", True)
                hw_plus = collectHW(li, "_plus", True)

                hw_plus = hw_plus[:-1].split(":")
                hw_minus = hw_minus[:-1].split(":")

                sumPlus = 0
                sumMinus = 0

                for i in range(0, len(hw_plus), 2):
                    
                    np.plusX=[]
                    np.plusZ=[]
                    np.minusX=[]
                    np.minusZ=[]

                    for j in range(0, 31, 1):
                        np.plusX.append(hw_plus[i][j*16:(j+1)*16].count('1'))
                        np.minusX.append(hw_minus[i][j*16:(j+1)*16].count('1'))
                    i+=1
                    for j in range(0, 31, 1):
                        np.plusZ.append(hw_plus[i][j*16:(j+1)*16].count('1'))
                        np.minusZ.append(hw_minus[i][j*16:(j+1)*16].count('1'))

                    noisepXn=np.random.normal(0,std_noise,len(np.plusX))
                    np.plusXn= np.plusX + (noisepXn)

                    noisepZn=np.random.normal(0,std_noise,len(np.plusZ))
                    np.plusZn= np.plusZ + (noisepZn)       
                    
                    noisemXn=np.random.normal(0,std_noise,len(np.minusX))
                    np.minusXn= np.minusX + (noisemXn)

                    noisemZn=np.random.normal(0,std_noise,len(np.minusZ))
                    np.minusZn= np.minusZ + (noisemZn)
                    # np.noiseX = np.minusXn + (np.random.normal(0,np.sqrt(16),len(np.minusXn)))
                    # np.noiseZ = np.minusZn + (np.random.normal(0,np.sqrt(16),len(np.minusZn))) 

                    np.hypoPlus.append(abs(np.corrcoef(np.plusXn,np.plusZn)[1,0]))
                    np.hypoMinus.append(abs(np.corrcoef(np.minusXn,np.minusZn)[1,0]))
                    # np.hypoNoise.append(abs(np.corrcoef(np.noiseX,np.noiseZ)[1,0]))             

                    sumPlus += np.hypoPlus[len(np.hypoPlus)-1]
                    sumMinus += np.hypoMinus[len(np.hypoMinus)-1]                      

                    np.snr1.append((np.var(np.plusX)/np.var((noisepXn))))

                count += 1
                if(sumPlus > sumMinus):
                    pos_count += 1
                
            np.history_snr2.append(np.mean(np.snr1))
            np.history_snr1.append(pos_count/count)

        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')          
        plt.gray()
        plt.rcParams.update({'font.size': 30})      
        plt.ylabel(r'Success rate',fontsize=50) 
        plt.axhline(y=0.5, color='r', linestyle='-')
        plt.xlabel(r'SNR',fontsize=50)    
        plt.yticks(np.arange(0, 1.1, 0.1), ["0.0", "0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"]) 


        axes = plt.axes()
        ax = plt.gca()
        ax.invert_xaxis()    

        axes.yaxis.grid(True)  
        plt.xscale('log')

        plt.plot(np.history_snr2, np.history_snr1, marker="o",  markersize=10)

        plt.show()




def plotFig1(li):

    history_runs=100

    np.hypoPlus=[]
    np.hypoMinus=[]
    np.hypoNoise=[]

    np.history_snr1=[]
    np.history_snr2=[]
    np.history_snr3=[]
    np.history_snr4=[]        



    for i in range(1, history_runs):
        
        
        np.snr1=[]
        np.snr2=[]
        np.snr3=[]
        np.snr4=[]

        # print(i)
        sys.stdout.flush()
        std_noise= i*(NOISE_MAX/history_runs)
        print('Noise')
        print(std_noise)
        num_runs = 10

        for _ in range(num_runs):

            hw_minus = collectHW(li, "_minus", False)
            hw_plus = collectHW(li, "_plus", False)

            hw_plus = hw_plus[:-1].split(":")
            hw_minus = hw_minus[:-1].split(":")

            for i in range(0, len(hw_plus), 2):

                np.plusX=[]
                np.plusZ=[]
                np.minusX=[]
                np.minusZ=[]

                for j in range(0, 31, 1):
                    np.plusX.append(hw_plus[i][j*16:(j+1)*16].count('1'))
                    np.minusX.append(hw_minus[i][j*16:(j+1)*16].count('1'))
                i+=1
                for j in range(0, 31, 1):
                    np.plusZ.append(hw_plus[i][j*16:(j+1)*16].count('1'))
                    np.minusZ.append(hw_minus[i][j*16:(j+1)*16].count('1'))

                noisepXn=np.random.normal(0,std_noise,len(np.plusX))
                np.plusXn= np.plusX + (noisepXn)

                noisepZn=np.random.normal(0,std_noise,len(np.plusZ))
                np.plusZn= np.plusZ + (noisepZn)       
                
                noisemXn=np.random.normal(0,std_noise,len(np.minusX))
                np.minusXn= np.minusX + (noisemXn)

                noisemZn=np.random.normal(0,std_noise,len(np.minusZ))
                np.minusZn= np.minusZ + (noisemZn)

                np.hypoPlus.append(abs(np.corrcoef(np.plusXn,np.plusZn)[1,0]))
                np.hypoMinus.append(abs(np.corrcoef(np.minusXn,np.minusZn)[1,0]))

                np.snr1.append((np.var(np.plusX)/np.var((noisepXn))))
                np.snr2.append((np.var(np.plusZ)/np.var((noisepZn))))
                np.snr3.append((np.var(np.minusX)/np.var((noisemXn))))
                np.snr4.append((np.var(np.minusZ)/np.var((noisemZn))))
        
        np.history_snr1.append(np.mean(np.snr1))
        np.history_snr2.append(np.mean(np.snr2))
        np.history_snr3.append(np.mean(np.snr3))
        np.history_snr4.append(np.mean(np.snr4))
            

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')          
    plt.gray()
    plt.rcParams.update({'font.size': 30})      
    plt.ylabel(r'SNR',fontsize=50) 
    plt.xlabel(r'SND',fontsize=50)    
    plt.xticks(np.arange(0, 100, 10), ['0', '1.0', '2.0', '3.0', '4.0', '5.0', '6.0', '7.0', '8.0', '9.0']) 


    axes = plt.axes()
    axes.yaxis.grid(True)  
    plt.yscale('log')
  
    plt.plot(np.history_snr1,'-', label=r'2C',linewidth=2.0)
    plt.plot(np.history_snr2, '--', label=r'4C',linewidth=3.0)
    plt.plot(np.history_snr3, '-.', label=r'A + 2C',linewidth=4.0)
    # plt.plot(np.history_snr4, label='[- X]') 
    plt.legend()
    plt.savefig('SNR',dpi=300)
    plt.show()


def plotCorrelationFig(withNoise, li, hw_plus, hw_minus):
    np.hypoPlus=[]
    np.hypoMinus=[]

    hw_plus = hw_plus[:-1].split(":")
    hw_minus = hw_minus[:-1].split(":")

    pos_count = 0
    neg_count = 0
    count = 0
    for i in range(0, len(hw_plus), 2):

        np.plusX=[]
        np.plusZ=[]
        np.minusX=[]
        np.minusZ=[]
        np.noiseX=[]
        np.noiseZ=[]

        for j in range(0, 31, 1):
            np.plusX.append(hw_plus[i][j*16:(j+1)*16].count('1'))
            np.minusX.append(hw_minus[i][j*16:(j+1)*16].count('1'))
        i+=1
        for j in range(0, 31, 1):
            np.plusZ.append(hw_plus[i][j*16:(j+1)*16].count('1'))
            np.minusZ.append(hw_minus[i][j*16:(j+1)*16].count('1'))

        # generate noise
        noisepXn=np.random.normal(0,NOISE,len(np.plusX))
        noisepZn=np.random.normal(0,NOISE,len(np.plusZ))       
        noisemXn=np.random.normal(0,NOISE,len(np.minusX))
        noisemZn=np.random.normal(0,NOISE,len(np.minusZ))

        if(withNoise):
            np.plusXn= np.plusX + (noisepXn)
            np.plusZn= np.plusZ + (noisepZn)
            np.minusXn= np.minusX + (noisemXn)
            np.minusZn= np.minusZ + (noisemZn)
        else:
            np.plusXn= np.plusX
            np.plusZn= np.plusZ 
            np.minusXn= np.minusX 
            np.minusZn= np.minusZ


        np.hypoPlus.append(abs(np.corrcoef(np.plusXn,np.plusZn)[1,0]))
        np.hypoMinus.append(abs(np.corrcoef(np.minusXn,np.minusZn)[1,0]))
         
        if (np.hypoPlus[len(np.hypoPlus)-1] - np.hypoMinus[len(np.hypoMinus)-1]) >0:
            pos_count+=1
        else:
            neg_count+=1

    print("success rate")
    print(pos_count/(len(hw_plus)/2))

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')            
    plt.gray()
    plt.rcParams.update({'font.size': 30})
    plt.ylabel(r'Correlation',fontsize=50)
    plt.xlabel(r'Measurements',fontsize=50)
    plt.xticks(np.arange(0, NUM_OF_ATTEMPTS[li]+1, 50)) 
    axes = plt.axes()
    axes.set_ylim([0, 1])
    axes.yaxis.grid(True)
        

    plt.rc('text.latex', preamble=r'\usepackage{amsmath} \usepackage{amssymb}')

    plt.plot(np.hypoPlus, '-', label=r'$\mathfrak{l} \ast E_{-v}$',linewidth=2.0) 
    plt.plot(np.hypoMinus, '--', label=r'$\mathfrak{l}^{-1} \ast E_{-v}$',linewidth=3.0)         
    
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)   
    leg = plt.legend()
    plt.legend(loc='upper right')

    leg_lines = leg.get_lines()
    leg_texts = leg.get_texts()
    plt.setp(leg_lines, linewidth=2)
    plt.setp(leg_texts, fontsize=30)

    plt.show()    

def decision_corr(sk, li, hw_plus, hw_minus, withNoise):
    global THRESHOLD, FACTOR
    np.hypoPlus=[]
    np.hypoMinus=[]
    np.hypoNoise=[]

    pos_count = 0
    neg_count = 0
    count = 0

    sumPlus = []
    sumMinus = []

    print("sk[i] = " + str(B[li]))

    hw_plus = hw_plus[:-1].split(":")
    hw_minus = hw_minus[:-1].split(":")
    for i in range(0, len(hw_plus), 2):

        np.plusX=[]
        np.plusZ=[]
        np.minusX=[]
        np.minusZ=[]
        np.noiseX=[]
        np.noiseZ=[]


        for j in range(0, 31, 1):
            np.plusX.append(hw_plus[i][j*16:(j+1)*16].count('1'))
            np.minusX.append(hw_minus[i][j*16:(j+1)*16].count('1'))
        i+=1
        for j in range(0, 31, 1):
            np.plusZ.append(hw_plus[i][j*16:(j+1)*16].count('1'))
            np.minusZ.append(hw_minus[i][j*16:(j+1)*16].count('1'))

        noisepXn=np.random.normal(0,NOISE,len(np.plusX))
        noisepZn=np.random.normal(0,NOISE,len(np.plusZ))
        noisemXn=np.random.normal(0,NOISE,len(np.minusX))
        noisemZn=np.random.normal(0,NOISE,len(np.minusZ))

        if(withNoise):
            np.plusXn= np.plusX + (noisepXn)
            np.plusZn= np.plusZ + (noisepZn)
            np.minusXn= np.minusX + (noisemXn)
            np.minusZn= np.minusZ + (noisemZn)
        else:
            np.plusXn= np.plusX
            np.plusZn= np.plusZ 
            np.minusXn= np.minusX 
            np.minusZn= np.minusZ


        np.hypoPlus.append(abs(np.corrcoef(np.plusXn,np.plusZn)[1,0]))
        np.hypoMinus.append(abs(np.corrcoef(np.minusXn,np.minusZn)[1,0]))
        # np.hypoNoise.append(abs(np.corrcoef(np.noiseX,np.noiseZ)[1,0]))             

        sumPlus += np.hypoPlus[count]
        sumMinus += np.hypoMinus[count]

        if (np.hypoPlus[count] - np.hypoMinus[count]) >0:
            pos_count+=1
        else:
            neg_count+=1
        count += 1


    if(sumPlus < sumMinus):
        print("guessing: +1")
        sk[li] = 1
    else:
        print("guessing: -1")
        sk[li] = -1

    # cheating during wip phase
    if(sk[li] != B[li]):
        print("------------->>>WRONG!!!")
        sk[li] = 0
        # print("threshold = " + str(THRESHOLD))
        return False
        # quit()
    else:
        FACTOR_ARRAY.append(FACTOR)
    return True

    
def startDF(cmd, num_of_attempts, result):
    result.result = ""
    for _ in range(num_of_attempts):
        callHW = ""
        while(callHW == ""):
            callHW = os.popen(cmd).read()
            split = callHW[:-1].split("\n")
            # if(split[0]!='3, '):
            #     callHW = ""
        # print(split[1])
        result.result += split[1] + ":"

def collectHW(li, type, withCM):
    global NUMBER_OF_THREADS, FACTOR
    if(type ==  "_plus"):
        param = KEYPLUS
        # print("PLUS")
    if(type ==  "_minus"):
        param = KEYMINUS   
        # print("MINUS")
    # 1st param := which li to attack
    param += str(li)
    # 2nd param := how many attemmpts
    # param += str(NUM_OF_ATTEMPTS[li]) + " "
    if(withCM):
        cmd = CM + param
    else:
        cmd = DF + param
    # print("calling " + cmd)
    # print("collecting hamming weights " + str(NUM_OF_ATTEMPTS[li]) + "x ...")
    threads = []
    
    attemptsT = math.ceil((NUM_OF_ATTEMPTS[li]*FACTOR)/NUMBER_OF_THREADS)
    
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

def attack(withNoise, withCM):
    global FACTOR
    for li in range(0, N):
        FACTOR = 3
        print("attacking ell_i = " + str(li) + " with " + str(NUM_OF_ATTEMPTS[li]*FACTOR) + " attempts")
        ret = False

        while(ret != True):
            # print("l_i = " + str(li) + " with " + str(NUM_OF_ATTEMPTS[li]) + " attemps ...")
            sk_minus = [x*-1 for x in sk]
            param = KEYPLUS
            # key gen plus
            sk_minus[li] = sk_minus[li] + 1
            param += ' '.join(str(x) for x in sk_minus)
            cmd = WD2 + param   
            # call key gen
            # print("calling " + cmd)
            # print("generating sk+ for l_i = " + str(li) + " ...")
            os.popen(cmd).read()
            # collect HW+
            hw_plus = collectHW(li, "_plus", withCM)
            
            sk_minus = [x*-1 for x in sk] 
            param = KEYMINUS
            # key gen minus
            sk_minus[li] = sk_minus[li] - 1
            param += ' '.join(str(x) for x in sk_minus)
            cmd = WD2 + param   
            # call key gen
            # print("calling " + cmd)
            # print("generating sk- for l_i = " + str(li) + " ...")
            os.popen(cmd).read()
            # collect HW-
            hw_minus = collectHW(li, "_minus", withCM)

            ret = decision_corr(sk, li, hw_plus, hw_minus, withNoise)
            FACTOR = FACTOR + 1
    print("FACTOR_ARRAY")
    print(FACTOR_ARRAY)

def plotFigs(count, withCM):
    for li in range(0, N):
        print("collecting HW for ell_i = " + str(li) + " with " + str(NUM_OF_ATTEMPTS[li]) + " attempts")
        ret = False
        FACTOR = 1
        sys.stdout.flush()
        while(ret != True):
            # print("l_i = " + str(li) + " with " + str(NUM_OF_ATTEMPTS[li]) + " attemps ...")
            sk_minus = [x*-1 for x in sk]
            param = KEYPLUS
            # key gen plus
            sk_minus[li] = sk_minus[li] + 1
            param += ' '.join(str(x) for x in sk_minus)
            cmd = WD2 + param   
            # call key gen
            # print("calling " + cmd)
            # print("generating sk+ for l_i = " + str(li) + " ...")
            os.popen(cmd).read()
            # collect HW+
            hw_plus = collectHW(li, "_plus", withCM)
            
            sk_minus = [x*-1 for x in sk] 
            param = KEYMINUS
            # key gen minus
            sk_minus[li] = sk_minus[li] - 1
            param += ' '.join(str(x) for x in sk_minus)
            cmd = WD2 + param   
            # call key gen
            # print("calling " + cmd)
            # print("generating sk- for l_i = " + str(li) + " ...")
            os.popen(cmd).read()
            # collect HW-
            hw_minus = collectHW(li, "_minus", withCM)

            if(count==li):
                # plot correlation without noise
                plotCorrelationFig(False, li, hw_plus, hw_minus)

                # plot correlation with noise
                plotCorrelationFig(True, li, hw_plus, hw_minus)
                return

def main():
    print("-----------------------------")
    print("starting attacking simulation for SQALE-2048 with " + str(NUMBER_OF_THREADS) + " threads.")
    print(ctime())
    start = time.time()	

    # starting simulation of full key recovery with noise without countermeasures
    attack(True, False)

    # starting simulation of full key recovery with noise with countermeasures
    # attack(True, True)
    
    end = time.time()
    print("execution time (secs):",)
    print(end-start)

    print()
    print(str(check()) + "/" + str(N) + " bits wrong")


    if(PLOT):
        # plot figures at aimed ell_i without countermeasures
        plotFigs(0, False)
        # plot figures at aimed ell_i with countermeasures 
        # plotFigs(0, True)
        plotFig1(0)        
        plotSRtoSNR(0)



if __name__ == "__main__":
    main()
