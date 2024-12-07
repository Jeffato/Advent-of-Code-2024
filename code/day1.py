import numpy as np
from pathlib import Path
from collections import defaultdict

dir = Path(__file__).resolve().parent.parent / "input"
q1_file= "day1_input.txt"
q1_input = dir / q1_file

'''
Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are. 
Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, 
and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. 
For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.
'''
def day1_q1(input : str) -> float:
    # Input both lists as an array
    # Sort the array
    # Zip and find the difference
    # Sum Differences

    data = np.loadtxt(input)
    list1 = data[:,0]
    list2 = data[:,1]

    list1.sort()
    list2.sort()

    output = 0

    for i, j in zip(list1, list2):
        output += abs(i - j)
    
    return output

'''
This time, you'll need to figure out exactly how often each number from the left list appears in the right list. 
Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times 
that number appears in the right list.
'''
def day1_q2(input : str) -> float:
    # Input both lists as an array
    # Iterate through the right list and place into dict with key = number, val = frequency
    # Iterate through the left list and multiply by frequency in r_list dict

    data = np.loadtxt(input)
    list1 = data[:,0]
    list2 = data[:,1]
    output = 0

    list1.sort()
    list2.sort()

    r_list_frequency = defaultdict(int)

    for num in list2:
        r_list_frequency[num] += 1

    for num in list1:
        output += num * r_list_frequency[num]

    return output

if __name__ == "__main__":
    print(f'Part1: {day1_q1(q1_input)}, Part2: {day1_q2(q1_input)}')