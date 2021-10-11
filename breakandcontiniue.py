#break statement(while 1,while true loop),stop the looop is also known as break statement
i = 0

while(1):
    if i+1<=50:
        i = i+1
        continue

    print(i+1, end="  ")
    if(i==70):
        break
    i = i + 1
    #example--
    #to take a num from user the pint a num greater than a num
    while(1):
        inp = int(input("enter a number"))
        if inp>100:
            print("congrats bahi ji you have enterd a number greater than 100")
            break
        else:
            print("try again!!!!")
            continue

