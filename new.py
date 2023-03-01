array1=[4,8,6,5,6,8]
n=len(array1)

for i in range(0,n):
     for j in range(i+1,n):
         if(array1[i]>array1[j]):
             temp=array1[i]
             array1[i]=array1[j]
             array1[j]=temp

