import string

text = open("sample.txt", "r")
d = {}

for line in text:
    line = line.strip().lower()
    line = line.translate(line.maketrans("", "", string.punctuation))
    words = line.split()
    for word in words:
        d[word] = d.get(word, 0) + 1

for word in sorted(d.keys()):
    print(word, d[word])
