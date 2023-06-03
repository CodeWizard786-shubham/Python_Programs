"""
@Author: shubham shirke
@Date: 2022-06-02 22:15:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-02 22:15:30
@Title : Gamblers problem to gamble 1 dollar each until it reaches goal amount or go broke.
"""

import random

def gambler_simulation(stake,goal,num):
    """
    Description: The function contains a random function to genrate random number to decide win or lose with 1$ bet.
                 It counts the number the times the bet is made along with number of wins.
    Parameter : stake - initial amount to start with  
                goal - final amount to achieve 
                num - num of times the bet must be made.
    result   :  Number of games played , win count , win percentage , lose percentage.
    """
    bet_amount = 1
    play_count=0
    win_count=0

    for _ in range(num):
        while(stake !=0 and stake!=goal):
            random_number = random.randint(0,1)
            play_count+=1
            if(random_number==0):
                stake = stake-bet_amount
            else:
                stake = stake+bet_amount
                win_count +=1
            if(stake == 0 or stake==goal):
                break
    return win_count,play_count




# Read in stake , goal and num of bets to make from user input
stake_amount= int(input("Enter stake amount: "))
goal_amount = int(input("Enter goal amount: "))
num = int(input("Enter number of times to bet: "))

win_count,play_count=gambler_simulation(stake_amount,goal_amount,num)

#calculate win and lose percentage
win_percentage = (win_count/play_count)*100
lose_percentage = 100 - win_percentage

# print output
print("Number of games played: ",play_count)
print("Number of games Won: ",win_count)
print("Win percentage: ",win_percentage)
print("Lose percentage: ",lose_percentage)