l = ["hello","welcome","to","python","hello","welcome","world"]
uniq_strings = []
for i in l:
    if i not in uniq_strings:
        uniq_strings.append(i)
print(uniq_strings)
