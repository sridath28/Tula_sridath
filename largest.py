nn1 = input()
nn2 = input()
nn3 = input()
 
if (nn1 > nn2) and (nn1 > nn3):
   largest = nn1
elif (nn2 > nn1) and (nn2 > nn3):
   largest = nn2
else:
   largest = nn3
 
print("largest")
