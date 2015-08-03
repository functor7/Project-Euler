# --Project Euler 1--
#If we list all the natural numbers below 10 that are multiples of 3 or 5, 
#we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
#Find the sum of all the multiples of 3 or 5 below 1000.

i=1
s=0

while 5*i<1000:
	s=s+5*i
	i=i+1

i=1

while 3*i<1000:
	if i%5 != 0:
		s=s+3*i
	i=i+1

print(s)
#Alternatively

a=int(1000/3)
b=int((1000/5))-1
c=int(1000/15)

print(int(3*(a*(a+1)/2)+5*(b*(b+1)/2)-15*(c*(c+1)/2)))

#In General: A list L of numbers. First, eleminate any term that is a
#multiple of another on the list.append Then for k=1 to the size of the list
#find the sum of all numbers less than V that divide some k-tuble on the list.


#Euclidean Algorithm that keeps track of all remainders and divisors
def euc(a,b):
        if a%b==0:
                
                return [[0], [int(a/b)]]

        r=a%b
        E=euc(b,r)

        return [[r]+E[0], [int(a/b)]+E[1]]
     
#Find the LCM via the GCD
def lcm(L):
        if len(L)==1:
                return L[0]
        a=L.pop()
        b=lcm(L)

        return int(a*b/(euc(a,b)[0][-2]))

#Outputs a list of all possible ways to choose k numbers out of the first n
def list_n_choose_k(n,k):
        if k==0:
                return [[]]
        if n<k:
                return []
        L=list_n_choose_k(n-1,k-1)
        i=0
        while i<len(L):
                L[i]=L[i]+[n]
                i=i+1
        return list_n_choose_k(n-1,k)+L

#Find the sum of all numbers less than N that are multiples of :
def sum_of_multiples(N,L):
        if N%L==0:
                a=int(N/L)-1
                return int(L*(a*(a+1)/2))

        a=int(N/L)
        return int(L*(a*(a+1)/2))
        

#for all k-tuples, find the lcm and then add up all the numbers less than N
#that are multiples of this lcm.
def sum_k_tuples(L,k,N):

        n=len(L)
        c=list_n_choose_k(n,k)
        M=[]
        S=0
        
        for p in c:
                for i in p:
                        M=M+[L[i-1]]
                                        
                
                S=S+sum_of_multiples(N,lcm(M))
                M=[]
        return S

#Find the sum of everything that is a multiple of anything on the list and less
#than N
def sum_inc_exc(L,N):
        n=len(L)
        k=1
        S=0

        while k<=n:
                S=S+sum_k_tuples(L,k,N)*(-1)**(k+1)
                k=k+1

        return S


print(sum_inc_exc([2,3,5],31))
        
        















        
        
        

