def words_suffix(word):
    if word[-3:]=='ing':
        print(word+'ly')
    else:
        print(word+'ing')
word=input("Enter the word:")
words_suffix(word)
