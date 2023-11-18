n = int(input())
words = []
for i in range(n):
    words.append(input())

shortened_words = []
for word in words:
    prefix = ""
    suffix = ""
    for i in range(len(word)-2):
        if word[:i+1] == word[-i-1:]:
            prefix = word[:i+1]
            suffix = word[-i-1:]
            break
    if prefix == "" or suffix == "":
        shortened_words.append(word)
    else:
        n = len(word) - len(prefix) - len(suffix)
        shortened_words.append(prefix + str(n) + suffix)

for shortened_word in shortened_words:
    print(shortened_word)
print(shortened_words)
