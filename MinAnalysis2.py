from scipy.optimize import minimize as min
from scipy.optimize import fsolve
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
from Random.Random import Random
import sys


#takes a .txt file, reads it, and makes a list
if __name__ == "__main__":
   
    haveH1=False
    myArray1=[]

    if '-input1' in sys.argv:
        p = sys.argv.index('-input1')
        InputFile1 = sys.argv[p+1]
        haveH1 = True

    if haveH1:
        with open(InputFile1, "r") as f:
            myArray1 = f.read().split()

        for i in range(0, len(myArray1)):
            myArray1[i] = float(myArray1[i])

    

#defining a 1D function, which we what to minimize
    def f(T):
        
        res=0
        
        
        for i in myArray1:
            
            L=np.log(T)+(1/T)*i

            res+=L
            
        
            
        return np.round(res,8)
            
            

    #a starting guess for location of minimum
    x_start=2.2
    #result of minimization
    result=min(f, x_start)

    if result.success:
        print("the minimum is at:")
        print((result.x))

    else:
        print("could not find minimum")
        print(result.message)

    #estimating error on estimated sigx using log(L(sigx)/L(sigx_best))<=-0.5

    def g(T):
        p=-f(T)+f(result.x)+0.5
        return p
    

    tauerr_guess=(1.8,2.6)
    tau_err=fsolve(g,tauerr_guess)
    print("error bounds are:")
    print(tau_err)
    
    #Plots distribution in histogram
    
    if haveH1:
        n, bins, patches = plt.hist(myArray1, 50, facecolor='green', alpha=0.50)

    plt.ylabel('Number of Events')
    plt.xlabel('Time Difference in μs')
    plt.title('Time Difference Between Stop and Start Times Recorded by Scintillator')
    plt.grid(True)


    

            

    plt.show()
