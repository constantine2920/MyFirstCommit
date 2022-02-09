

#Suppose object A is traveling towards object B with a speed v. A and B are separated by a
#distance d. If A is decelerating by a value of a , we want to determine if it will hit the object B.
#The user must provide the following values d, v and a. d is in the range [5,10], a is in the range
#[-100,0] and v is in the range [1,10]. The distance travelled by the object A in time t (a positive
#number less than 10 that is also to be received from the user) can be calculated as
#� = max(0, �� + 0.5��!)
#If s is greater than or equal to d then the object will collide. Write a python program that does
#the following: (i) determines if the objects collide for a given set of d, v, a and t. (ii) for a given
#value of d and v, and starting with a = -50, determines the critical value of a at which A will just
#touch B.
#Hint: To find the critical value of a, keep increasing a by a small amount (example, 0.2 ), and for
#each value of a scan through a long range of t to conclusively establish if the object A hits B or
#not. Note: All values are floating point data.

#Get input

#D is in the range [5 , 10]

#V is in the range [1, 10]
#a is in the range [-100 , 0] 

def RecieveInputForFloat(TextToPrint):
    statusCode = 1
    try:
        print(TextToPrint)
        DistanceToTen = float(input())
        return DistanceToTen, statusCode
    except:
        print("Please enter a decimal or integer, no text")
        statusCode = -1
        return "Error", statusCode

def RecieveUserInput():
    DistanceInput = RecieveInputForFloat("Please enter the distance from 5 to 10")
    #ErrorChecking
    if DistanceInput[1] != -1:
        print(F'{DistanceInput[0]} is the distance between both locations')

    VelocityInput = RecieveInputForFloat("Please enter a velocity from 1 to 10")
    #ErrorChecking
    if VelocityInput[1] != -1:
        print(F'{VelocityInput[0]} is the current velocity in the range [1 ,10]')

    DecelerationInput = RecieveInputForFloat("Please enter the decleration Value from -100 to 0")
    #ErrorChecking
    if DecelerationInput[1] != -1:
        print(F'{DecelerationInput[0]} is the current deceleration in the range [-100 ,0]')
    
    return DistanceInput[0],VelocityInput[0],DecelerationInput[0]

#how fast is the object going
print("Did Pool ball A Hit Pool ball Two")

#UserInput = RecieveUserInput()

d = 10
v = 10
a = -50

CurrentT = 0
STEPTIME = 1
haveTheyColided = 0
shortestTime = 0 
previousTravelDistance = 100
ClosestDistance = 100
ClosestA = 0
while a <= -46:
    print("\n A Value: ", "{:10.2f}".format(a), "\n")
    print( "Distance Traveled", "   Time Taken", "   Total Distance " "    Distance Remaining")
    CurrentT =0
    s = 0
   
    while s <=d:
        s = max(0,v*CurrentT+0.5*a*CurrentT**2)
    #Manual print of first row
        
        if d-s <= ClosestDistance:
            ClosestDistance =  d-s
            ClosestA = a
            shortestTime = CurrentT
        CurrentT = CurrentT+0.01
        print("{:10.4f}".format(s),"        ",  "{:10.3f}".format(CurrentT),"          ",d, "        ", "{:10.2f}".format(d-s ))

    print(f' \n A colision occured at {"{:10.3f}".format(CurrentT)} Units of time {s} Distance Traveled ' )
    
    a = a + 0.2

print(" Distance Overshot              A Value    Time taken")
print(ClosestDistance,"     ","{:10.2f}".format(ClosestA), "    ","{:10.4f}".format(shortestTime))