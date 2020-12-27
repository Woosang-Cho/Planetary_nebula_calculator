'''
21cm 전파를 보내는 행성상성운과 우리 은하 사이 상대적 속도를 계산합니다.
21cm 전파의 lamda_0 는 5006.84 A 이고,관측된 파장 lamda 와 적색편이 z가 주어졌을 때 시선속도 V_r 은 다음과 같이 주어집니다.

V_r = z * c = (lambda_obsereved - lamda_0/lambda_0)*c
'''

from astropy import constants as const
import math

lambda_obsereved = float(input("Enter the obeserved wavelength (lambda_obsereved): "))
lambda_0 = 5006.84 
c = const.c.to('km/s')

def func_V_r():
    print(" \n V_r = " , end='', flush = True)

func_V_r()

def func_radial_velocity(lambda_obsereved, lambda_0, c):
    print( ((lambda_obsereved - lambda_0)/ lambda_0 )*c )

func_radial_velocity(lambda_obsereved, lambda_0, c)