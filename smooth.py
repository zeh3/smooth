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
  print(new_averages)
  return new_averages

cases_filepath = "new_cases.json"

cases = []
rates = []

with open(cases_filepath) as jsonfile:
  for line in jsonfile:
    result = json.loads(line)["result"]
    cases.append(result["New Cases"])
    rates.append(result["Case Positivity %"])

print(type(cases))

cases = np.array(cases).astype(np.float)
cases = seven_day_rolling_average(cases)

rates = np.array(rates).astype(np.float)
rates = seven_day_rolling_average(rates)

plt.plot(cases)
plt.savefig("cases.png")
plt.clf()

plt.plot(rates)
plt.savefig("rates.png")

