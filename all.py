import csv
with open(r"F:\Python Files\Mean, Median and Mode\SOCR-HeightWeight.csv",newline="")as f:
    reader = csv.reader(f)
    file_list = list(reader)
    file_list.pop(0)
    newData = []
    for i in range(len(file_list)):
        n_num = file_list[i] [1]
        newData.append(float(n_num))
        # getting mean 
n = len(newData)
total = 0
for x in newData:
    total+=x
mean = total/n
# getting median
n= len(newData)
newData.sort()
# Using floor division to get the nearest whole number
# Floor division is shown by//
if n%2 == 0:
    # Getting the first number
    median1 = float(newData[n//2])
    # Getting the second number
    median2 = float(newData[n//2-1])
    median = (median1+median2)/2

else:
    median = newData[n//2]
from collections import Counter

with open(r"F:\Python Files\Mean, Median and Mode\SOCR-HeightWeight.csv",newline="")as f:
    reader = csv.reader(f)
    file_list = list(reader)
file_list.pop(0)
newData = []
for i in range(len(file_list)):
    n_num = file_list[i] [1]
    newData.append(float(n_num))
data = Counter(newData)
mode_data_for_range = {
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for height, occurence in data.items():
    if 50<float(height)<60:
        mode_data_for_range["50-60"]+= occurence
    elif 60<float(height)<70:
        mode_data_for_range["60-70"]+= occurence
    elif 70<float(height)<80:
        mode_data_for_range["70-80"]+= occurence
mode_range, mode_occurence = 0,0
for range, occurence in mode_data_for_range.items():
    if occurence>mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence
mode = float((mode_range[0]+mode_range[1])/2)
print("Mean or average is:-"+str(mean))
print("Median is:-"+str(median))
print(f"Mode is:-{mode:2f}")
