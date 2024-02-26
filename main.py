hello = 4j
hello = '''Hello My name is {} and I am here to use python'''
query = 34
query = "kunal"
if " is " in hello:
    print("The word is present in the above string")
else:
    print("word is absent in above string ")

hello = hello.format("kunal")
print(hello)
if query not in hello:
    print(query + " word is absent in the above text")
    print(hello.format(query))
else:
    print(hello.replace('kunal', 'null'))
    print("after formatting the null")
hi = bool('true')
print(hi)
