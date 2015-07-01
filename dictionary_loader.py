__author__ = 'janickelsen'

import re

phonetic_dictionary = "cmudict.0.7a"


class WordInfo:
    def __init__(self):
        self.instances = []
        self.part_of_speech = ''


def simplify_phonemes(phoneme):
    phoneme = phoneme[:2]  # Cut off stress if present
    if phoneme == 'AO':
        return 'AA'
    return phoneme


def load_dictionary():
    word_dict = dict()
    with open(phonetic_dictionary) as file_dict:
        num_entries = 0
        for line in file_dict:
            if line[:2] == ';;;':
                continue
            match = re.match(r"([A-Z\-']+)(\([0-9]\))?  ([A-Z0-9 ]+)", line)
            if match:
                phonemes = map(simplify_phonemes, match.group(3).split(' '))
                if match.group(1).lower() in word_dict:
                    word_dict[match.group(1).lower()].instances.append(phonemes)
                else:
                    word_info = WordInfo()
                    word_info.instances.append(phonemes)
                    word_dict[match.group(1).lower()] = word_info
                num_entries += 1
        print 'Successfuly imported {} entries'.format(num_entries)
    return word_dict
