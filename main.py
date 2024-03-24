from yay import kunal

hello = 4j
hello_string = '''Hello My name is {} and I am here to use python'''
query = 34
new_kunal = "this is new kunal string and I am very useful"
query_string = "kunal"


def joking_new_kunal(joking,yaay):
    print(new_kunal)
    print(joking)
    print(yaay)


joking_new_kunal("this is first string","this is second string")


def j_kunal():
    print("boom boom boom ")


if " is " in hello_string:
    print("The word is present in the above string")
else:
    print("word is absent in above string ")

hello_string = hello_string.format("kunal")

print(hello_string)
if query_string not in hello_string:
    print(query_string + " word is absent in the above text")
    print(hello_string.format(query_string))
else:
    print(hello_string.replace('kunal', 'null'))
    print("after formatting the null")

hi = bool('true')
print(hi)
kunal("kk calling")

j_kunal()
