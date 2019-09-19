

def random_words(amount):
    import loremipsum
    import re
    count = 0
    words = []
    while count < amount:
        sentence = loremipsum.get_sentence()[:-1]
        result = re.split(r'\s+|\.|,', sentence)
        if len(result) + count > amount:
            to_take = amount - count
            words.extend(result[:to_take])
            count = amount
        else:
            words.extend(result)
            count += len(result)

    return words


def random_words_as_string(amount, sep=' '):
    return sep.join(random_words(amount))


def random_sentences(amount):
    import loremipsum
    return loremipsum.get_sentences(amount)


def random_sentences_as_string(amount, sep=' '):
    return sep.join(random_sentences(amount))


def get_paragraphs(amount):
    import loremipsum
    return loremipsum.get_paragraphs(amount)