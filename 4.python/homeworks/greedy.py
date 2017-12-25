# quarter : 0.25, dimes = 0.1, nickel = 0.05, pennies = 0.01

def money(change, sous):
    coin = int(round(change * 100) // round(sous * 100))
    change -= coin * sous
    result = [change, coin]
    return result

change = -1
while change < 0:
    change = float(input("Change : "))

coin_value = [0.25, 0.1, 0.05, 0.01]
coin_number = [0,0,0,0]
index = 0

for value in coin_value:
    result = money(change, value)
    change = result[0]
    coin_number[index] = result[1]
    index += 1

print("Change is {} quarter, {} dimes, {} nickel and {} pennies.".format(coin_number[0], 
    coin_number[1], coin_number[2], coin_number[3])) 
