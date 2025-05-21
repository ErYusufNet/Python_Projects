import time
my_time = int(input("Enter the time: "))
for x in range(my_time, 0, -1):
    
    print(f"{x} seconds remaining")
    time.sleep(1)

print("Wake up!")