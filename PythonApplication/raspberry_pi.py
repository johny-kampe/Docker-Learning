import random
from time import sleep

while True:
	temp = random.randint(15,45) #Temperature
	ahum = random.randint(0,100) #Air humidity	
	ghum = random.randint(0,100) #Ground humidity
	wind = random.randint(0,17) #Beaufort (Bofor)
	
	print("Temperature:",temp)
	print("Air humidity:",ahum)
	print("Ground humidity:",ghum)
	print("Beaufort:",wind,"\n")

   	sleep(5) #produce data every 30 seconds
