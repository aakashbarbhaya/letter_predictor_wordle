import json

all_word_file_path = 'files/all_words.txt'
find_words_for_length_path = 'files/find_words_for_length.txt'
unique_words_for_length_path = 'files/unique_words_for_length_path.txt'
weighted_character_dict_path = 'files/weighted_character_dict.json'
weighted_words_path = 'files/weighted_words_path.json'


def find_words_for_length(length):
    read_file = open(all_word_file_path, 'r')
    write_file = open(find_words_for_length_path, 'w')
    words = read_file.readlines()
    for word in words:
        if len(word.strip()) == length:
            write_file.writelines(word.strip() + '\n')
    read_file.close()
    write_file.close()


def create_weighted_character_dict():
    character_dict = dict()
    read_file = open(find_words_for_length_path, 'r')
    write_file = open(weighted_character_dict_path, 'w')
    words = read_file.readlines()

    for word in words:
        split_list = list(word.strip())
        for character in split_list:
            if character in character_dict:
                character_dict[character] = character_dict[character] + 1
            else:
                character_dict[character] = 1
    sorted_character_dict = dict(sorted(character_dict.items(), key=lambda item: item[1], reverse=True))
    sum = 0
    for character_key, character_value in sorted_character_dict.items():
        sum = sum + character_value

    weighted_character_dict = dict()
    for character_key, character_value in sorted_character_dict.items():
        weighted_character_dict[character_key] = (character_value / sum) * 100

    write_file.write(json.dumps(weighted_character_dict, indent=4))
    read_file.close()
    write_file.close()


def create_list_of_words_with_unique_characters():
    read_file = open(find_words_for_length_path, 'r')
    write_file = open(unique_words_for_length_path, 'w')
    words = read_file.readlines()
    for word in words:
        if len(set(word)) == len(word):
            write_file.writelines(word)
    read_file.close()
    write_file.close()


def create_weighted_word_list():
    character_weight_json_file = open(weighted_character_dict_path, 'r')
    character_weight_json = json.load(character_weight_json_file)

    read_file = open(unique_words_for_length_path, 'r')
    write_file = open(weighted_words_path, 'w')

    words = read_file.readlines()
    weighted_word_dict = dict()

    for word in words:
        split_word = list(word.strip())
        sum = 0
        for character in split_word:
            sum = sum + character_weight_json[character]
        weighted_word_dict[word.strip()] = sum

    sorted_weighted_word_dict = dict(sorted(weighted_word_dict.items(), key=lambda item: item[1], reverse=True))
    write_file.write(json.dumps(sorted_weighted_word_dict, indent=4))
    read_file.close()
    write_file.close()


def generate_base(length):
    find_words_for_length(length)
    create_weighted_character_dict()
    create_list_of_words_with_unique_characters()
    create_weighted_word_list()
