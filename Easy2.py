a=input()
v="aeiou"
c=0
for ch in a.lower():
    if ch in v:
        c=c+1
print(c)

