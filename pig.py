vowels = "aeiouy"

def pig(word):
    """
    Function to return the pig latin translation of a single word 
	
    Arguments:
	
    :param word: the word to be translated
    :return: the translated word
    """

    #for words beginning with vowel (not including y), add "way" to end of word
    if word[0] in "aeiou":
        return word + "way"

    #for words beginning with consonants or y, iterate over letters
    #in word until a vowel is found and then apply pig latin rules to word
    else:
        n=1
        while word[n] not in vowels:
            n = n + 1
        return word[n:len(word)] + word[0:n] + "ay"
    

def test_pig():
    """
    Function to test my pig() function with the examples given
    """

    assert pig("happy") == "appyhay","Happy does not translate"
    assert pig("duck") == "uckday","Duck does not translate"
    assert pig("glove") == "oveglay","Glove does not translate"
    assert pig("evil") == "evilway","Evil does not translate"
    assert pig("eight") == "eightway","Eight does not translate"
    assert pig("yowler") == "owleryay","Yowler does not translate"
    assert pig("crystal") == "ystalcray","Crystal does not translate"

def run_translator():
    """
    Function to translate a sentence to pig latin and print it
    :input: the sentence to be translated
    :output: the printed translated sentence
    """

    #asking for user input, and inserting a new line after
    #the input prompt because it looks nice
    sentence = input((("""What would you like to translate?
    """)))
    words = sentence.split()
    
    #repeatedly asks for input until a blank line is inputted
    while sentence != "":
        
        #converting the inputted string to a list
        words = sentence.split()
        translation = []

        for word in words:
            translation.append(str(pig(word)))

        #converting the list back to a string
        output = " ".join(translation)
        print("Translation: " + output)
        print(" ")
        
        #repeating the loop until input is blank
        sentence = input((("""What would you like to translate?
""")))
        if sentence == "":
            break

test_pig()

#arranging my code so that thee functions can be imported to other modules,
#but the translator runs automatically when pig.py is called directly
if __name__ == '__main__':
    run_translator()
