import json
from difflib import get_close_matches

data = json.load(open('Dictionary/data.json', 'r'))

def translate (word):
    word = word.lower().strip()
    if word in data:
        return "\n".join(data[word])
    #Allows word to be capitalized to see if a capitol is in the dictionary, like Paris or Dehli
    elif word.title() in data:
        return "\n".join(data[word.title()])
    elif word.upper() in data:
        return "\n".join(data[word.upper()])
    #If word is misspelled but close to a correct spelling, this will create a list of the 3 closet words and iterate through them
    elif len(get_close_matches(word, data.keys(), cutoff = .8)) > 0:
        count = 0
        while count < 3:
            yn = input("Did you mean %s instead? Please enter Y for yes or N for no: " % get_close_matches(word, data.keys())[count])
            yn = yn.lower()
            if yn == "y":
                return "\n".join(data[get_close_matches(word, data.keys())[count]])
            elif yn == "n":
                count +=1
                continue
            else:
                print ("Please enter Y or N")
        return "We did not find a match for your word. Please double check it and try again. "
    else:
        return "The word doesn't exist. Please double check it. "

word = input("Enter word: ")
print (translate(word))

#Below is if you want the function to return lists. To use, remove both the .join methods in the translate function
'''
output = translate(word)
if type (output) == list:
    for item in output:
        print (item)
else:
    print (output)
'''