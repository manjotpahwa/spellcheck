
import enchant
from nltk.metrics import edit_distance
import argparse

class SpellingReplacer(object):
    def __init__(self, dict_name = 'en_GB', max_dist = 2):
        self.spell_dict = enchant.Dict(dict_name)
        self.max_dist = 2

    def replace(self, word):
        if self.spell_dict.check(word):
            return word
        suggestions = self.spell_dict.suggest(word)

        if suggestions and edit_distance(word, suggestions[0]) <= self.max_dist:
            return suggestions[0]
        else:
            return word



def spell_check(word_list):
    checked_list = []
    for item in word_list:
        print item
        replacer = SpellingReplacer()
        r = replacer.replace(item)
        checked_list.append(r)
    print checked_list
    return checked_list



if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("words", help="list of words to evaluate")
  args = parser.parse_args()
  words = str.split(args.words)
  spell_check(words)
