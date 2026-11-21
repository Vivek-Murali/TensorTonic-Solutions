def word_count_dict(sentences: list) -> dict:
    """
    Returns a dictionary of token counts.
    """
    # Write code here
    words:dict = {}

    if len(sentences)>0:
        for sentence in sentences:
            for word in sentence:
                if word in words:
                    words[word]+=1
                else:
                    words[word] = 1


    return words