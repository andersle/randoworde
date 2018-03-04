"""Tests for randoworde."""
import random
import tempfile
from randoworde import read_words, random_word, main


WORDS = [
    'pineapple',
    'banana',
    'apple',
    'orange',
    'horse',
    'battery',
    'staple'
]


WORDS_TXT = '\n'.join(WORDS)


def test_read_words():
    """Test that we can read dictionaries."""
    with tempfile.NamedTemporaryFile() as tmp:
        with open(tmp.name, 'w') as wordout:
            wordout.write(WORDS_TXT)
        tmp.flush()
        words = read_words(tmp.name)
        assert len(words) == len(WORDS)
        for i, j in zip(WORDS, words):
            assert i == j


def test_random_words():
    """Test generation of random words."""
    random.seed(0)
    correct = ['staporangepineapple', 'stapapporange', 'apbanana']
    for i in range(3):
        word = random_word(WORDS, maxw=3)
        assert word == correct[i]


def test_main():
    """Test the main function."""
    random.seed(123)
    correct = [
        'hermitagamorou',
        'lamazepirate',
        'mulos',
        'misintega',
        'ampi',
    ]
    gen_words = main(5)
    assert len(gen_words) == 5
    for i, j in zip(gen_words, correct):
        assert i == j
