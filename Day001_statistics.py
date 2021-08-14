#python for Data science - sololearn
#Day001: statistics
"""
python library:
    pandas
    numpy
    matplotlib
"""

"""
why python?
    - easy to learn.
    -syntax is easy to read andunderstand.
"""

"""
Statistics:
    Mean: Average of a dataset.
    Median: middle value of an ordered dataset.
        -for odd number of dataset, we take median as middle one.
        -for even number of dataset, we take median as average of two middle datas.
-Generally, median is more prefferd upon mean since mean can vary a lot larger
or smaller as compared to other values.
-Measures of central tendency - descibes the center of a datset, like mean and median.
"""

"""
Standard deviation: is a measure of how spread out our data is, and is the 
square root of the variance.
Variance: average of squared differnce from the mean.

E.g. [14, 18, 19, 24, 26, 33, 42, 55, 67]
Mean = 33.1
variance = 292.5
standard deviation(std) = 17.1
range: (33.1 - 17.1) to (33.1 + 17.1)
[18, 19, 24, 26, 33, 42] falls in the range.

A low standard deviation indicates that the values tend to be close to the 
mean of the set, while a high standard deviation indicates that the values 
are spread out over a wider range.
"""

#statistics: code challenge
players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
mean = sum(players)/len(players)

list1 = []
for i in range(len(players)):
    list1.append((players[i]-mean)**2)

var = sum(list1)/len(list1)
std = (var)**(0.5)

lower = mean - std
upper = mean + std

list2 = []
for num in players:
    if lower < num < upper:
        list2.append(num)

print(len(list2))
