sentence="hello word how are you"
words=sentence.split()
result=""
for word in words:
    result += word[0].upper() + word[1:] + " "
print(result.strip())