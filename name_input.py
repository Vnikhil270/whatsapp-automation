groups = []
 
# number of people/groups as input
n = int(input("\nEnter number of group-name/person you want to send message : "))

print("\nEnter the names of the groups/person's") 
# iterating till the range
for i in range(0, n):
    ele = input()
 
    groups.append(ele) # adding the element

print("\n Name of the groups/person's you entered\n")

for j in range(len(groups)):
    print(groups[j])
    print("\n")

