# Author: James Trey Nickelsen
# File created: 08/07/2014

import re
import bisect

import phoneme_match

# TODO: guess_spelling
# TODO: guess_phonemes

def match_phonemes(word, phonemes):
    regex = ''.join('{}?'.format(phoneme_match.phoneme_to_symbol[phoneme]) for phoneme in phonemes)
    regex += '(.*)'
    phonemes = phonemes + ['']
    partitions = [[group, phonemes[phoneme_index]] for phoneme_index, group in
                  enumerate(re.match(regex, word).groups())]
    return partitions


def sequence_in_sequence(search, sequence):
    s = iter(search)
    index = -1
    try:
        for index, e in enumerate(sequence):
            if e != s.next():
                s = iter(search)
        index += 1
        s.next()
    except StopIteration:
        return index - len(search)
    return -1


def replace_part_of_word(word_dict, word, puns):
    if word in word_dict:
        phonemes = word_dict[word].instances[0]  # TODO: check all pronunciations

        partition = match_phonemes(word, phonemes)

        for pun in puns:
            index = sequence_in_sequence(pun[0], phonemes)
            if index != -1:
                for offset, pun_letters in enumerate(pun[1]):
                    partition[index + offset][0] = pun_letters

        for pair_index, pair in enumerate(partition):
            if pair[0] is None:
                pair[0] = ''
        return ''.join(pair[0] for pair in partition)
    return word


class SortedEntry:
    def __init__(self, word, phonemes):
        self.word = word
        self.phonemes = phonemes

    def __cmp__(self, other):
        return cmp(self.phonemes, other.phonemes)


def regenerate(sorted_dict, phonemes):
    if not phonemes:
        return []
    for length in range(min(len(phonemes), 9), 0, -1):
        for phoneme_index in range(len(phonemes)):
            end_index = min(len(phonemes), phoneme_index + length)
            index = bisect.bisect_left(sorted_dict, SortedEntry('', phonemes[phoneme_index:end_index]))
            if sorted_dict[index].phonemes == phonemes[phoneme_index:end_index]:
                return regenerate(sorted_dict, phonemes[:phoneme_index]) + [sorted_dict[index].word] + regenerate(
                    sorted_dict, phonemes[end_index:])
    return []


def to_phonemes(word_dict, string):
    phonemes = list()
    for word in re.split('[^A-Za-z\'\-]+', string):
        word = word.lower()
        if word in word_dict:
            phonemes += word_dict[word].instances[0]
    return phonemes


def map_to_sentence(function, sentence):
    def replace(match):
        return function(match.group(1))
    return re.sub(r'([a-zA-Z\']+)', replace, sentence)
