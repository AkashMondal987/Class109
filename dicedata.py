import random
import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
diceResult = []
for i in range(0,1000):
    dice1= random.randint(1,6)
    dice2= random.randint(1,6)
    diceResult.append(dice1 + dice2)

mean = sum(diceResult)/len(diceResult)
stddeviation = statistics.stdev(diceResult)
median = statistics.median(diceResult)
mode = statistics.mode(diceResult)

firststdStart,firstStdEnd = mean - stddeviation,mean+stddeviation
secondstdStart,secondStdEnd = mean - (2*stddeviation),mean+(2*stddeviation)
thirdstdStart,thirdStdEnd = mean - (3*stddeviation),mean+(3*stddeviation)

fig = ff.create_distplot([diceResult],["Result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines", name = "MEAN"))
fig.add_trace(go.Scatter(x=[firststdStart,firststdStart],y=[0,0.17],mode="lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[firstStdEnd,firstStdEnd],y=[0,0.17],mode="lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[secondstdStart,secondstdStart],y=[0,0.17],mode="lines", name = "STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[secondStdEnd,secondStdEnd],y=[0,0.17],mode="lines", name = "STANDARD DEVIATION 2"))

listOfFirst = [result for result in diceResult if result>firststdStart and firstStdEnd]
listOfSecond = [result for result in diceResult if result>secondstdStart and secondstdStart]
listOfThird = [result for result in diceResult if result>thirdstdStart and thirdStdEnd]

print("Mean Of This Data Is:{}".format(mean))
print("Mode Of This Data Is:{}".format(mode))
print("Median Of This Data Is:{}".format(median))
print("Standard Deviation Of This Data Is:{}".format(stddeviation))

print("{}% of data lies within 1st Standard Deviation".format(len(listOfFirst)*100.0/len(diceResult)))
print("{}% of data lies within 2nd Standard Deviation".format(len(listOfSecond)*100.0/len(diceResult)))
print("{}% of data lies within 3rd Standard Deviation".format(len(listOfThird)*100.0/len(diceResult)))