# First algorithm without max() or sort()
# Date: June 10, 2026
# Status: FLAWLESS VICTORY

sakshi = []
even_count = 0

for i in range(1, 6):
    num = int(input("enter your number: "))
    sakshi.append(num)
    if num % 2 == 0:
        print(num, "it's Even")
        even_count += 1
    else:
        print(num, "it's odd")

greatest = sakshi[0]
smallest = sakshi[0]
second_greatest = -999999

for num in sakshi:
    if num > greatest:
        second_greatest = greatest
        greatest = num
    elif num > second_greatest and num!= greatest:
        second_greatest = num
    if num < smallest:
        smallest = num

print("greatest number:", greatest)
if second_greatest == -999999:
    print("second_greatest number: None - all numbers same")
else:
    print("second_greatest number:", second_greatest)
print("smallest number:", smallest)
print("total even number:", even_count)
