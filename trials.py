"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums


def get_odd_indices(items):
    result = []

    for item in range(len(items)):
        if item % 2 != 0:
            result.append(items[item])

    return result


def print_as_numbered_list(items):
    num = 1

    for item in items:
        print(f"{num}. {item}")

        num += 1


def get_range(start, stop):
    result = []
    begin = start
    while begin < stop:
        result.append(begin)
        begin += 1

    return result


def censor_vowels(word):
    char = []
    vowels = "aeiou"

    for letter in word:
        if letter in vowels:
            char.append("*")
        else:
            char.append(letter)

    return "".join(char)


def snake_to_camel(string):
    camel_case = []

    for word in string.split("_"):
        camel_case.append(f"{word[0].upper()}{word[1:]}")

    return "".join(camel_case)


def longest_word_length(words):
    longest = len(words[0])
    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest


def truncate(string):
    result = []

    for char in string:
        if char not in result:
            result.append(char)

    return "".join(result)


def has_balanced_parens(string):
    parenopen = 0
    parenclose = 0

    for char in string:
        if char == "(":
            parenopen += 1
        if char == ")":
            parenclose += 1

    return parenclose == parenopen


def compress(string):
    compressed = []

    curr_char = ""
    char_count = 0
    for char in string:
        if char != curr_char:
            compressed.append(curr_char)

            if char_count > 1:
                compressed.append(str(char_count))

            curr_char = char
            char_count = 0

        char_count += 1

    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return "".join(compressed)
