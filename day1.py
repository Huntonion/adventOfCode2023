## part 1 ##
import re
sum = 0
with open('txt/day1.txt') as f:
    for line in f:
        numbers = re.findall('[0-9]+', line)
        numberToSum = numbers[0][0] + numbers[-1][-1]
        sum = sum + int(numberToSum)
    print("part 1 solution: " + str(sum))
        
## part 2 ##
words = ["one","two","three","four","five","six","seven","eight","nine"]
numbers = ["1","2","3","4","5","6","7","8","9"]
sum = 0
counter = 1

with open('txt/day1.txt') as f:
    for line in f:
        leftMostPos = 50
        rightMostPos = 0
        leftMostEl = 0
        rightMostEl = 0
        for word,number in zip(words,numbers):
            iterator = 0
            lineBuffer = line.replace(word,number)
            for char in lineBuffer:
                if char.isdigit():
                    if(iterator < leftMostPos):
                        leftMostPos = iterator
                        leftMostEl = lineBuffer[iterator]
                    if(iterator > rightMostPos):
                        rightMostPos = iterator
                        rightMostEl = lineBuffer[iterator]
                    if(rightMostPos == leftMostPos):
                        rightMostEl = 0
                iterator = iterator + 1
        print(str(counter)+":" + str(leftMostEl)+ " "+str(rightMostEl))
        numToSum = str(leftMostEl)+str(rightMostEl)
        numToSum2 = numToSum.replace('0','')
        print(numToSum2)
        sum  = sum + int(numToSum2)
        print(sum)
        counter = counter + 1

    print("part 2 solution: " + str(sum))