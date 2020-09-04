import re 

if __name__ == '__main__':
    text = "This is the spyder3. I am programming with python. I am going to market"
    com = re.findall('ing', text)
    print(com)
    
    text = 'cat bat mat sat'
    com = re.compile('at')    
    p = com.sub('N',text)
    print(p)