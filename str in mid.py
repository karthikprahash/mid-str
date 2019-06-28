# mid-str
i=input()
s=int((len(i)-1)/2)
if len(i)%2!=0:
    print(i[0:s]+'*'+i[s+1:])
else:
    print(i[0:s]+'**'+i[s+2:])
