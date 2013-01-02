

n = 100

sum_sqn = 0
sum_n = 0
for i in range(1,n+1,1):
	sum_sqn += i**2
	sum_n += i

diff = sum_n**2 - sum_sqn
print diff

