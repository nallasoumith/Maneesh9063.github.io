import pprint as p

l,a = [],{}

with open(r'C:\Users\soumith\Desktop\1.txt','r') as f :
    initial = f.readlines()
    s = initial[10:35]
    for j,i in enumerate(s):
       
        l.append( i.split('=')[0].strip().swapcase().replace('_','-'))
        s[j] = i.split('=')[-1].strip()

        a[l[j]] = s[j]

b,c = [],{}

with open(r'C:\Users\soumith\Desktop\2.txt','r') as f :
    out = f.readlines()
    out = out[6:32] + out[34:52]
    for j,i in enumerate(out):
        b.append(i.split(':'))
        b[j][0] = b[j][0].strip().replace("'","")[:-1]
        b[j][1] = b[j][1].strip().replace("'","")[:-1]

        c[b[j][0]] = b[j][1]


for i in b:
    try:
        i[1] = a[i[0]]
    except:
        pass
s = ''
for i in b:
    s += "{'"+i[0]+"':'"+i[1].replace("'","")+"'},\n"

print(s[:-2])

