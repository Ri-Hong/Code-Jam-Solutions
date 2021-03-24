'''
Author: Ri Hong
Date Solved: March 24, 2021
Problem: https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f
'''

#Explanation
'''
This problem can be solved by looping through the string of numbers and surrounding each character with the it's desired number of brackets. 
For example, if the input was 1234, we would turn it into (1)((2))(((3)))((((4))))

Then, we need to simplify to eliminate the redundant brackets. We can observe that if there is a closing bracket next to an opening bracket, those two
brackets can be removed to simpify our string.

We keep removing the redundant brackets until there are no more redundant brackets and that is when we will arrive at our solution
'''

numTestCases = int(input())

for case in range(numTestCases):
    S = input()
    #surrounding each character with the it's desired number of brackets
    SWithBrackets = ""
    for char in S:
        numBrackets = int(char)
        SWithBrackets += '('*numBrackets
        SWithBrackets += char
        SWithBrackets += ')'*numBrackets

    #removing the redundant brackets
    condensable = True
    while condensable: #keep looping while there are still redundant brackets
        condensedS = ""
        condensed = False
        skipNextTurn = False
        for i in range(len(SWithBrackets)-1):
            if skipNextTurn:
                skipNextTurn = False
                continue
            if SWithBrackets[i] == ')' and SWithBrackets[i+1] == '(': #Skip next turn if we arrive at a redundant pair of brackets
                skipNextTurn = True
                condensed = True
            else:
                condensedS += SWithBrackets[i]
        condensedS += SWithBrackets[-1]
        #check if still need to keep looping 
        if condensed == True:
            SWithBrackets = condensedS
        else:
            condensable = False

    print("Case #{}: {}".format(case + 1, condensedS))