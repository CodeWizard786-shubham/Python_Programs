"""
@Author: shubham shirke
@Date: 2023-06-02 15:10:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-02 15:10:30
@Title : To take in username as input and print in a sentence.
"""

username =input("Enter your name: ")
if len(username) >= 3:
    print(f"Hello {username},How are you?")
else:
    print("The string should have at least 3 characters.")