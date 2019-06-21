"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["abc"],
            "answer": "a"
        },
        {
            "input": ["abacada"],
            "answer": "aba"
        },
        {
            "input": ["artrartrt"],
            "answer": "rtrartr"
        },
        {
            "input": ["aaaaa"],
            "answer": "aaaaa"
        }

    ],
    "Extra": [
        {
            "input": ["so sad das-li"],
            "answer": "sad das"
        },
        {
            "input": [" a b c"],
            "answer": " a "
        },
        {
            "input": ["1"],
            "answer": "1"
        },
        {
            "input": ["123abcba"],
            "answer": "abcba",
            "explanation": "At the end of text"
        },
        {
            "input": ["abcba123abcdcba"],
            "answer": "abcdcba",
            "explanation": "Two palindromes in text"
        }
    ]
}
