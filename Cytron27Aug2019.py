##Simple motor script for the RTK-000-001
import RPi.GPIO as GPIO
import time
import sys
#Set to broadcom pin numbers
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

DirRV = 9
PwmRV = 11

GPIO.setup(DirRV, GPIO.OUT)
GPIO.setup(PwmRV, GPIO.OUT)

rv = GPIO.PWM(PwmRV, 20000) # 20000 hertz

DirLV = 5
PwmLV = 6

DirR = 17
PwmR = 27

DirLV = 22
PwmRL = 10

GPIO.setup(DirRV, GPIO.OUT) # 17
GPIO.setup(PwmRV, GPIO.OUT) # 18

GPIO.output(PwmRV, 1)
GPIO.output(DirRV, 0)

print
rv.start(5)
time.sleep(2)

# rv.start(80)
# time.sleep(2)
# 
# for i in range(500):
#     time.sleep(0.01)
#     rv.start(i % 100) # set motor to speed 
# time.sleep(1)
# 
# GPIO.output(PwmRV, 0)

GPIO.cleanup()
sys.exit()




# def toggle_dir(pin):
#     if GPIO.input(pin):
#         GPIO.output(pin, 0)
#     else:
#         GPIO.output(pin, 1)
# 
# while (True):
#     try:
#         print ("SPEED 0")
#         GPIO.output(PwmRV, 0)
#         print ("SLEEP 1")
#         time.sleep(1)
#         print ("DIR 0")
#         toggle_dir(DirRV)
#         print ("SPEED 1")
#         GPIO.output(PwmRV, 1)
#         print ("SLEEP 1")
#         time.sleep(1)
#         print ("SPEED 0")
#         GPIO.output(PwmRV, 0)
#         print ("SLEEP 1")
#         time.sleep(1)
#         print ("DIR 1")
#         #GPIO.output(DirRV, 1)
#         toggle_dir(DirRV)
#         print ("SPEED 1")
#         GPIO.output(PwmRV, 1)
#         print ("SLEEP 1")
#         time.sleep(1)
#     except:
#         print ("STOPPING")
#         GPIO.cleanup()
#         break
    
    
    
    


    
        


# import keyboard
# 
# while True:
#     try:
#         if keyboard.is_pressed("a"):
#             print ("A PRESSED")
#     except KeyboardInterrupt:
#         print ("STOPPING")
#      #   GPIO.cleanup()
# 






# import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# 
# DirRV=17
# PwmRV=27
# GPIO.setup(PwmRV,GPIO.OUT)
# GPIO.setup(DirRV,GPIO.OUT)
# rv=GPIO.PWM(PwmRV,100)
# 
# DirR=22
# PwmR=10
# GPIO.setup(DirR,GPIO.OUT)
# GPIO.setup(PwmR,GPIO.OUT)
# r=GPIO.PWM(PwmR,100)
# 
# DirL=9
# PwmL=11
# GPIO.setup(DirL,GPIO.OUT)
# GPIO.setup(PwmL,GPIO.OUT)
# l=GPIO.PWM(PwmL,100)
# 
# DirLV=5
# PwmLV=6
# GPIO.setup(DirLV,GPIO.OUT)
# GPIO.setup(PwmLV,GPIO.OUT)
# lv=GPIO.PWM(PwmLV,100)
# 
# def RV(w):
#     if(w<=0):
#         GPIO.output(DirRV,GPIO.HIGH)
#         rv.start(abs(w))
#     if(w>0):
#         GPIO.output(DirRV,GPIO.LOW)
#         rv.start(abs(w))
# 
# def R(x):
#     if(x<=0):
#         GPIO.output(DirR,GPIO.HIGH)
#         r.start(abs(x))
#     if(x>0):
#         GPIO.output(DirR,GPIO.LOW)
#         r.start(abs(x))
# 
# def LV(y):
#     if(y>=0):
#         GPIO.output(DirLV,GPIO.HIGH)
#         lv.start(abs(y))
#     if(y<0):
#         GPIO.output(DirLV,GPIO.LOW)
#         lv.start(abs(y))
# def L(z):
#     if(z<=0):
#         GPIO.output(DirL,GPIO.HIGH)
#         l.start(abs(z))
#     if(z>0):
#         GPIO.output(DirL,GPIO.LOW)
#         l.start(abs(z))
#         
# RV(10)
# R(10)
# LV(10)
# L(10)



