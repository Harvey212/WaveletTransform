import time
import numpy as np
import math
import cmath
import cv2
import wave



##############################################
def myRange(start,end,step):
    i = start
    while i < end:
        yield i
        i += step
    yield end

wavefile=wave.open('Chord.wav','rb')

fs =wavefile.getframerate()

num_frame = wavefile.getnframes()

str_data = wavefile.readframes(num_frame)


wave_data = np.frombuffer(str_data, dtype=np.int16)
#wave_data = wave_data / max(abs(wave_data))

n_channel = 2
wave_data = np.reshape(wave_data, (num_frame, n_channel))

mydata=wave_data[:,0]
###########################################
dtau=1/44100
dt=0.01
df=1
sgm=200
###########################################
tau=[]
maxx=0
for tauu in myRange(0,1.6,dtau):
    tau.append(tauu)
    if maxx<tauu:
    	maxx=tauu

##################
t=[]
for tt in myRange(0,maxx,dt):
    t.append(tt)

##############################
f=[]
for ff in myRange(20,1000,df):
    f.append(ff)

###########################################################
def gabor(x,tau,t,f,sgm):
	dtau=tau[1]-tau[0] 
	dt=t[1]-t[0]
	df=f[1]-f[0]
	N=round(1/(dtau*df))
	Q=round(1.9143/(math.sqrt(sgm)*dtau))
	S=round(dt/dtau)

	####################################
	immm=np.zeros((len(t),len(f)), dtype=np.uint8)
	mag=0.25
	#buff2=[]
	#for _ in range(2*Q+1,N):
	#	buff2.append(0)
	T=immm.shape[0]
	F=immm.shape[1]
	#####################################################
	
	for n in range(T):
		buff=[]
		for q in range(2*Q+1):
			ind=int(q+n*S-Q)
			if (ind>-1) and (ind<len(x)):
				myx=x[ind]
			else:
				myx=0

			s=dtau*(q-Q)
			xx=myx*cmath.exp(-sgm*math.pi*s*s)
			buff.append(xx)

		#bf=buff+buff2

		
		fftX=np.fft.fft(buff,N)
		

		for m in range(F):
			
			k=2*math.pi*(Q-n*S)*m/N
			Ak=dtau*cmath.exp(1j*k)*pow(sgm,1/4)
			immm[n,F-1-m]=abs(Ak*fftX[m])*mag 

			
			#################################
			



	return immm.transpose()


################################
start=time.time()
see=gabor(mydata,tau,t,f,sgm)
end=time.time()
diff=end-start

print('calculated time is:')
print(diff)
print('secs')
see = cv2.resize(see, (400, 400)) 
cv2.imshow('result', see)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
