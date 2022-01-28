import json
from generate_base import generate_base

weighted_words_path = 'files/weighted_words_path.json'


def find_best_combination():
    weighted_word_json_file = open(weighted_words_path, 'r')
    weighted_words_json = json.load(weighted_word_json_file)

    combination_of_words = list()
    for word in weighted_words_json:
        if len(combination_of_words) == 0:
            combination_of_words.append(word.strip())

        accounted_characters = list()
        for combination_word in combination_of_words:
            split_combination_word = list(combination_word)
            accounted_characters.extend(split_combination_word)

        split_word = list(word)
        if len(set(split_word).intersection(set(accounted_characters))) == 0:
            combination_of_words.append(word.strip())

        elif len(combination_of_words) == 2:
            if len(set(split_word).intersection(set(accounted_characters))) <= 1:
                combination_of_words.append(word.strip())

        if len(combination_of_words) == 3:
            break

    print(combination_of_words)
    weighted_word_json_file.close()


def main(length):
    generate_base(length)
    find_best_combination()


if __name__ == '__main__':
    main(5)