# import time
# 
# import RPi.GPIO as GPIO
# 
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(True)
# 
# # DirRV=17
# # PwmRV=27 #rv
# # GPIO.setup(PwmRV,GPIO.OUT)
# # GPIO.setup(DirRV,GPIO.OUT)
# # rv=GPIO.PWM(PwmRV,20)
# # 
# # DirR=22
# # PwmR=10 #r
# # GPIO.setup(DirR,GPIO.OUT)
# # GPIO.setup(PwmR,GPIO.OUT)
# # r=GPIO.PWM(PwmR,20)
# 
# DirL=22
# PwmL=10 #l
# GPIO.setup(DirL,GPIO.OUT)
# GPIO.setup(PwmL,GPIO.OUT)
# l=GPIO.PWM(PwmL,10000)
# 
# DirLV=27
# PwmLV=17 #lv
# GPIO.setup(DirLV,GPIO.OUT)
# GPIO.setup(PwmLV,GPIO.OUT)
# lv=GPIO.PWM(PwmLV,10000)
# 
# GPIO.output(DirL, GPIO.LOW)
# #GPIO.output(DirRV, GPIO.LOW)
# 
# n = 0
# #while True:
#   #  time.sleep(0.05)
# l.start(n)
#     #rv.start(n)
#     #n += 1
#     #n %= 100
# print(n)
# '''
# DirL=9
# PwmL=11 #l
# GPIO.setup(DirL,GPIO.OUT)
# GPIO.setup(PwmL,GPIO.OUT)
# l=GPIO.PWM(PwmL,20)
# 
# DirLV=5
# PwmLV=6 #lv
# GPIO.setup(DirLV,GPIO.OUT)
# GPIO.setup(PwmLV,GPIO.OUT)
# lv=GPIO.PWM(PwmLV,20)
# 
# def RV(w):
#     print ("CALLED RV with w=" + str(w))
#     if(w<=0):
#         print ("GPIO.HIGH")
#         GPIO.output(DirRV,GPIO.HIGH)
#         rv.start(abs(w))
#     if(w>0):
#         print ("GPIO.LOW")
#         GPIO.output(DirRV,GPIO.LOW)
#         rv.start(abs(w))
# 
# def R(x):
#   #  print ("CALLED R with x=" + str(x))
#     if(x<=0):
#         print ("GPIO.HIGH")
#         GPIO.output(DirR,GPIO.HIGH)
#         r.start(abs(x))
#     if(x>0):
#         print ("GPIO.LOW")
#         GPIO.output(DirR,GPIO.LOW)
#         r.start(abs(x))
#     
# # GPIO.output(DirL, GPIO.LOW)
# # GPIO.output(DirL
#     
# # n = 0
# # while n < 1000000: 
# #     time.sleep(0.1)
# #     RV(-10)
# #     n += 1
# #     
# # print ("DONE")
# 
# def LV(y):
#     if(y>=0):
#         GPIO.output(DirLV,GPIO.HIGH)
#         lv.start(abs(y))
#     if(y<0):
#         GPIO.output(DirLV,GPIO.LOW)
#         lv.start(abs(y))
# def L(z):
#     if(z<=0):
#         GPIO.output(DirL,GPIO.HIGH)
#         l.start(abs(z))
#     if(z>0):
#         GPIO.output(DirL,GPIO.LOW)
#         l.start(abs(z))
#         
# L(50)
# LV(50)
# R(50)
# RV(50)
# '''
# 