def word(sent):
    words = sent.lower().split()
    freq = {}

    for w in words:
        freq[w] = freq.get(w, 0) + 1

    max_freq = max(freq.values())

    for w in words:
        if freq[w] == max_freq:
            return w 
sent = input()
print(word(sent))