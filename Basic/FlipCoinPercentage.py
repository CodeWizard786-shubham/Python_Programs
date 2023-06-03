"""
@Author: shubham shirke
@Date: 2022-06-02 18:00:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-02 13:03:30
@Title : To flip a coin and find the percentage of heads vs tails.
"""
import random
num_flip_coin=int(input("Enter number of times to flip coin: "))
tails=0
heads=0


for i in range(num_flip_coin):
    random_num = random.randint(0,1)    # generates random number between 0 and 1
    if (random_num < 0.5):

        print("tails")
        tails=tails+1
    else:
        print("heads")
        heads=heads+1

percetage_heads = (heads/num_flip_coin)*100
# percetage_tails = (tails/num_flip_coin)*100
percentage_tails = 100 - percetage_heads


print("Number of times Coin Fliped:",num_flip_coin)
print("Head count: ",heads)
print("Tail count: ",tails)
print("Head Percentage:",percetage_heads)
print("Tails Percentage:",percentage_tails)



