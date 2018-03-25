import sys
def Load_Settings():
    global url_dict
    url_dict = 'none'
    settings_1 = open('settings.txt', 'r')
    my_string = settings_1.readlines()
    if my_string[0].strip() == '1':
        url_dict = my_string[1].strip()
    else:
        url_dict = 'none'

    if my_string[2].strip() == '1':
        url_powerrankings = my_string[3].strip()
    else:
        url_powerrankings = 'none'

def Create_dict():
    dict1 = open(url_dict, 'r')
    my_string = dict1.readlines()
#    for i in range(0, len(my_string)):
    for i in range(0, 100):
        if my_string[i].startswith('   -'):
            print(my_string[i])


def Parse_slovar():
    espn_1 = open('espn.html', 'r')
    my_string = espn_1.read()

if __name__ == '__main__':
    Load_Settings()
    Create_dict()
    print('test')