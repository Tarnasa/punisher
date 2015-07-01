__author__ = 'janickelsen'

import re
import itertools
import random

import dictionary_loader
import make_puns
import phoneme_score

word_dict = dictionary_loader.load_dictionary()

sorted_dict = list(make_puns.SortedEntry(word, word_info.instances[0]) for word, word_info in word_dict.iteritems())
sorted_dict.sort()


def full_regeneration(sentence):
    return ' '.join(make_puns.regenerate(sorted_dict, make_puns.to_phonemes(word_dict, sentence)))


def cat_talk(word):
    puns = [
        ['P AA', 'p aw'],
        ['K AE T', 'c a t'],
        ['T EY L', 't ai l'],
        ['F AH R', 'f u r'],
        ['F ER', 'f ur'],
        ['IY R', 'ea r'],
        ['T UW N UH', 't u n a'],
        ['P AW N S', 'p ou n ce'],
    ]
    puns = [[pair[0].split(' '), pair[1].split(' ')] for pair in puns]

    return make_puns.replace_part_of_word(word_dict, word, puns)


def look_for_phoneme_sequence(phoneme_sequence):
    results = list()
    for word, word_info in word_dict.iteritems():
        for phonemes in word_info.instances:
            match = re.search(' '.join(phoneme_sequence), ' '.join(phonemes))
            if match:
                results.append(word)
                break
    return results


def find_similar_phonemes():
    print('Vowels:')
    delta = 0.4

    for a, b in itertools.combinations(phoneme_score.vowels, 2):
        if a.distance(b) <= delta:
            print('{} is close to {}'.format(a.symbol, b.symbol))
    print('Consonants:')
    delta = 1.0
    for a, b in itertools.combinations(phoneme_score.consonants, 2):
        if a.distance(b) <= delta:
            print('{} is close to {}'.format(a.symbol, b.symbol))


def random_word_replacement(word):
    phonemes = make_puns.to_phonemes(word_dict, word)
    while True:
        start = random.randint(0, len(phonemes) - 1)
        stop = random.randint(start, len(phonemes))
        substitution = ''.join(make_puns.regenerate(sorted_dict, phonemes[start:stop]))
        if substitution and substitution != word:
            print(substitution)
            break

    partitions = make_puns.match_phonemes(substitution, phonemes[start:stop])
    print(partitions)
    puns = [[[], []]]
    for pair in partitions:
        if pair[1]:
            puns[0][0].append(pair[1])
            if pair[0]:
                puns[0][1].append(pair[0])
            else:
                puns[0][1].append('')
        else:
            puns[0][1][-1] += pair[0]

    print(puns)
    return make_puns.replace_part_of_word(word_dict, word, puns)


if __name__ == '__main__':
    sentence = 'The tale of the pausing photographer'

    print(make_puns.map_to_sentence(cat_talk, sentence))
    print(full_regeneration(sentence))

    for _ in range(1):
        print(random_word_replacement('photographer'))
