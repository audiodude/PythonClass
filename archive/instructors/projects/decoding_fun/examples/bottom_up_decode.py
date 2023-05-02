# -*- coding: utf-8 -*-

#correct two letter words from scrambled text into unscrambled words 
#and cache the correct conversions

#found on http://www.textfixer.com/resources/common-english-words.txt
a = "a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,would,yet,you,your"
ls = a.split(",")
#>>> a = ['a', 'able', 'about', 'across', 'after', 'all', 'almost', 'also', 'am', 'among', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'but', 'by', 'can', 'cannot', 'could', 'dear', 'did', 'do', 'does', 'either', 'else', 'ever', 'every', 'for', 'from', 'get', 'got', 'had', 'has', 'have', 'he', 'her', 'hers', 'him', 'his', 'how', 'however', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just', 'least', 'let', 'like', 'likely', 'may', 'me', 'might', 'most', 'must', 'my', 'neither', 'no', 'nor', 'not', 'of', 'off', 'often', 'on', 'only', 'or', 'other', 'our', 'own', 'rather', 'said', 'say', 'says', 'she', 'should', 'since', 'so', 'some', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'this', 'tis', 'to', 'too', 'twas', 'us', 'wants', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'would', 'yet', 'you', 'your']
two_ltrs = [word for word in ls if len(word) == 2]
two_ltrs = ['am', 'an', 'as', 'at', 'be', 'by', 'do', 'he', 'if', 'in', 'is', 'it', 'me', 'my', 'no', 'of', 'on', 'or', 'so', 'to', 'us', 'we']


def get_twoltr_words(scrambled_text):
    with open(scrambled_text) as t:
        text_two_ltrs = [word for word in t.read() if len(word) == 2]
    return text_two_ltrs

#print "two ltr words"
#print get_twoltr_words("mmenc.txt")




#from collections import Counter 
def get_longest_word(scrambled_text):
    with open(scrambled_text) as t:
        # > 10 is an arbitrary number for now
        text_list = [word for word in t.read().split() if len(word) > 10]
        ln = 1
        longest_word = ""
        for word in text_list:
            if len(word) > ln:
                ln = len(word)
                longest_word = word

    return longest_word


print "longest word"
print get_longest_word("mmenc.txt")



import pickle

def get_eng_word_dict():
    filename = 'ngsl.pickle'
    mode = 'r'

    with open(filename, mode) as f:
        ngsl_words = pickle.load(f)
        return ngsl_words

def match_english_words_by_length(eng_dict, word_length):
    eng_dict_word_len_matches = [word for word in eng_dict if len(word) == word_length]
    return eng_dict_word_len_matches

word_len = len(get_longest_word("mmenc.txt"))
eng_dict = get_eng_word_dict()

print match_english_words_by_length(eng_dict, word_len)

        #text_longest_word
    #return text_two_ltrs

#clean all non-matching english words eg: words with dashes, numbers, non-alpha or nonsense words
#take care of unicode issues



