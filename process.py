import numpy as np
import pandas as pd

a = pd.read_csv('./sword.csv')

f = np.array(a)

new = np.zeros(f.shape)

for i in range(16):
    for j in range(12):
        temp = int(f[i,j])
        new[15-i,j]=int(temp)
new = new.astype(int)
print(new)
print("\n")
print(f)
z = np.zeros((16,12))
fin = np.zeros((16,12))
num = 1

for num in range(6):
    for i in range(6):
        if(i==0 and num==0):
            fin = new
        else:
            if(i==0 and num!=0):
                fin = z
            else:
                if(i==num and num!=0):
                    fin = np.append(fin,new,axis=0)
                else:
                    fin = np.append(fin,z,axis=0)
    fin = np.reshape(fin,(1,1152))
    np.savetxt('./sword/'+str(num+1)+'.txt',fin,delimiter='',fmt='%i')

fin = np.reshape(fin,(1,1152))
np.savetxt('p.txt',fin,delimiter='',fmt='%i')
