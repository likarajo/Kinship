from lib.processor import preprocess, terms_to_ignore
from collections import Counter
import json
import os

def mine(word, kins, streamed_data_file, mined_data_file, ):

    with open(streamed_data_file, 'r') as infile:    
        count_all = Counter()
        #print('Mining data from dump....')
        for line in infile:
            if not line.isspace():
                tweet = json.loads(line) 
                terms = preprocess(tweet['text'])            
                terms_filtered = [term for term in terms if \
                         all( 31<ord(i) and ord(i)<127 for i in term) \
                         and all(ord(i)<48 or ord(i)>57 for i in term) \
                         and term not in terms_to_ignore \
                         and not term.startswith( ('#','@') ) \
                         and len(term) != 1
                         and term.lower() not in (word.lower())                     
                         ]
                count_all.update(terms_filtered)            
    data = count_all.most_common(kins)
    #print('Data mining complete!')
    with open(mined_data_file, 'w') as outfile:
        json.dump(data, outfile)
    os.remove(streamed_data_file)
