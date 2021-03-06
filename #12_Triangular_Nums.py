#Euler Project #:Triangular_Numbers
"""
The sequence of triangle numbers is generated by adding the natural numbers. 
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first 
ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""


trinums=[1,3,6];


def get_trinum(x):
    n=x;
    trinum=0;
    while n>0:
        trinum+=n;
        n-=1;
    #print(trinum);
    return trinum;
    
def assemble_trinums(num):
    p=4;
    while p<num:
        trinums.append(get_trinum(p));
        p+=1;
    return trinums;
    
b=assemble_trinums(13001);
#print(b);


def get_num_factors(x):
    factors=[];
    for i in range (1,x+1):
        if x%i==0:
            if i not in factors:
                factors.append(i);
    return len(factors);

k=12000;
while k<13001:
    print("trinum with index",k,"has",get_num_factors(b[k]),"factors");
    k+=1;
print("done");




 
"""
#get_num_factors(100) --> 9

numfactoftrinums=[];
for elem in range (0,len(trinums)):
    numfactoftrinums.append(get_num_factors(trinums[elem]));
    if elem%100==0:
        print("now calculating number of factors for the element of trinums with index ",elem,".");
print(numfactoftrinums);
"""

"""
#already did up through 10000, then kept trying chunks at a time from there, slow going...
for z in range (15000,20000):
    print(get_num_factors(trinums[z]));
    if get_num_factors(trinums[z])>=499:
        print ("found it! ",trinums[z]);
    if z%100==0:
        print ("now trying element# "+str(z));
""" 

"""
********
trinum with index 12374 has 576 factors, this is the number 76576500 CORRECT
********
"""



    