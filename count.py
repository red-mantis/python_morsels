from collections import deque


def count_words(sentence):
    word_dict = {}
    init_a = deque(sentence.split())
    final_a = deque()
    for word in init_a:
        word_new = list()
        char_list = list(word)
        final_word = ""
        for char in char_list:
            if char_list.index(char) == 0 or char_list.index(char) == (len(char_list)-1):
                if char.isalpha():
                    word_new.append(char)
            else:
                word_new.append(char)
        final_word = "".join(word_new)
        final_a.append(final_word)
    for y in range(0,len(final_a)):
        b = final_a.popleft()
        if b in word_dict:
            count = word_dict[b]
            for x in final_a:
                if b == x:
                    count += 1
            word_dict[b] = count
        else:
            count = 1
            for x in final_a:
                if b == x:
                    count += 1
            word_dict[b] = count
    return word_dict


# print(count_words("oh what a day what a lovely day"))
# print(count_words("Oh what a day what a lovely day"))
# print(count_words("Oh what a day, what a lovely day!"))
# print(count_words("don't stop believing"))