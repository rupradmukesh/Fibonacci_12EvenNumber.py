# Count the number of innings Sachin scored less than 25 runs in 2001
FH = open("sachin_runs.csv")
All_Text = FH.read()
# print(All_Text)
TextList = All_Text.split('\n')
print(TextList)
count = 0
for run in TextList[1:-1]:
    run_St = run.strip(',')
    # print(run1)
    if int(run_St) < 25:
        count += 1
print("Number of innings Sachin scored less than 25 runs in 2001 =", count)
print("-"*50)
# Fill the missing pieces in the below line to get the list of runs scored by
# Sachin in 2001.
runs = [ num.strip(',') for num in open("sachin_runs.csv").read().split() ][9:]                                                                        
#print(runs)
# Use the above "runs" list to find out the number of innings Sachin scored
# less than 25 runs
count = 0
for run in runs:
    #print(run)
    if int(run) < 25:
        count += 1
print("Number of innings Sachin scored less than \n25 runs in 2001 using given code =", count)
print("-"*50)
# A Journalist makes a claim that in 2001, Sachin scored less than 33 runs,
# in less than 33% of his innings
countLess33 = 0
Totalcount = 0
for run in runs:
    #print(run)
    Totalcount += 1
    if int(run) < 33:
        countLess33 += 1
print("Tolal Number of innings = ", Totalcount)
print("Total count score less than 33 run = ", countLess33)
if ((countLess33 * 100)//Totalcount) < 33 :
    print("Journalist claim is true")
else:
    print("Journalist claim is false")

print("-"*50)       
# Write Python code to check the claim made by this Journalist
## YOUR CODE GOES HERE ##
# Already writte above

# A Commentator then claims that in 2001, Sachin's score on an average,
# crossed half a century in at least one of every 2 innings.
count2ndIn = 0
PrevInRun = 0
setFlag = False
for run2ndIn in runs:
    AvgRun =  PrevInRun + int(run2ndIn)
    count2ndIn += 1
    if AvgRun < 50 and count2ndIn == 2:
        setFlag = True
    elif count2ndIn == 2:
            count2ndIn = 0
    PrevInRun = int(run2ndIn)
print(setFlag)
if setFlag:
    print("average score,crossed half a century in at least one of every 2 innings is false")

else:
    print("average score,crossed half a century in at least one of every 2 innings is true")
print("-"*50)
# Write Python code to check the claim made by this Commentator
## YOUR CODE GOES HERE ##
# Already writte above
FH.close()
