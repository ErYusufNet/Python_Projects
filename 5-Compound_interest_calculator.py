

principle = 0
rate = 0
time = 0
while principle <= 0:
    principle = float(input("Enter the principle: "))
    if principle <= 0:
        print("principle can not be less than zero or equal to zero")
while rate <= 0:
    rate = float(input("Enter interest rate: "))
    if rate <= 0:
        print("interest can not be less than zero or equal to zero")
while time <= 0:
    time = int(input("Enter the principle: "))
    if time <= 0:
        print("time can not be less than zero or equal to zero")
print(principle)
print(rate)
print(time)
final = principle * pow(( 1 + rate /time), time)
print (f"Balance after {time} years: €{final}.2f")