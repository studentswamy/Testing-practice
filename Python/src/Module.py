# write a program to reverse a number
n=int(input("enter the number"))
for i in range(1,n+1):
    print(i,end='')
print("")
for j in range(0,n):
        print(n-j,end='')       
print("")

# length of string
cricket = "Indiancricketcouncil"
count = 0
for letters in cricket:
    count +=1
print(count)

#Reverse a letter
string = "Hello world"
print(string[::-1])
