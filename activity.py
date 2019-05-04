"""Prints a maximum set of activities that can be done by a
single person, one at a time"""
# n --> Total number of activities
# s[]--> An array that contains start time of all activities
# f[] --> An array that contains finish time of all activities
 
def printMaxActivities(s , f ):
    n = len(f)
    print ("The following activities are selected")
 
    # The first activity is always selected
    i = 0
    print (i),
 
    # Consider rest of the activities
    for j in range(n):
 
        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if s[j] >= f[i]:
            print (j),
            i = j
 
# Driver program to test above function
#s = [1 , 3 , 0 , 5 , 8 , 5]
#f = [2 , 4 , 6 , 7 , 9 , 9]
print ("enter start time of the activities")
s=list(map(int,input().split()))

print ("enter finish time of the activities")
f=list(map(int,input().split()))

#if not sorted applying bubble sort
for i in range(len(f)):
    for j in range(len(f)-i-1):
        if f[j]>f[j+1]:
            f[j],f[j+1],s[j],s[j+1]=f[j+1],f[j],s[j+1],s[j]
            
printMaxActivities(s , f)
 

