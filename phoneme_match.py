__author__ = 'janickelsen'

phoneme_to_symbol = {
    'AA': r'(ough|awe|au|aw|a|o)',  # dOg - Less rounded
    'AE': r'(a)',  # cAt
    'AH': r'(ah|uh|o|a|u|e|i|(?=l))',  # hUt
    'AO': r'(ough|au|aw|a|o)',  # OUGHt. More rounded
    'AW': r'(ough|iao|ou|ow|au|ao)',  # cOW
    'AY': r'(igh|ay|uy|aj|ai|ei|ie|i|y)',  # hIde
    'B': r'(bb|b)',  # Bone
    'CH': r'(tsch|tch|ch|cz|cc|t|c)',  # CHerry
    'D': r'(dd|d)',  # Dome
    'DH': r'(th)',  # broTHer
    'EH': r'(ae|ai|e|a)',  # rEd
    'ER': r'(erre|ear|our|yr|er|ur|ar|or|r)',  # hERd - Don't put forms with final e
    'EY': r'(ei|ay|ey|e|a)',  # hEY
    'F': r'(ff|ph|w(?=s)|f)',  # Far
    'G': r'(x|g|q)',  # Get - Part of X
    'HH': r'(wh|ch|j|h)',  # He
    'IH': r'(ee|ea|e|i|y)',  # It
    'IY': r'(ee|ea|e|i|y)',  # EEl
    'JH': r'(dg[a-z]?(?=[ei])|j|g)',  # Jack
    'K': r'((?<=s)ch|ck|c|k|x|q)',  # Kansas - Part of X
    'L': r'(al|el|le$|l)',  # Less
    'M': r'(m)',  # More
    'N': r'(kn|gn|n)',  # Next
    'NG': r'(ng|nk|n)',  # riNG
    'OW': r'(o)',  # tOme
    'OY': r'(oy|oi)',  # tOY
    'P': r'(p)',  # Pot
    'R': r'(r)',  # Rod
    'S': r'(ss|s|c)',  # Son
    'SH': r'(sh|s|t)',  # SHag
    'T': r'(t)',  # Tarn
    'TH': r'(th)',  # THing
    'UH': r'(oo|ou|o|u)',  # hOOd
    'UW': r'(oo|u|o)',  # tOO
    'V': r'(v|f)',  # Vase
    'W': r'(w|u)',  # Well
    'Y': r'(y|u)',  # Year
    'Z': r'(x|z|s)',  # Zap
    'ZH': r'(zh|x|g|j|z|s)'  # treaSure
}
