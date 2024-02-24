import math
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np

def myRange(start,end,step):
    i = start
    while i < end:
        yield i
        i += step
    yield end


dt=0.01
threshold=0.2
##################
t=[]
for tt in myRange(0,10,dt):
    t.append(tt)

x=[]

for i in range(len(t)):
	tim=t[i]
	temp=0.2*tim+math.cos(2*math.pi*tim)+0.4*math.cos(10*math.pi*tim)
	x.append(temp)

################################################
def hht(xx,tt,thr):
	################################
	K=10
	N=10
	#################################
	n=0
	y=xx

	c0flag=True
	Cs=[]

	######################################
	######################################

	while (n<N) and c0flag:
		###############################
		k=0
		hkflag=True
		c0flag=False

		while (k<K) and hkflag:
			############################
			hkflag=False
			maxys=[]
			maxts=[]

			minys=[]
			mints=[]
			#######################
			#######################################
			for i in range(1,len(y)-1):
				if (y[i]>y[i-1]) and (y[i]>y[i+1]):
					maxys.append(y[i])
					maxts.append(tt[i])
				elif (y[i]<y[i-1]) and (y[i]<y[i+1]):
					minys.append(y[i])
					mints.append(tt[i])
			###########################

			####################################
			peaks=interp1d(maxts,maxys,kind='cubic',fill_value='extrapolate')
			ypeaks =peaks(tt)

			dips=interp1d(mints,minys,kind='cubic',fill_value='extrapolate')
			ydips=dips(tt)
			###############################
			z=[]
			hk=[]
			for i in range(len(tt)):
				temp=(ypeaks[i]+ydips[i])/2
				z.append(temp)
				temp2=y[i]-temp
				hk.append(temp2)
			################################
			#check whether ht is IMF
			hmaxys=[]
			hmaxts=[]

			hminys=[]
			hmints=[]

			for i in range(1,len(tt)-1):
				if (hk[i]>hk[i-1]) and (hk[i]>hk[i+1]):
					hmaxys.append(hk[i])
					hmaxts.append(tt[i])

					if hk[i]<0:
						hkflag=True
				elif (hk[i]<hk[i-1]) and (hk[i]<hk[i+1]):
					hminys.append(hk[i])
					hmints.append(tt[i])

					if hk[i]>0:
						hkflag=True
			
			################################################
			u1=interp1d(hmaxts,hmaxys,kind='cubic',fill_value='extrapolate')
			yu1 =u1(tt)

			u0=interp1d(hmints,hminys,kind='cubic',fill_value='extrapolate')
			yu0=u0(tt)

			for i in range(len(tt)):
				if abs((yu1[i]+yu0[i])/2) >thr:
					hkflag=True

			##############################################
			if hkflag:
				y=hk
			#################################
			k=k+1

		#############################3
		Cs.append(hk)
		#####################################
		x0=[]
		for i in range(len(xx)):
			ss=0
			for j in range(len(Cs)):
				cn=Cs[j]
				ss+=cn[i]

			temp=xx[i]-ss
			x0.append(temp)
		#######################################
		check=0
		for i in range(1,len(x0)-1):
			if (x0[i]>=x0[i-1]) and (x0[i]>=x0[i+1]):
				check+=1
			elif (x0[i]<=x0[i-1]) and (x0[i]<=x0[i+1]):
				check+=1

		#########################################
		if check>3:
			c0flag=True
			y=x0

		n=n+1
		

	######################################
	Cs.insert(0,x0)

	return Cs



IMFs=hht(x,t,threshold)
#print(len(IMFs))

plt.plot(t,IMFs[0])
plt.show()