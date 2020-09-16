import psutil


cpuInfo = str(psutil.cpu_times())
result = cpuInfo.split(", ")

print(result)
# print(result)
#print("Time spent by normal processes executing in user mode")
#print(result[0].split("(")[1].split("=")[1], "second")

# print("Time spent by processes executing in kernel mode")
# print(result[2].split("=")[1], "seconds")

# print("blah blah blah")
# print(result[3])

# print("4th question")
#print(result[1])

# print("5th question")
# print(result[4], "seconds")

print("6thquestion")
print(result[5])
