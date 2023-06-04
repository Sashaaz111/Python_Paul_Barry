def search4vowels(phrase):
    """Возвращает гласные, найденные в указанной фразе."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search4letters(phrase, letters='aeiou'):
    """Возвращает множество букв из `letters`, найденные в указанной фразе."""
    return set(letters).intersection(set(phrase))