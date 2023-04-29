#python statistics

"""import statistics
scores = [4, 5, 6, 7, 8, 9, 10, 20, 30]
a = statistics.mean(scores)
print(a)"""

"""import statistics
list = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9,]
b = statistics.median(list)
print(b)"""

"""import statistics
scores = [3, 5, 7, 9, 11, 13, 15, 17, 19]
c = statistics.mode(scores)
print(c)"""

#low median

"""import statistics
list1 = [10, 20, 30, 40, 50]
list2 = [60, 70, 80, 90, 100]
print("low median of list1 is : ", statistics.median(list1))
print("low median of list2 is : ", statistics.median(list2))"""

"""import statistics

list3 = [12, 13, 14, 15, 16]
list4 = [17, 18, 19, 20, 21]
print("high median of list3 is : ", statistics.median_high(list3))
print("high median of list4 is : ", statistics.median_high(list4))"""

# variance method
"""import statistics
data = [20, 30, 40, 50, 60, 70, 80, 90]
data_mean = statistics.mean(data)
print("variance of data is : ",statistics.variance(data,data_mean))"""

# standard deviation
import statistics
grades = [30, 40, 50, 60, 70, 80, 90, 100]
stdevgrades = statistics.stdev(grades)
print("The standard deviation of the list is : ",stdevgrades)


