# PHSX815_Project4
This repository contains all the code, images, and other important files related to the final project

This project contains code from:
My own repositories
https://en.wikipedia.org/wiki/Exponential_distribution

To run the code:
1. place Random.py in a folder, and specify its location in DataGen.py 
2. Run DataGen.py to generate some fake data. I used python3 DataGen.py -Nmeas 10000 -lamda 0.454545455 > data.txt
3. Run MinAnalysis2.py. I used python3 MinAnalysis2.py -input1 data.txt
  This should output the estimation on tau=1/lamda, as well as the error interval for tau. It should also output a histogram for the generated data.
