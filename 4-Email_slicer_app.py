email = input("Enter your email: ")
index = email.index("@") #@ isaretinin index yerini bulur
username = email[:index] #baslangictan baslar email indexe kadar olan yeri alir
domain = email[index:]# email indexten sonrasini alir
print(f"Your username is {username} and domain is {domain}")
