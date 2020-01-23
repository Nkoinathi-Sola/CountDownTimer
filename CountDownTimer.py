import time 
# importing time exposes the functions e.g sleep()
# prompt user for input
seconds = int(input("Enter seconds")) 
# creat a loop for count down
for i in range(seconds):
    print(str(seconds - i) + " seconds remaining")
    time.sleep(1) # executes puthon sleep function between each loop
print("Time Up!")
