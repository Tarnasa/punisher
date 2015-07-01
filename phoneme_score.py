__author__ = 'janickelsen'

# https://en.wikipedia.org/wiki/Vowel_diagram
# https://msu.edu/course/asc/232/Charts/Tense-Lax_Vowels.html

vowels_source = \
"""
AA 1.0 1.0 0.0 1.0
AE 0.4 1.0 0.0 0.0
AH 1.0 0.7 0.0 0.0
AO 1.0 0.7 1.0 1.0
AW -1. -1. -1. 0.0
AY 0.4 -1. 0.0 0.0
EH 0.3 0.5 0.0 0.0
ER 0.6 0.5 1.0 1.0
EY 0.1 0.2 0.0 1.0
IY 0.0 0.0 0.0 1.0
OW 1.0 0.3 1.0 1.0
OY -1. 0.5 -1. 0.0
UH 0.7 0.2 0.5 0.0
UW 1.0 0.0 1.0 1.0
"""

# https://en.wikipedia.org/wiki/General_American

# x, voiced, plosive, nasal, fricative, approx?
consonants_source = \
"""
B 0 1 1 0 0 0 0
CH 3 0 1 0 0.2 0 0
D 2 1 1 0 0 0 0
DH 1 1 0 0 1 0 0
F 0 0 0 0 1 0 0
G 5 1 1 0 0 0 0
HH 6 0.5 0 0 1 0 0
JH 3 1 1 0 0.2 0 0
K 5 0 1 0 0 0 0
L 2 1 0 0 0 0 1
M 0 1 0 1 0 0 0
N 2 1 0 1 0 0 0
NG 5 1 0 1 0 0 0
P 0 0 1 0 0 0 0
R 2.5 1 0 0 0 1 0
S 2 0 0 0 1 0 0
SH 3 0 0 0 1 0 0
T 2 0 1 0 0 0 0
TH 1 0 0 0 1 0 0
V 0 1 0 0 1 0 0
W 5 1 0 0 0 1 0
Y 4 1 0 0 0 1 0
Z 2 1 0 0 1 0 0
ZH 3 1 0 0 1 0 0
"""


class Vowel:
    def __init__(self, symbol, closeness=0.0, backness=0.0, roundness=0.0, tenseness=0.0):
        """
        :param symbol: string
        :param closeness: float
        :param backness: float
        :param roundness: float
        :param tenseness: float
        """
        self.symbol = symbol
        self.closeness = closeness
        self.backness = backness
        self.roundness = roundness
        self.tenseness = tenseness

    def to_tuple(self):
        return (
            self.closeness,
            self.backness,
            self.roundness,
            self.tenseness,
        )

    def distance(self, other):
        """
        :param other: Vowel
        :return: float
        """
        return sum(((self.closeness - other.closeness) ** 2.0,
                    (self.backness - other.backness) ** 2.0,
                    (self.roundness - other.roundness) ** 2.0,
                    (self.tenseness - other.tenseness) ** 2.0)) ** 0.5


class Consonant:
    def __init__(self, place, symbol, voiced, plosive, nasal, fricative, approx, lateral_approx):
        """
        :param symbol: string
        :param place: float
        :param voiced: float
        :param plosive: float
        :param nasal: float
        :param fricative: float
        :param approx: float
        :param lateral_approx: float
        """
        self.symbol = symbol
        self.place = place
        self.voiced = voiced
        self.plosive = plosive
        self.nasal = nasal
        self.fricative = fricative
        self.approx = approx
        self.lateral_approx = lateral_approx

    def to_tuple(self):
        return (
            self.place,
            self.voiced,
            self.plosive,
            self.nasal,
            self.fricative,
            self.approx,
            self.lateral_approx,
        )

    def distance(self, other):
        """
        :param other: Consonant
        :return: float
        """
        return sum((
            (self.place - other.place) ** 2.0,
            (self.voiced - other.voiced) ** 2.0,
            (self.plosive - other.plosive) ** 2.0,
            (self.nasal - other.nasal) ** 2.0,
            (self.fricative - other.fricative) ** 2.0,
            (self.approx - other.approx) ** 2.0,
            (self.lateral_approx - other.lateral_approx) ** 2.0,
        )) ** 0.5


vowels = list()
for line in vowels_source.split('\n'):
    parts = line.split(' ')
    if len(parts) != 5:
        continue
    vowels.append(Vowel(
        symbol=parts[0],
        closeness=float(parts[1]),
        backness=float(parts[2]),
        roundness=float(parts[3]),
        tenseness=float(parts[4]),
    ))

consonants = list()
for line in consonants_source.split('\n'):
    parts = line.split(' ')
    if len(parts) != 8:
        continue
    consonants.append(Consonant(
        symbol=parts[0],
        place=float(parts[1]),
        voiced=float(parts[1]),
        plosive=float(parts[2]),
        nasal=float(parts[3]),
        fricative=float(parts[4]),
        approx=float(parts[5]),
        lateral_approx=float(parts[6]),
    ))
