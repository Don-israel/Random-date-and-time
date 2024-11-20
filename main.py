import random #importing module
import time

def getRandomDate(startDate, endDate): #defining function
    print("Print random date between", startDate," and ", endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'
    startTime= time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))
    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomTime
#display result
print ("Random Date =", getRandomDate("1/1/2016", "12/12/2018"))