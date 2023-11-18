sss = ["please wait", "continue to fight", "continue to win"]
num_words = [len(ss.split()) for ss in sss]
s = max(num_words)
print(s)