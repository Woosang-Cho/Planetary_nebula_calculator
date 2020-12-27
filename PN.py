'''
(1)에서 구한 시선속도 V_r 에 대하여, 은경 l은 다음과 같이 주어집니다 (cos law):

ㅣ = math.acos(((8kpc)**2 + R**2 - V_r**2)/(2 * 8kpc * R))

8kpc: 은하 중심--지구 거리
R: 은하 중심 -- PN(행성상성운)거리
V_r: 시선속도 
'''
from astropy import constants as const
import math

R = float(input("Enter the distance of Galactic center to Planetary neblua (R): ")) #은하중심--행성상성운 거리를 받습니다
V_r = float(input("Enter the radial velocity (V_r): ")) #시선속도를 받습니다

def func_l(): 
    print(" \n l = " , end='', flush = True)

func_l() #그냥 l = 을 밷는 함수입니다. 제 미천한 코딩실력 때문에 이거밖에 방법을 모릅니다

def func_calculate(R, V_r): #은경 l 을 계산하기 위해 은하중심--행성상성운 거리 R 과, 시선속도 V_r 을 받습니다
    print( round( math.acos( math.cos( (V_r*V_r + 64 - R*R) / (16*V_r)) ), 3)  ) #은경 ㅣ값을 (계산)출력합니다

func_calculate(R, V_r)

