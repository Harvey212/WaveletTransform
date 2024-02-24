from scipy.io.wavfile import write
import numpy as np

def gwave(a,b,c,T,Fs):
	samplerate = Fs
	time = np.linspace(0, T, num=samplerate*T)

	datas=[]

	for i in range(len(time)):
		t=time[i]
		fs = a*t*t+b*t+c
		amplitude = np.iinfo(np.int16).max
		
		data = amplitude * np.sin(2. * np.pi * fs )

		datas.append(data)
	
	datas=np.array(datas)
	write(filename="ex7.wav",rate= samplerate,data=datas.astype(np.int16))

A =10 #input("Enter number a:")
B =4  #input("Enter number b:")
C =5  #input("Enter number c:")
T =20   #input("Enter length of the file T:")
FF=44100 #input("Enter sampling frequency Fs:")

gwave(A,B,C,T,FF)