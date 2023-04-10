hour = 2 #target of desired amount of time to run the experiment
min = hour*60
ml = 3
flow_rates = [1, 2, 5, 10, 15, 20, 25, 30, 100] #examples of typical flow rates
list_ul = []
for i in flow_rates:
    x = i*min
    list_ul.append(x)

list_ml = []
for y in list_ul:
    list_ml.append(y*0.001)
print("In mls, for " + str(hour) + "hrs:")
print(list_ml)
print("With flow rates (im ul/min): ")
print(flow_rates)

for i in range(0, len(flow_rates)+1):
    flow_rate = flow_rates[i]
    volume = list_ml[i]
    print("For a flow rate of " + str(flow_rate) + " um/min, " + str(volume) + " ml of reagent solution will be used in " + str(hour) + " hours.")


