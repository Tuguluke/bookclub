phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

##indices = [1,2,4,7,6]
##ontap = [plist[index] for index in indices]
##ontap.insert(2," ")
##new_phrase = ''.join(ontap)

for i in range(4):
    plist.pop()

plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
