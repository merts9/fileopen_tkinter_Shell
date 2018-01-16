__author__ = "Uni-Nummer: 6593731: Ekaterina Merts, 6621331: Lucas Laub"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "No thanks"
__email__ = "merts.ekaterina@gmail.com, l.g.laub@gmx.de"

import file_reading


class Calc():
    def __init__(self):
        self.__number_words = 0
        self.__number_chars = 0
        self.__number_chars_no_space = 0
        self.__dic_words = {}
        self.__dic_chars = {}
        self.__f = open(file_reading.file_selection)



    def get_words(self, file):
        for line in file:
            if line == '':
                f.close()
                break
            number_words += len(line)
            number_chars += len(line) - line.count(' ')
            line_space = line.split(' ')
            for elem in line_space:
                if len(elem) == 1:
                    line_space.remove(elem)
        text = f.read().lower()
        selection = re.findall(r'\b[a-z]{2,15}\b', text)
        
        for word in selection:
            count_words = dic_words.get(word, 0)
            dic_words[words] = count_words + 1
        frequency_list = dic_words.keys()
        
        for words in frequency_list:
            print(words, dic_word[words])
        
        for litera in line:
            count_litera = dic_chars.get(litera, 0)
            count_litera += 1
            dic_char[litera] = count_litera
            print(dic_char)
    main()            
            


