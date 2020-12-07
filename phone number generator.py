import random
#make decision for operator

operator_list = ["banglalink","grameephone","robi","airtel","teletalk","citycell"]
random_operator=random.choice(operator_list)
	
	#get the operator number with condition
	
if random_operator == "banglalink":
		numbers = random.choice(["019","014"])
elif random_operator == "grameephone":
		numbers = random.choice(["013","017"])	
elif random_operator == "airtel":
		numbers = "016"
elif random_operator == "robi":
		numbers = "018"
elif random_operator == "teletalk":
		numbers = "011"
else:
		numbers = "015"
	#sign another numbers
other_numbers1 = random.randint(0,9)
other_numbers2 = random.randint(0,9)
other_numbers3 = random.randint(0,9)
other_numbers4 = random.randint(0,9)
other_numbers5 = random.randint(0,9)
other_numbers6 = random.randint(0,9)
other_numbers7 = random.randint(0,9)
other_numbers8 = random.randint(0,9)
	
print(f"your number is +88{numbers}{other_numbers1}{other_numbers2}{other_numbers3}{other_numbers4}{other_numbers5}{other_numbers6}{other_numbers7}{other_numbers8}")
	
	