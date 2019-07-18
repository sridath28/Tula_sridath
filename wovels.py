sr = input()

if(sr=='A' or sr=='a' or sr=='E' or sr =='e' or sr=='I'
 or sr=='i' or sr=='O' or sr=='o' or sr=='U' or sr=='u'):
    print("Vowel")
elif(sr!="y"):
    print("Consonant")
else:
    print("Invalid")
