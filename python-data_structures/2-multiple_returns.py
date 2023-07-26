def multiple_returns(sentence):
    if sentence == "":
        length = 0
        first = None
        return length, first
    else:
        length = len(sentence)
        first = sentence[0]
        return length, first
