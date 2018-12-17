from collections import OrderedDict

main_str = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

list = []

def words(string, dic = {}):
    for word in string.split():
        temp_word = ""
        for letter in word:
            if letter.isalpha():
                temp_word += letter
        list.append(temp_word)

    for word_in_list in list:
        if word_in_list in dic:
            i = dic[word_in_list]
            dic[word_in_list] = i + 1
        else:
            dic[word_in_list] = 1

    print("Words: ", dic)
    print("SortedWords: ", sorted_dic(dic))


def sorted_dic(dic):
    return OrderedDict(sorted(dic.items(), key = lambda x: x[1]))

words(main_str)

