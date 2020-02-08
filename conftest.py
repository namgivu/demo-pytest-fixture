import sys

def pytest_configure(config):
    sys._called_from_test = True  # mark it as running test

def pytest_unconfigure(config):
    del sys._called_from_test
