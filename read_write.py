#file = open("read_write.txt","w")

#x = int(input("Enter the no of lines you are going to enter"))

#for i in range(x) :
#    file.write(str(input(f"Enter {i+1} Line")))

#file.close()

# claud_one GOATED

file = open("read_write.txt","w")

x = int(input("Enter the no of lines you are going to enter"))

for i in range(x) :
    file.write(str(input(f"Enter {i+1} Line")))

file.close()

with open("read_write.txt", "r") as file:
        print("Result:", repr(file.read()))