import time

start = time.time()
count = 0
with open("H:\log\log") as file:
	for line in file:
	    print(line)
	    count = count + 1
end = time.time()
print("Execution time in seconds: ",(end-start))
print("No of lines printed: ",count)
