weight = float(input("Please, enter your weight: "))
unit = input("Is your weight in (K)g or (L)bs: ")

if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else: 
    converted = weight * 0.45
    print("Weight in Kg: " + str(converted))





