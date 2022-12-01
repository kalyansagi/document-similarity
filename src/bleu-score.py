def convertTextToWords():

    candidate1 = ["It is a guide to action which ensures that the military always obeys the commands of the party."]
    # data = ['a a b c h d b f', 'b c h h a d f f a h b', 'b b a a h h c c h d d f', 'a b f f h c c d f f h', 'h h f c f c a a c c d d d ']
    dat = []
    for i in range(len(candidate1)):
        for word in candidate1[i].split():
            dat.append(word)
    print(dat)
    return dat

def bigramFunction(data):
    bigram_list = []
    bigram_counts = {}
    unigram_counts = {}
    for i in range(len(data) - 1):
        if i < len(data) - 1 and data[i + 1].islower():

            bigram_list.append((data[i], data[i + 1]))

            if (data[i], data[i + 1]) in bigram_counts:
                bigram_counts[(data[i], data[i + 1])] += 1
            else:
                bigram_counts[(data[i], data[i + 1])] = 1

        if data[i] in unigram_counts:
            unigram_counts[data[i]] += 1
        else:
            unigram_counts[data[i]] = 1
    return bigram_list, unigram_counts, bigram_counts

def calculate_bigram_probability(list_of_bigrams, unigram_counts, bigram_counts):
    list_of_prob = {}
    for bigram in list_of_bigrams:
        word1 = bigram[0]
        list_of_prob[bigram] = (bigram_counts.get(bigram)) / (unigram_counts.get(word1))
    return list_of_prob

if __name__ == '__main__':
    words = convertTextToWords()


    bigrams, number_of_unigrams, number_of_bigrams = bigramFunction(words)
    print('Bigrams:', bigrams)
    print('Bigrams and counts:', number_of_bigrams)
    print('Unigrams and counts:', number_of_unigrams)

    bigram_probability = calculate_bigram_probability(bigrams, number_of_unigrams, number_of_bigrams)
    print('Bigrams and probability', bigram_probability)