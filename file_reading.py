__author__ = "Uni-Nummer: Katharina Mepq, 6621331: Lucas Laub"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "No thanks"
__email__ = "merts.ekaterina@gmail.com, l.g.laub@gmx.de"


def file_selection():
    """This function gets a path to a file from the user and returns it to the main body"""
    while True:
        way = input('please enter the full path to your file: ')
        try:
            # making sure the File exists
            f = open(way, 'r')
            return way
        # handel FileNotFoundError inform the user
        except FileNotFoundError:
            print('Die Datei konnte nicht gefunden werden.Überprüfen Sie bitte ihre Eingabe.')

