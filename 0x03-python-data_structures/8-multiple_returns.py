#!/usr/bin/python3
def multiple_returns(sentence):
    k = len(sentence)
    if len(sentence) == 0:
        return (None)
    else:
        for c in sentence:
            return (k, sentence[0])
