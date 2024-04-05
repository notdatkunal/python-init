friends1 = ["kunal", True, 3]
friends1[0] = 99
friends = ["kunal", "atharva", "saurabh", "akash", "ritisha", "madhuri", "priyanka"]

friends.extend(friends1)
friends.append("one item")
friends.insert(0, "first element")
friends.remove(True)
print(friends)
print(friends[3:])
print(friends1)
print(friends.pop())

print(friends)
