import random
low=1
high=100
mid=(low+high)/2
attempts =0
number=random.randint(low, high)
while True:
    if number == mid:
        print("CONGRATS")
        break
    elif number < mid:
        high=mid -1
        attempts+=1
        mid= (low+high)/2
    else:
        low=mid+1
        mid=(low+high)/2
        attempts+=1