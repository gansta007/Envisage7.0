import numpy as np

f1 = np.zeros((16,12,6))
f2 = np.zeros((16,12,6))
f3 = np.zeros((16,12,6))
f4 = np.zeros((16,12,6))
f5 = np.zeros((16,12,6))
f6 = np.zeros((16,12,6))
f7 = np.zeros((16,12,6))
f8 = np.zeros((16,12,6))

f1[:,6,5]=1
f1[:,6,4]=1
f1[:,6,3]=1

f2[:,8,5]=1
f2[:,7,4]=1
f2[:,6,3]=1

f3[:,6,3]=1
f3[:,7,3]=1
f3[:,8,3]=1

f4[:,6,3]=1
f4[:,7,2]=1
f4[:,8,1]=1

f5[:,6,3]=1
f5[:,6,2]=1
f5[:,6,1]=1

f6[:,6,3]=1
f6[:,5,2]=1
f6[:,4,1]=1

f7[:,6,3]=1
f7[:,5,3]=1
f7[:,4,3]=1

f8[:,6,3]=1
f8[:,5,4]=1
f8[:,4,5]=1

ftemp = np.zeros((8,16,12,6))


for i in range(16):
    ftemp[0,15-i,:,:]=f1[i,:,:]
    ftemp[1,15-i,:,:]=f2[i,:,:]
    ftemp[2,15-i,:,:]=f3[i,:,:]
    ftemp[3,15-i,:,:]=f4[i,:,:]
    ftemp[4,15-i,:,:]=f5[i,:,:]
    ftemp[5,15-i,:,:]=f6[i,:,:]
    ftemp[6,15-i,:,:]=f7[i,:,:]
    ftemp[7,15-i,:,:]=f8[i,:,:]

fin = np.reshape(ftemp,(8,1152))
np.savetxt('./rotation.txt',fin,delimiter='',fmt='%i')

ftemp = ftemp.astype(int)
