import time
import numpy as np
import math
import cmath
import cv2



dt=0.05
df=0.05


def myRange(start,end,step):
    i = start
    while i < end:
        yield i
        i += step
    yield end

t1=[]
for i in myRange(0,(10-dt),(dt)):
    t1.append(round(i, 2))

t2=[]
for i in myRange(10,(20-dt),(dt)):
    t2.append(round(i, 2))

t3=[]
for i in myRange(20,30,(dt)):
    t3.append(round(i, 2))

t=[]
for i in myRange(0,30,(dt)):
    t.append(round(i, 2))

f=[]
for i in myRange(-5,4.9999,(df)):
    f.append(round(i, 2))


x=[]
for i in range(len(t1)):
	x.append(math.cos(2*math.pi*t1[i]))

for i in range(len(t2)):
	x.append(math.cos(6*math.pi*t2[i]))

for i in range(len(t3)):
	x.append(math.cos(4*math.pi*t3[i]))
###########################################################

def recSTFT(x,t,f,B):
	
	dt=0.05
	df=0.05

	nn=len(t)
	mm=len(f)

	Q=int(B/dt)
	N=int(1/(dt*df))

	immm=np.zeros((nn,mm), dtype=np.uint8)

	mag=400
	#####################################################

	for p in range(nn):
		
		n=int(t[p]/dt)
		for d in range(mm):
			
			#?
			m=int((f[d]/df))

			ss=dt*cmath.exp(1j*2*math.pi*(Q-n)*m/N)
			
			m=int((f[d]/df)%N)
			######################################3
			summ=0
			#############################################
			for q in range((2*Q+1)):

				
				##########################
				
				if abs((Q-q)*dt)<B:
				######################
					k=n-Q+q
					#?
					if (k>-1) and (k<nn):
						xq=x[k]
						summ+=xq*cmath.exp(-1j*2*math.pi*q*m/N)

			#############################################################
			#?
			immm[p,d]=abs(ss*summ)*mag

			###############################################

	return immm.transpose()






################################
B=0.5
start=time.time()
see=recSTFT(x,t,f,B)
end=time.time()
diff=end-start

print('calculated time is:')
print(diff)
print('secs')
cv2.imshow('result', see)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
