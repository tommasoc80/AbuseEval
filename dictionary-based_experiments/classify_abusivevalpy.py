import csv, re
from nltk.tokenize import TweetTokenizer
import collections
from nltk.stem import PorterStemmer

def output_print(prediction_dict, outfile_):

    output = open(outfile_, "a")

    for k, v in prediction_dict.items():
        output.writelines(str(k[0]) + "\t" + str(k[1]) + "\t" + str(k[2]) + "\t" + v + "\n")
    output.close()


def check_messages(message_dict, offensive_term):
    """
    :param message_dict: message id and list of tokens of the message
    :param offensive_term: offensive term list
    :return:
    """

    """
    2 or more off words in == OFF
    """

    data_tokens = collections.defaultdict(list)

    for id, tokenized_message in message_dict.items():
        for elem in tokenized_message:
            if elem in offensive_term:
                data_tokens[id].append(elem)

    """
    classification
    """

    classified_elems = {}
    for msid, token_list in data_tokens.items():
        if len(token_list) >= 1:
            #print(msid, token_list)
            classified_elems[msid] = "ABU\tEXP"

    for entry in message_dict.keys():
        if entry not in classified_elems:
            classified_elems[entry] = "NOTABU\tO"

    return classified_elems


def clean_tokens(tweet_message):
    tweets_clean = []

    tweet_tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)

    # only removing the hash # sign from the word
    tweet_message = re.sub(r'#', '', tweet_message)
    # tokenize
    tokens =  tweet_tokenizer.tokenize(tweet_message)
    # get stem of tokens
    for elem in tokens:
        stem_token = PorterStemmer().stem(elem)  # stemming word
        #print(elem, stem_token)
        tweets_clean.append(stem_token)

    return tweets_clean


def read_and_match(comments, terms2):

    tokens_ = {}


    with open(comments, newline='') as csvfile:
        read_data = csv.reader(csvfile, delimiter='\t',) # OLID;
#        next(read_data)
        counter = 0

        for row in read_data:
            message_id = row[0]
            message = row[1]
            label = row[-1]

            """
            tokenize data with TweetTokeinizer NLTK and clean it
            """
            tokens = clean_tokens(message)
            tokens_[(message_id,message,label)] = tokens

    wiegand_extended = []

    with open(terms2) as f:
        for line in f:
            line_splitted = line.strip().split("\t")
            token_off = line_splitted[0].split("_")[0]
            score_off = float(line_splitted[1])
            if score_off >= 0.75:
                stem_offensive = PorterStemmer().stem(token_off)
                wiegand_extended.append(stem_offensive)

    print()
    print("number of test messages: " + str(len(tokens_))) # number of messages


    set_4 = check_messages(tokens_, wiegand_extended)
    #print(set_4)

#    outdir = "./predictions-v4/test/"

    outfile4 =  "abuseval_test.txt"

    output_print(set_4, outfile4)


if __name__ == '__main__':

    """
    abusive_comments_test = .tsv file containing the following information: message id (OffenseEval test file);
    message (OffenseEval test file); abuseval labels (labels available in ./data/abuseval_labels/abuseval_offenseval_test.tsv)

    list_offensive_words4 = expanded lexicon of offensive/abusive terms available at https://github.com/uds-lsv/lexicon-of-abusive-words/tree/master/Lexicons

    """


    abusive_comments_test = "../abuseval_offenseval_test.tsv"
    list_offensive_words4 = "../../../implicit_explicit/offeseval_data/dictionary_approach/wiegand_expanded" # Wiegand et al., 2018 - offensive terms expanded

    read_and_match(abusive_comments_test,list_offensive_words4)