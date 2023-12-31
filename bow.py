def bag_of_words(document):
    doc_tokenized = document.split(' ')
    vocab = dict()
    bow = list()

    for word in doc_tokenized:
        if word not in vocab.keys()
            vocab[word] = len(vocab)
            bow.append(1)
        else:
            word_index = vocab.get(word)
            bow[word_index] += 1
    return vocab, bow