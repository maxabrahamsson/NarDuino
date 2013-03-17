#Narduino Project by Ahmet YILDIRIM
#homepage:www.mclightning.com
#Code Licence: GNU General Public Licence v3

from bluetooth import *
import os,time,serial
c=raw_input('Bluetooth Port>>')
a=raw_input('ttyUSB>>')
h,p='00:1F:00:B5:3A:45',int(c)
print 'connecting'
try:
  sock=BluetoothSocket(RFCOMM)
  sock.connect((h,p))
except:
  print "Bluetooth Communication has failed"
try:
  ss=serial.Serial('/dev/ttyUSB'+a,9600)
except:
  print 'Serial Communication has failed'

import pygame
from pygame.locals import *
from sys import exit
pygame.init()
screen=pygame.display.set_mode((800,480),0,16)
Fullscreen=True
pygame.mixer.init()
a=pygame.image.load('./background.jpg')
ses=pygame.mixer.Sound('./transforming.wav')
screen=screen=pygame.display.set_mode((800,480),FULLSCREEN,16)
f=0
while True:
  for event in pygame.event.get():
    if(event.type==QUIT):
      exit()
    if(event.type==KEYDOWN):
      if(event.key==K_f):
        Fullscreen=not Fullscreen
        if Fullscreen:
          screen=screen=pygame.display.set_mode((800,480),FULLSCREEN,16)
        else:
          screen=screen=pygame.display.set_mode((800,480),FULLSCREEN,16)
  screen.fill((0,0,0))
  screen.blit(a,(150,0))
  if f==0:
    ses.play()
    f=1
  data=sock.recv(1024)
  if len(data)==11:
    print data
    if(data[3]=='1'):
      ss.write(u'b')
    if(data[3]=='2'):
      ss.write(u'a')
    if(data[3]=='0'):
      ss.write(u'c')
    if(data[6]=='1'):
      ss.write(u'd')
    if(data[6]=='2'):
      ss.write(u'e')
    if(data[6]=='0'):
      ss.write(u'f')
    if(data[9]=='1'):
      ss.write(u'g')
    if(data[9]=='0'):
      ss.write(u'h')
  else:
    print 'Buffer error'
  pygame.display.update()
client_sock.close()
server_sock.close()
print 'Connection Lost.'
