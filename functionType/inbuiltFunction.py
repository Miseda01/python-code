#x =30
#print(type(x))
#import builtins

#print(dir(builtins))
#import sys

#print(sys.builtin_module_names)

#import statistics

# Example data
#data = [3, 5, 7, 9, 14]

# Mean
#mean_value = statistics.mean(data)
#print("Mean:", mean_value)

# Median
#median_value = statistics.median(data)
#print("Median:", median_value)

# Mode
#mode_value = statistics.mode(data)
#print("Mode:", mode_value)

# Standard deviation
#stdev_value = statistics.stdev(data)
#print("Standard Deviation:", stdev_value)

def fibonacci_of(n):
    if n in {0, 1}:  # Base ca
      return n 
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)

for n in range(0,15):
    print(fibonacci_of(n))

print(type(fibonacci_of))