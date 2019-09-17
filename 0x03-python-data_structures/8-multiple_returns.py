#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        tupla = len(sentence), None
        return tupla
    tupla = len(sentence), sentence[0]
    return tupla
