order = [1,4,5,3,2]
friends = [2,5]
friends_dupe = []
for i in range(len(order)):
    for j in range(len(friends)):
        if order[i] == friends[j]:
            friends_dupe.append(friends.pop(j))
            break
print("Restored finishing order of friends:", friends_dupe)