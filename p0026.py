
maxFrac = 0
maxN = 0

Top = 10000
for d in range(3, Top):
   for x in range(1, d + 1):
      if (10 ** x) % d == 1:
         if x > maxN:
            maxFrac = max(maxFrac, d)
            maxN = x
         break


print maxN
print maxFrac
