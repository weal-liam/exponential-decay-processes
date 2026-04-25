#This program calculates the exponential decay of a substance over time,
#Given an initial amount, a decay factor, and a time period. 
#It also includes a function to calculate the decay factor based on known data points
#And a function to tabulate the results over a specified time range.
#import math module to perform mathematical operations, specifically for calculating the exponential decay and logarithm.
import math

# The exp_decay function calculates the remaining amount of a substance after a certain time period, given an initial amount and a decay factor.
def exp_decay(t = 0, decay_factor = 0.0, initial_N = 1):
    #this function takes three parameters: t (time), decay_factor (the rate of decay), and initial_N (the initial amount of the substance).
    #the formula used is N(t) = N0 * e^(-kt), where N0 is the initial amount, k is the decay factor, and t is time.
    current_N = initial_N * pow(math.e,(-(decay_factor) * t))
    return current_N #returns the calculated amount of the substance remaining after time t

# The get_decay_factor function calculates the decay factor commonly denoted as k or lambda
def get_decay_factor(tn = 0, current_N = 0, initial_N = 0):
    #this function takes three parameters: tn (the time at which the current amount is measured), current_N (the amount of the substance at time tn), and initial_N (the initial amount of the substance).
    #this function calculates the decay factor based on known data points.
    #it uses the formula k = ln(N0/N(t))/t, where N0 is the initial amount, N(t) is the amount at time t, and t is the time period.
    decay_factor = math.log(initial_N/current_N)/tn
    return decay_factor

# The tabulate function generates a table of the remaining amount of the substance over a specified time range, given an initial amount, a known data point, and the calculated decay factor.
def tabulate(time_range = 0, initial_N = 0, tn = 0, current_N = 0):
    #this function takes four parameters: time_range (the total time period for which to generate the table), initial_N (the initial amount of the substance), tn (the time at which the current amount is measured), and current_N (the amount of the substance at time tn).
    #the function first initializes a table with the known data point (time tn and current amount current_N).
    #it then calculates the decay factor using the get_decay_factor function.
    table = [[0,tn],[initial_N, current_N]]
    decay_factor = get_decay_factor(tn, current_N, initial_N)

    #the function uses a for loop to iterate over the specified time range,
    #calculating the remaining amount of the substance at each time point using the exp_decay function
    #appending the results to the table.
    for i in range(time_range):
        if i != 0 and i != tn:
            amount = exp_decay(i, decay_factor, initial_N)
            table[0].append(i)
            table[1].append(round(amount,3))
    
    #after populating the table with the calculated values,
    #it sorts the time points in ascending order and the corresponding amounts in descending order for better readability.
    table[0], table[1] = sorted(table[0]), sorted(table[1],reverse=True)

    #finally, it prints the initial amount, the known data point, the calculated decay factor, and the generated table of values over the specified time range.
    print(f"Using initial amount, {initial_N}, known data `amount {current_N} after {tn} days`,\nThe decay factor, approximately {decay_factor:.2f} obtained, gives the data below for a period of {time_range} days\n", table)

    #lastly, the function returns the generated table of time points and corresponding amounts.
    return table
