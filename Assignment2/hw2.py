# Homework 2 
# (C/H)200 Fall 2025
# IU Bloomington
# Data Science/Computer Science
# MM Dalkilic
import math

# Problem 1
#input radius r, height h
#return volume
def c(r,h):
    vol = (1/3)*math.pi*(r**2)*h
    return round(vol)
    
# Problem 2
#input t days
#output oxygen conten percent of it normal level
def f(t):
    ox = 100*(((t**2)+(10*t)+100)/((t**2)+(20*t)+100))
    return round(ox,2) 
# Problem 3
#input t hours
#return percent watching tv
def P(t):
    per = (0.0135*(t**4))-(0.49375*(t**3))+(2.58333*(t**2))+(3.8*t)+31.60704
    return round (per,2)
# problem 4
#input x percent
#return millions of dollars
def cost(x):
    c = ((0.5*x)/(100-x))
    return round (c,2)
# Problem 5
#input dosage a mg and years t
#return child dosage mg
def D(t,a):
    dos = (a*((t+1)/24))
    return round (dos,2)
# Problem 6
#input number of susceptible, but healthy children
#output number of the infected children
# use math.ceil() before returning your final answer.
def I(S):
    infect = (192*math.log2(S/2)-S+763)
    return math.ceil(infect)

# Problem 7
#input number of items 
#output total cost 
# q > 0
def C(q):
    total = (0.01*(q**2)) - (0.6*q)+1000
    return total
#input number of items
#output average cost
def A(q):
    avg = ((0.01*(q**2)) - (0.6*q)+1000)/q
    return avg
# Problem 8
#input months t=0,...,11
#output items sold x 1000
def hh(t):
    sales = 532/(1+(869*(math.e**(-1.33*t))))
    return math.floor(sales)
# Problem 9
#input time seconds
#output feet
def height(t):
    height1 = (-16*(t**2))+(64*t)+80
    return round (height1,2)
# Problem 10
#input t hours
#output percent treatment
def B(t):
    if 0 <= t and t <= 24:
        benefit = ((0.44*(t**4))+700)/((0.1*(t**4))+7)
        return round (benefit,2)
# Problem 11
# 3 Functions

#input years since (and including) 1980
#output per capita cigarette consumption
def cig(t):
    cig1 = 3870*(0.970**t)
    return math.ceil(cig1)
#input years 2000->2004
#output kg of metamphetimine
def mk(y):
    meta = (151.500000*(y**2))-(606377.300265*y)+606755991.065880
    return math.floor(meta)
#input function and two points a<b
#output average rate of change
def arc(f,a,b):
    rate1 = (mk(b) - mk(a))/(b-a)
    return rate1
# Problem 12 
#input P principle, n times per year, t years, r rate
#output dollars
def R(P,r,n,t):
    payment = P*(((1+((r/n)**(n*t)))-1)/(r/n))
    return round (payment)
#Problem 13
#input side s of a square
#output diagonal length 
def diagonal(s):
    diag = square_diagonal(s)
    return round (diag,2)
#input diagonal of a square
#output area of largest circle inscribed in square
def circle_area(d):
    circlearea = circle_area(square_diagonal(s))
    return round (circlearea,2)
#Problem 14
#input velocity v (m/s), theta angle degrees
#output distance feet travelled
def dk(v,theta):
    distance = ((v**2)/g)*math.sin(2*math.radians(theta))*3.2808399
    return round (distance,2)

#problem 15
#input temperature (F), wind speed (mph)
#output wind chill
def T_wc(temp,wind_speed):
    chill = 35.74+0.6215(temp) - 35.75(wind_speed**0.16)+(0.4275*temp*(wind_speed**0.16))
    return math.floor(chill)

#problem 16
#input n
#output approximate to n!
def fact_est(n):
    return (math.factorial(n),fact_est(n))

if __name__ == "__main__":

    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here  """

    # Problem 1
    print(c(2,5)) 
    print(c(3,7))

    # Problem 2
    print(f(0))
    print(f(10))

    # Problem 3
    for i in 0,3,8:
        print(P(i))
    
    # Problem 4
    for i in 50,70,90:
        print(cost(i))

    # Problem 5
    print(D(4,500))
    
    # Problem 6
    for S_6 in 100,300:
        print(I(S_6)) 

    # Problem 7
    for q in 1,10,316:
        print(A(q))
    
    # Problem 8
    for i in 0,5,10,11:
        print(hh(i))

    # Problem 9
    print(height(5))
   
    # Problem 10        
    print (B(12))

    # Problem 11
    y1,y2 = 1985,2005
    print(arc(cig,y2-1980,y1-1980))

    y1,y2 = 2000,2004
    print(arc(mk,y2,y1))

    # Problem 12
    d12_1 = (22000,6/100,1,7)
    print(R(*d12_1))
    d12_2 = (500,4/100,12,20)
    print(R(*d12_2))
    d12_3 = (1200,8/100,4,10)
    print(R(*d12_3))

    # Problem 13
    print(diagonal(10))

    # Problem 14
    print(dk(20,40))
    
    #problem 15
    temp_15, wind_speed_15 = 2,5
    print(T_wc(temp_15,wind_speed_15))

    #problem 16
    n0_16 = 10
    print(math.factorial(n0_16),fact_est(n0_16))
    n0_16 = n0_16 * 10
    print(math.factorial(n0_16),fact_est(n0_16))