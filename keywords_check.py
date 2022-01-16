import re


def pattern_matching(sentence, keyword_patterns, keywords):
    # Detected words
    detected_keywords = []
    # Start matching
    for i in range(len(keyword_patterns)):
        result = re.search(keyword_patterns[i], sentence, re.IGNORECASE)
        if result :
            detected_keywords.append(keywords[i])
    return detected_keywords   
    
def keywords_to_patterns(keywords):
    patterns = []
    for i in range(len(keywords)):
        keyword_pattern = ''
        for j in range(len(keywords[i])):
            if j != len(keywords[i])-1 :
                keyword_pattern = keyword_pattern + keywords[i][j] + '.{0,3}'
            else:
                keyword_pattern = keyword_pattern + keywords[i][j]
        patterns.append(keyword_pattern)
    return patterns
    
def main():
	

    test1 = 'Fauucaak and my homie bro, reApEa and some fruits'
    test2 = 'jqhdiqudhqduhhc wqiuhdqwiudhqwiu dhiwq hiwqudhiu wh uqhdiq hd'
    test3 = 'gaNg bAng is bonkers, thisshit is tight'
    
    keywords = ['fuck','shit','rape','gangbang']
    keyword_patterns = keywords_to_patterns(keywords)
    
    #print('keywords ',keywords,' patterns ',keyword_patterns)
    print('test 1 text: ',test1,' detected words: ',pattern_matching(test1,keyword_patterns,keywords))
    print('test 2 text: ',test2,' detected words: ',pattern_matching(test2,keyword_patterns,keywords))
    print('test 3 text: ',test3,' detected words: ',pattern_matching(test3,keyword_patterns,keywords))
    
if __name__ == "__main__":
    main()