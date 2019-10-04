# Name: Naima Ontiveros
# Period 4
# Dice Rolling Simulator
import random

num_rolled = int(input("How many times will the dice be rolled?"))


ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0
sevens = 0
eights = 0
nines = 0
tens = 0

i = 0
print("Total Rolls: " + str(num_rolled))

while i < num_rolled:
	i += 1
	D4 = random.randrange(1, 5, 1)
	D6 = random.randrange(1, 7, 1)
	D8 = random.randrange(1, 9, 1)
	D10 = random.randrange(1, 11, 1)
	D12 = random.randrange(1, 13, 1)
	D20 = random.randrange(1, 21, 1)

	print("Roll " + str(i) + "-------------" + "\n" + "Dice 1 (1,6): "+ str(D4) )

	if D4 == 1:
		ones += 1
	elif D4 == 2:
		twos += 1
	elif D4 == 3:
		threes += 1
	else: 
		D4 == 4
		fours += 1

	
	print("1s - " + str(ones))
	print("2s - " + str(twos))
	print("3s - " + str(threes))
	print("4s - " + str(fours))
	print("5s - " + str(fives))
	print("6s - " + str(sixes))


	print("Percentages:")
	print("1s - " + str(ones/(i)*100) + "%")
	print("2s - " + str(twos/(i)*100) + "%")
	print("3s - " + str(threes/(i)*100) + "%")
	print("4s - " + str(fours/(i)*100) + "%")
	print("5s - " + str(fives/(i)*100) + "%")
	print("6s - " + str(sixes/(i)*100) + "%")



