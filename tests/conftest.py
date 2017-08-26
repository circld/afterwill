"""
Testing suite-wide shared fixtures and test data
"""
from afterwill.__main__ import initialize_parser
import pytest as pt


data_args = (
    ['-t', 'do thing1', 'do thing2', '-t', 'do something', 'do something else'],
    ['-t', 'eat', 'drink', 'sleep', 'wake up', 'go for a run']
)

data_formatted = (
    [['After I do thing1, I will do thing2'],
     ['After I do something, I will do something else']],
    [['After I eat, I will drink', 'After I drink, I will sleep', 'After I sleep, I will wake up', 'After I wake up, I will go for a run']]
)

data_output = (
    '\nAfter I do thing1, I will do thing2\n\nAfter I do something, I will do something else\n',
    '\nAfter I eat, I will drink\nAfter I drink, I will sleep\nAfter I sleep, I will wake up\nAfter I wake up, I will go for a run\n'
)


@pt.fixture(scope='session', autouse=True)
def parser():
    return initialize_parser()
