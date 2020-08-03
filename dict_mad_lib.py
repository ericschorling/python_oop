import random


sweet_matlib_dict = {
    "noun" : "",
    "verb" : "",
    "adjective": '',
    'number' : 0,
    'play_again' : 'Y'
}



while sweet_matlib_dict['play_again'] == "Y": 

    sweet_matlib_dict['noun'] = input('Give me a cool, funny noun: ')
    sweet_matlib_dict['verb'] = input('Give me an even funnier verb (present tense): ')
    sweet_matlib_dict['adjective'] = input('Lastly, give me a really great adjective: ')
    sweet_matlib_dict['number'] = int(input("Give me an integer: "))

    print("Yesterday, %s was having a very bad nightmare about having to %s, they were awake for %d hours with a %s stomach ache worring about git hub..." % (sweet_matlib_dict['noun'], sweet_matlib_dict['verb'], sweet_matlib_dict['number'], sweet_matlib_dict['adjective']))

    sweet_matlib_dict['play_again'] = input("would you like to play again? (Y/N) ")



