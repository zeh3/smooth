import json
import numpy as np 
import matplotlib.pyplot as plt

# ty to these tutorials/stackoverflow threads:
# https://pynative.com/python-parse-multiple-json-objects-from-file/
# https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
# https://stackoverflow.com/questions/28393103/typeerror-cannot-perform-reduce-with-flexible-type

def seven_day_rolling_average(array):
  new_averages = np.zeros(len(array) - 7)
  for i in range(7, len(array)):
    slice = array[i - 7:i]
    new_averages[i - 7] = np.sum(slice) / 7
  return new_averages

def make_cumulative(array):
  sum = np.zeros(len(array))
  for i in range(len(array)):
    sum[i] = array[i] + sum[i - 1]#sum[-1] is 0
  return sum


cases_filepath = "new_cases.json"

cases = []
rates = []

with open(cases_filepath) as jsonfile:
  for line in jsonfile:
    result = json.loads(line)["result"]
    cases.append(result["New Cases"])
    rates.append(result["Case Positivity %"])

cases = np.array(cases).astype(np.float)
cumulative_cases = make_cumulative(cases)
cases = seven_day_rolling_average(cases)

rates = np.array(rates).astype(np.float)
rates = seven_day_rolling_average(rates)

# graphing time

xlabel = "Days Since UIUC Saliva Testing Centers Opened"

plt.plot(cases)
plt.title("A Rolling Average of New Coronavirus Cases at UIUC")
plt.xlabel(xlabel)
plt.ylabel("Average New Cases Per Day")
plt.savefig("cases.png")
plt.clf()

plt.plot(rates)
plt.title("A Rolling Average of Coronavirus Positivity Rates at UIUC")
plt.xlabel(xlabel)
plt.ylabel("Average Positivity Rate")
plt.savefig("rates.png")
plt.clf()

plt.plot(cumulative_cases)
plt.title("Cumulative Coronavirus Cases at UIUC")
plt.xlabel(xlabel)
plt.ylabel("Cumulative Cases Since July 6, 2020")
plt.savefig("cumulative_cases.png")
plt.clf()

