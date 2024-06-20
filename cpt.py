'''#file handling
file=open("datta.txt",'r')
print(file.read())

#2
path=r"harsha.txt"
file=open(path,'w')
for i in range(1,11):
    for j in range(10-i):
        file.write(' ')
    for j in range(i):
        file.write('*')
    file.write('\n')
file.close()

#3
path=r'vij.txt'
file=open(path,'w')
ls=[1,2,3,4,5]
s=''
for i in ls:
    s=s+str(i)+''
print(s)
file.write(s)
file.close()


#4
path=r"key.txt"
file=open(path,'w')
d={'key1':'val1','key2':'val2'}
s=''
for i in d.keys():
    s+=i+''+d[i]+'\n'   
file.write(s)
file.close()


#5

path=r"key.txt"
file=open(path,'r')
lines=file.readlines()
d={}
for line in lines:
    s=line.strip().split()
    d[s[0]]=s[1]
print(d)
file.close()

#6
import os
file=r'phani'
#checking the file existing
if os.path.exists(file):
    print('file is existing')
else:
    print('file is not existing')

#removeing file
os.remove(file)
#other method to remove file
#os,rmdir(file)

'''
#7
n=int(input('enter the number'))
if n>=0:
    print('yes !!! A NON-NEGATIVE NUMBER')
else:
    raise Exception('NO NEGATIVE NUMBER IS  ALLOWED')

    



