kg=lambda tonns: tonns * 1000  

gm=lambda tonns: tonns * 1e6

mlgm=lambda tonns: tonns * 1e9

pound=lambda tonns: tonns * 2204.62


n=int(input("Enter the value in tonns: "))

list1=[kg(n),gm(n),mlgm(n),pound(n)]
list2=["kg","gm","mlgm","pound"]

for i in list1,list2:
    print(n,"tonns = ",i,sep=" ")