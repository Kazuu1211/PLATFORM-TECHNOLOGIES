def word(sentence):
    word_count = {}
    words = sentence.split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print("Word Prequencies:")
    for word, count in word_count.items():
        print(f" (word): {count}")

sentence = input("Enter a sentence: ")
word(sentence)
