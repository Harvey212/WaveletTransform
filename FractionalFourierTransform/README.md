# 時頻分析與小波轉換 期末專案       
姓名:葉冠宏   學號:R11943113<br />

## 一、專案目標
本次期末專案主要在實作有關fractional fourier transform的部分，以及有關頻譜的shifting, dilation,和 shearing。Fractional fourier transform的部分主要是參考[1]的論文來進行實作。<br />

[1] Digital Computation of the Fractional Fourier Transform, Haldun M. Ozaktas, Orhan Ankan, Member, IEEE, M. Alper Kutay, Student Member, IEEE, and Gozde Bozdaki, Member, IEEE

<br />
註:詳細的實驗結果會在pdf檔。

## 二、使用程式環境
語言:Python<br />
套件:<br />
numpy<br />
math<br />
cmath<br />
cv2<br />
scipy.signal<br />
argparse<br />
matplotlib.pyplot<br />
random<br />

## 三、實驗一:Fractional Fourier transform
1.執行方式:
```
python test1.py
```
2.說明:我們假設fraction 為1代表作一次完整的fourier transform，即會使得頻譜轉pi/2圈。而例如:fraction=0.3代表作0.3次的fourier transform，會使得頻譜轉0.3*pi/2圈。實作會分別對訊號如果做0次、0.3次、1次、1.7次、2.3次、3.5次fourier transform來做實驗。<br />

## 四、實驗二: 實作頻譜的shifting, dilation, shearing和Fractional fourier transform
1.執行方式:
```
python test2.py --[arg1] [value1]
```
其中arg1為hshift或vshift或dilate或fshear或tshear或frac，value1則為其對應的值。<br />
Hshift代表horizontal shifting，對應的值為時間軸的位移。<br />
Vshift代表vertical shifting，對應的值為頻率軸的位移。<br />
Dilate代表scaling，對應的值代表頻率軸和時間軸的縮放率。<br />
Fshear代表針對頻率軸的shearing，其值代表其shearing直線的斜率。<br />
Tshear代表針對時間軸的shearing，其值代表其shearing直線的斜率。<br />
Frac代表對頻譜做rotation，以及fractional fourier transform，其值代表是幾個fourier transform。<br />

例如: python test2.py --hshift 2 就是對於頻譜做horizontal shifting，對時間軸做2秒的位移。<br />
如果想只看原圖也可以執行python test2.py 就好。<br />
