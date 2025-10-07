n=int(input("Enter the number of words: "))
words=[]
max_len=0
for i in range(n):
    word=input("Enter the word:")
    words.append(word)
for word in words:
    if len(word)>=max_len:
        max_len=len(word)
        lengthy_word=word
print("length of longest word",lengthy_word,'is',max_len)
