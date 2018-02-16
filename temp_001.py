import serial 
import numpy
import matplotlib.pyplot as plt
from drawnow import *
import pygame
from pygame import *

timeS = []
tempC = []
arduinoData = serial.Serial('com12', 9600)
plt.ion()
pygame.mixer.init()

def makeFig():
	plt.style.use('ggplot')
	plt.plot(tempC, 'ro-', label='Centigrados')
	plt.legend(loc='upper left')
	plt.rc('lines', linewidth=3, color='g')
	


while True: 
	while(arduinoData.inWaiting()==0):
		pass
	arduinoString = (arduinoData.readline().decode("utf-8"))
	dataArray = arduinoString.split(',')
	time = float (dataArray[0])
	temp = float (dataArray[1])
	timeS.append(time)
	tempC.append(temp)
	print (timeS,tempC)
	drawnow(makeFig)
	plt.pause(0.000001)
	

	if temp >= 25:
		pass
		pygame.mixer.music.load('alarm1.ogg')
		pygame.mixer.music.play();


