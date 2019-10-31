#https://dmoj.ca/problem/ccc12j2

# previousvalue = None
# fishRising = None
# fishDiving = None 

# for i in range(0,4):
#     currentValue = int(input())
#     if not(previousvalue is None):
#         if fishRising is True:             
#             if currentValue > previousvalue:
#                 if fishRising is None:
#                     fishRising = True
                
#     previousvalue = currentValue
    

entry1 = int(input())
entry2 = int(input())
entry3 = int(input())
entry4 = int(input())

if entry1 < entry2 and entry2 < entry3 and entry3 < entry4:
    print("Fish Rising")
elif entry1 > entry2 and entry2 > entry3 and entry3 > entry4:
    print("Fish Diving") 
elif entry1 == entry2 and entry2 == entry3 and entry3 == entry4:
    print("Fish At Constant Depth")
else:
    print("No Fish")