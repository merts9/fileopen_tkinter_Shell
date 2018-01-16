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



