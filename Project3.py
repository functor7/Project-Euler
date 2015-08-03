# --Project Euler 3--
#What is the largest prime factor of the number 600851475143?


def Prime_Find(k,n):
	if k==n:
		return k

	a=1

	while n%k != 0:
		k=k+1

	while n&k**(a+1) == 0:
		a=a+1 

	if k**a==n:
		return k

	return Prime_Find(k+1,n/(k**a))


N=600851475143

print(Prime_Find(2,N))