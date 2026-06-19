'''
-1 = snake,
0 = water,
1 = gun
'''
#snake water and gun game.
import random #used lib for random guess for computer

computer = random.choice([-1,0,1])

youstr = int(input("enter your choice:")) #input from user
youdict = {"water":0,"snake":-1,"gun":1}
reverse_dict = {0:"water",-1:"snake",1:"gun"}

print(f"computer choice is {reverse_dict[computer]} \n  your choice is {reverse_dict[youstr]} ")

if (computer == youstr):
    print("its draw")
else:
    if(computer == 0 and youstr == -1): #comp = water, you = snake
        print("you win")
    elif(computer == 1 and youstr == -1):   #comp = gun,you = snake
        print("you lose")
    elif(computer == -1 and youstr == 1):   #comp = gun,you = water
        print("you win")
    elif(computer == -1 and youstr == 0):   #comp =  snake,you = water
        print("you lose")
    elif(computer == 1 and youstr == 0):    #comp = gun,you = water
        print("you win")
    elif(computer == 0 and youstr == 1):    #comp = water,you = gun
        print("you lose")

        

    