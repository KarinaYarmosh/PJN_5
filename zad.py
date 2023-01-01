import re

def f():
    # consonants = "bcdfghjklmnpqrstvwxz"
    # vowels = "aeiouy"
    _vowels = "[eyuoai]"
    _consonants = "[bcdfghjklmnpqrstvwxz]"

    # Word regions.
    _re_vowels = re.compile(_vowels)
    print(_re_vowels)

    _re_consonants = re.compile(_vowels + _consonants)
    print(_re_consonants)

def gerund(stem):
    stem2 = re.sub(r'(ing|ings|ed)$', '', stem)
    if stem == stem2:
        adjective(stem)
    else:
        print(stem2)

def adjective(stem):
    stem2 = re.sub(r'(al|ful|ic|able|ible|ant|ement|'
                   r'ment|ent|ism|ate|iti|ous|ive|ize|ise|less|ie|ual|ness)$', '', stem)
    if stem == stem2:
        participle(stem)
    else:
        print(stem2)

def participle(stem):
    stem2 = re.sub(r'(ne|ing|n)$', '', stem)
    if stem == stem2:
        reflexive(stem)
    else:
        print(stem2)
        step2(stem2)

def reflexive(stem):
    stem2 = re.sub(r'(self|selves)$', '', stem)
    if stem == stem2:
        verb(stem)
    else:
        print(stem2)
        step2(stem2)

def verb(stem):
    stem2 = re.sub(r'(s|ies|es|d)$', '', stem)
    if stem == stem2:
        noun(stem)
    else:
        print(stem2)
        step2(stem2)

def noun(stem):
    stem2 = re.sub(r'(s|es|ies|ves)$', '', stem)
    if stem == stem2:
        superlative(stem)
    else:
        print(stem2)
        step2(stem2)

def superlative(stem):
    stem2 = re.sub(r'(est|er)$', '', stem)
    if stem == stem2:
        derivational(stem)
    else:
        print(stem2)
        step2(stem2)

def derivational(stem):
    stem2 = re.sub(r'(ent|er|ly)$', '', stem)
    if stem == stem2:
        ww(stem)
    else:
        print(stem2)
        step2(stem2)

def ww(stem):
    stem2 = re.sub(r'(wise|ward)$', '', stem)
    if stem == stem2:
        #noun(stem)
        print(stem2)
        pr(stem2)
    else:
        print(stem2)
        step2(stem2)

def pr(stem):
    stem2 = re.sub(r'(ness|hood|ity|ety|iety)$', '', stem)
    if stem == stem2:
        #noun(stem)
        print(stem2)
        step2(stem2)
    else:
        print(stem2)
        step2(stem2)

def step2(stem):
    stem2 = re.sub(r'^(un|dis|side|back|in|out|a|de|mis|pre|fore|under|over|'
                   r'im|il|ir|en|re|be|non|post|super)', '', stem)
    if stem == stem2:
        print(stem2)
    else:
        print(stem2)

def main():
    with open("diffs.txt", "rt", encoding="utf-8") as diffs_file:
        diffs = diffs_file.readlines()
    for i, line in enumerate(diffs):
        stem = line
        print(stem)
        gerund(stem)
        #f()

if __name__ == "__main__":
    main()