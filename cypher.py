#Jozua Kleu 18/11/2016

blank_list = []
original_text = input(" ")
text_list = list(original_text)
print ("original", text_list)
for i in text_list:
    blank_list.append(int(ord(i)))
print ("converted to integer format", blank_list)

base = (0)
for i in blank_list:
    blank_list[base+0] = blank_list[base+0] +2
    base += 1

print ("amount of letters", base)

text_list = ("")
for i in blank_list:
    text_list += chr(i)

print ("final coded message", text_list)
