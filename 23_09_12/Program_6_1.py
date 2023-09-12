while True:
    userInp = int(input("please input number"))
    listNums = []


    userConfirm = str(input("wanna add more y or n").lower)

    if userConfirm == "y" or "yes":
        listNums.append(userInp)
        continue
    if userConfirm == "n" or "no":
        break
        for i in listNums(-1,0):
            print(i)

32