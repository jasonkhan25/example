import matplotlib.pyplot as plt
limt =[840,700,2,44,343,343,434]
tm=[1,2,3,4,5,6,7]
B = [0.2,0.3,0.1 ,0.4,0.3,0.3,0.3]
PNA= [0.25,0.44,0.6,0.5,0.70,0.3,0.9]
PR = [0.8 ,0.9,0,8,0.3,0.5,0.6,0.8]

per=[60,40,30,80,20,40,70]
no_of_users=[1000,700,2000,500,800,300,2000]

lamT=[]
lamC=[]
LamdaR=[]

for a in range(0,7):
    a+=0
    limr= (limt[a]*(B[a]+(1-B[a])*PNA[a])*PR[a])
    
    LamdaC=((no_of_users[a])/100)*per[a]
    
   
    LamdaR.append(limr)
    
    lamC.append(LamdaC)
    LamdaT=LamdaR[a]+limt[a]
    lamT.append(LamdaT)
    
print(lamT)
print(LamdaR)
print(lamC)

plt.subplot(3,1,1)
plt.plot(tm, LamdaR,"ob--",color='r')
plt.xlabel('Time (hr)')
plt.ylabel('call repeat')
plt.title("Call Rpeat Lamda(R)")

plt.subplot(3,1,2)
plt.plot(tm,lamT,"ob--",color='g')
plt.xlabel("Time(hr)")
plt.ylabel("Total Arrival Rate")
plt.title("Total Arrival Rate Lamda(T)")

plt.subplot(3,1,3)
plt.plot(tm,lamC,"ob--",color='orange')
plt.xlabel("Time(hr)")
plt.ylabel("Users in per Hour")
plt.title("Users in per Hour Lamda(C)")