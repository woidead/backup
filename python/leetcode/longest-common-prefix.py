# def longestCommonPrefix(strs):
#         c = 0
#         d = []
#         for i in d:
#             if strs[0][c] == strs[1][c]:
#                 d.append(strs[0][c])
#                 c=+1
            
#         print(d)

# longestCommonPrefix(["flower","flow","flight"])



# strs = ["flower","flow","flight"]
# strs.sort()
# print(strs)
# first = strs[0]
# print(enumerate(first))


def longestCommonPrefix( strs: list[str]) -> str:
        if not strs:
            print("")
        if len(strs) == 1:
            print( strs[0])
        strs.sort()
        first = strs[0]
        last = strs[-1]
        for index, value in enumerate(first):
            if value != last[index]:
                print(first[:index])
        print(first)
longestCommonPrefix(["ab", "a"])