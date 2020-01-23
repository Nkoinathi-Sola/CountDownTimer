import time

seconds = int(input("Enter secnds"))

for i in range(seconds):
    print(str(seconds - i) + " seconds remaining")
    time.sleep(1)
print("Time Up!")