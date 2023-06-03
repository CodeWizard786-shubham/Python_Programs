"""
@Author: shubham shirke
@Date: 2022-06-03 13:44:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-03 13:44:30
@Title : Python stop watch program to find elapsed time between start and stop keyboard click.
"""
import time

def time_convert(sec):
  """
  Description : The function calculates and prints the lapsed time between start and stop clicks.
  Parameters : sec - time in seconds collected using time.time() function.
  result : time_lapsed in a format of hours,minutes and seconds. 
  """
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))   # print format for lapsed time

def main():
    input("Press Enter to start: ")
    start_time = time.time()    # collects time in seconds.

    input("Press Enter to stop: ")
    end_time = time.time()     # collects time in seconds.

    time_lapsed = end_time - start_time
    time_convert(time_lapsed)   # calling the time_convert function and passing the time_lapsed parameter.

if __name__ == "__main__":
    main()