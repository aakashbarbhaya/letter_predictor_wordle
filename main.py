import json
from generate_base import generate_base
from itertools import permutations

weighted_words_path = 'files/weighted_words_path.json'


def find_best_shortest_path_combination():
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


def get_best_two_word_permutation():
    weighted_word_json_file = open(weighted_words_path, 'r')
    weighted_words_json = json.load(weighted_word_json_file)
    list_of_words = list()
    for word in weighted_words_json:
        list_of_words.append(word.strip())
    permutations_of_words = permutations(list_of_words, 2)
    best_value = 0
    best_list = list()
    for combination in permutations_of_words:
        if len(set(list(combination[0])).intersection(set(list(combination[1])))) == 0:
            weighted_value = weighted_words_json[combination[0]] + weighted_words_json[combination[1]]
            if weighted_value > best_value:
                best_value = weighted_value
                best_list = combination
    print(best_list)
    weighted_word_json_file.close()
    return best_list


def get_best_three_word_permutation(list_of_best_two_words):
    weighted_word_json_file = open(weighted_words_path, 'r')
    weighted_words_json = json.load(weighted_word_json_file)
    list_of_words = list()
    for word in weighted_words_json:
        list_of_words.append(word.strip())
    best_value = 0
    best_list = list()

    accounted_characters = list()
    for combination_word in list_of_best_two_words:
        split_combination_word = list(combination_word)
        accounted_characters.extend(split_combination_word)

    for word in list_of_words:
        split_word = list(word)
        split_word_intersection = set(split_word).intersection(set(accounted_characters))
        if len(split_word_intersection) <= 1:
            if len(split_word_intersection.intersection({'a', 'e', 'i', 'o', 'u'})) == 0:
                list_of_best_three_words = list_of_best_two_words.append(word)
                print(list_of_best_two_words)
                break


def main(length):
    generate_base(length)
    find_best_shortest_path_combination()
    # uncomment if you want to run permutations
    # best_two_words = get_best_two_word_permutation()
    # overriding this
    best_two_words = ['eosin', 'ultra']
    get_best_three_word_permutation(best_two_words)



if __name__ == '__main__':
    main(5)
