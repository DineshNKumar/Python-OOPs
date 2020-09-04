# regex

import re

# Qualifiers
# *       : zero or more
# +       : one or more
# ?       : zero or one 
# {3}     : exact number
# {2,5}   : range of numbers(minimum, maximum)
# |       : Either or 
# ()      : group


if __name__=='__main__':
    text_for_search = '''
    abcdefghijklmnopqrstuvwxyz
    www.google.com
    23,4232342
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    Ha Haha
    6773-7746-7432
    6667.7639.7687
    2342*3453*3534
    1000.7639.7687
    6000*3453*3534
    '''
    sentence = '''
    bat
    cat
    rat
    mat
    Mr. Rahul
    Mr Deepak Singh
    Mrs Soniya
    Mrs. Deepika Kumar
    Mr. Dinesh
    Mr Rajesh
    Mr. T
    '''
    # patterns = re.compile(r'[^b]at')
    # matches = patterns.finditer(sentence)
    # for lines in matches:
    #     print(lines.group(),end=' ')
    # patterns = re.compile(r'\d{4}.\d{4}.\d{4}')
    # matches = patterns.finditer(text_for_search)
    # for lines in matches:
    #     print(lines.group())
    
    # patterns = re.compile(r'Mr\.?\s[A-Z][a-z]{3}')
    # matches = patterns.finditer(sentence)
    # for lines in matches:
    #     print(lines.group())
    
    # patterns = re.compile(r'M(r|s|rs)\s[A-Z]*')
    # matches = patterns.finditer(sentence)
    # for lines in matches:
    #     print(lines.group())
    
    # patterns = re.compile(r'Mr\.?\s[A-Z]\w*')
    # matches = patterns.finditer(sentence)
    # for lines in matches:
    #     print(lines.group())
    
# =============================================================================
#     WORKING WITH EMAIL ADDRESS
# =============================================================================
    
    emails = '''
    saniya@yahoo.com
    dinesh21324@gmail.com
    dinesh-kumar@gmail.com

    sohan.kumar@university.edu
    seenu-324-kumar@my-work.net
    '''
    
    # patterns = re.compile('[a-zA-Z.]+@[a-z]+\.(com|edu)')
    # matches = patterns.finditer(emails)
    # for match in matches:
    #     print(match.group())
    
    # patterns = re.compile('[a-zA-Z0-9.-]+@[a-z]+\.(com|edu)')
    # matches = patterns.finditer(emails)
    # for match in matches:
    #     print(match.group())
    
    
    # patterns = re.compile('[a-zA-Z0-9.-]+@[a-z-]+\.(com|edu|net)')
    # matches = patterns.finditer(emails)
    # for match in matches:
    #     print(match.group())
        
# =============================================================================
# Working with urls or IP address
# =============================================================================
        
    urls = '''
        https://www.google.com
        http://coreapp.com
        https://youtube.com
        http://www.up.government.edu
    '''
    
    # patterns = re.compile(r'https?://(www\.)?(\w+)*(\.\w+)')
    # matches = patterns.finditer(urls)
    # for match in matches:
    #     print(match.group(0))
    
    # patterns = re.compile(r'https?://(www\.)?(\w+)*(\.\w+)')
    # matches = patterns.finditer(urls)
    # for match in matches:
    #     print(match.group(1))
    
    # patterns = re.compile(r'https?://(www\.)?(\w+)*(\.\w+)')
    # subbed_urls = patterns.sub(r'\2\3', urls)
    # for match in subbed_urls:
    #     print(match,end='')
        
    # patterns = re.compile(r'Mr\.?\s[A-Za-z]+')
    # finded = patterns.findall(sentence) # findall returns all matches as list
    # for f in finded:
    #     print(f)
    
    # patterns = re.compile(r'\d{4}.\d{4}.\d{4}')
    # finded = patterns.findall(text_for_search) # findall returns all matches as list
    # for f in finded:
    #     print(f)
    
    # sentence = "This is the start of the sentence"
    # patterns = re.compile(r'sentence')
    # mat = patterns.match(sentence)
    # print(mat)
    
    sentence = "This is the start of the sentence"
    patterns = re.compile(r'sentence')
    mat = patterns.search(sentence)
    print(mat.group())
    
# =============================================================================
#     Flags (Use for search a string with ignorecase)
# =============================================================================
    
    patterns = re.compile(r'START',re.IGNORECASE)
    matches = patterns.search(sentence)
    print(matches.group())
    
    
    
    

  