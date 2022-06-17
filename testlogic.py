car=input("which car do you have")
print(f"fuck you you have a {car}, i dont believe that shit ")

car=input("can you tell how many cars you have")
print("no shit {} this much ".format(car))

car=input("which is you fav car")
if car=="mercedes":
    print("shit you like mercedes me too ")

elif car=="ferrari":
    print("hmm thats a fast car")
else:
    print("those are ok ok ")
    print(" you should reconsider press y/n")
    x=input()
    if x=="y":
        car=input("enter again ")
    else:
        exit()



li = ['kaif',' kkoo ' ,'rave', 'maek ']
list=' '.join(li)
print(list)
listnew = list.split()
print(listnew)