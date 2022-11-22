z = input()
from collections import Counter

a = Counter(z)
if a['z']*2 == a['o']:
    print("Yes")
elif a['z']*11 == a['o']:
    print("Maybe")
else:
    print("No")
