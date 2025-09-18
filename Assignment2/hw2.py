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
    pass

# problem 4
#input x percent
#return millions of dollars
def cost(x):
    pass

# Problem 5
#input dosage a mg and years t
#return child dosage mg
def D(t,a):
    pass

# Problem 6
#input number of susceptible, but healthy children
#output number of the infected children
# use math.ceil() before returning your final answer.
def I(S):
    pass

# Problem 7
#input number of items 
#output total cost 
# q > 0
def C(q):
    pass

#input number of items
#output average cost
def A(q):
    pass

# Problem 8
#input months t=0,...,11
#output items sold x 1000
def hh(t):
    pass

# Problem 9
#input time seconds
#output feet
def height(t):
    pass

# Problem 10
#input t hours
#output percent treatment
def B(t):
    pass

# Problem 11
# 3 Functions

#input years since (and including) 1980
#output per capita cigarette consumption
def cig(t):
    pass

#input years 2000->2004
#output kg of metamphetimine
def mk(y):
    pass

#input function and two points a<b
#output average rate of change
def arc(f,a,b):
    pass

# Problem 12 
#input P principle, n times per year, t years, r rate
#output dollars
def R(P,r,n,t):
    pass

#Problem 13
#input side s of a square
#output diagonal length 
def square_diagonal(s):
    pass

#input diagonal of a square
#output area of largest circle inscribed in square
def circle_area(d):
    pass

#Problem 14
#input velocity v (m/s), theta angle degrees
#output distance feet travelled
def dk(v,theta):
    pass

#problem 15
#input temperature (F), wind speed (mph)
#output wind chill
def T_wc(temp,wind_speed):
    pass


#problem 16
#input n
#output approximate to n!
def fact_est(n):
    pass

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
    # for i in 0,3,8:
    #     print(P(i))
    
    # Problem 4
    # for i in 50,70,90:
    #     print(cost(i))

    # Problem 5
    # print(D(4,500))
    
    # Problem 6
    # for S_6 in 100,300:
    #     print(I(S_6)) 

    # Problem 7
    # for q in 1,10,316:
    #     print(A(q))
    
    # Problem 8
    # for i in 0,5,10,11:
    #     print(hh(i))

    # Problem 9
    # print(height(5))
   
    # Problem 10        
    # Your own values

    # Problem 11
    # y1,y2 = 1985,2005
    # print(arc(cig,y2-1980,y1-1980))

    # y1,y2 = 2000,2004
    # print(arc(mk,y2,y1))

    # Problem 12
    # d12_1 = (22000,6/100,1,7)
    # print(R(*d12_1))
    # d12_2 = (500,4/100,12,20)
    # print(R(*d12_2))
    # d12_3 = (1200,8/100,4,10)
    # print(R(*d12_3))

    # Problem 13
    # print(circle_area(square_diagonal(10)))

    # Problem 14
    # print(dk(20,40))
    
    #problem 15
    # temp_15, wind_speed_15 = 2,5
    # print(T_wc(temp_15,wind_speed_15))

    #problem 16
    # n0_16 = 10
    # print(math.factorial(n0_16),fact_est(n0_16))
    # n0_16 = n0_16 * 10
    # print(math.factorial(n0_16),fact_est(n0_16))