f = open("dictionary.txt",'r')
vocabulary = f.read()
print(vocabulary)

vocabulary = open("dictionary.txt", "r").read()
tokenized_vocabulary = vocabulary.split(" ")
print(tokenized_vocabulary[0:4])

f = open("story.txt", 'r')
story_string = f.read()

print(story_string)
story_string = story_string.replace(".","")
story_string = story_string.replace(",","")
story_string = story_string.replace("'","")
story_string = story_string.replace(";","")
story_string = story_string.replace("\n","")


def clean_text(text_string):
    cleaned_string = text_string.replace(".","")
    cleaned_string = cleaned_string.replace(",","")
    cleaned_string = cleaned_string.replace("'", "")
    cleaned_string = cleaned_string.replace(";", "")
    cleaned_string = cleaned_string.replace("\n", "")
    return(cleaned_string)
cleaned_story = clean_text(story_string)

def clean_text(text_string):
    text_string = text_string.lower()
    cleaned_string = text_string.replace(",","")
    cleaned_string = cleaned_string.replace(".","")
    cleaned_string = cleaned_string.replace("'", "")
    cleaned_string = cleaned_string.replace(";", "")
    cleaned_string = cleaned_string.replace("\n", "")
    return(cleaned_string)
cleaned_story = clean_text(story_string)


f = open("story.txt", 'r')
story_string = f.read()
clean_chars = [",", ".", "'", ";", "\n"]

# Previous code for clean_text().
def clean_text(text_string,special_characters):
    cleaned_string = text_string
    for i in special_characters:
        cleaned_string = cleaned_string.replace(i,"")
    
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

cleaned_story = clean_text(story_string,clean_chars)
print(cleaned_story)

def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string,special_characters):
    cleaned_story = clean_text(text_string,special_characters)
    story_tokens = cleaned_story.split(" ")
    return(story_tokens)

clean_chars = [",", ".", "'", ";", "\n"]
cleaned_story = clean_text(story_string, clean_chars)
tokenized_story = tokenize(story_string, clean_chars)
print(tokenized_story[0:9])


def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string, special_characters):
    cleaned_story = clean_text(text_string, special_characters)
    story_tokens = cleaned_story.split(" ")
    return(story_tokens)


clean_chars = [",", ".", "'", ";", "\n"]
tokenized_story = tokenize(story_string, clean_chars)
tokenized_vocabulary = tokenize(vocabulary, clean_chars)
misspelled_words = []
for item in tokenized_story:
    if item not in tokenized_vocabulary:
        misspelled_words.append(item)
        
        
print(misspelled_words)

# Default code
def tokenize(text_string, special_characters, clean=False):
    if clean == True:
        cleaned_story = clean_text(text_string, special_characters)
        story_tokens = cleaned_story.split(" ")
        return(story_tokens)
    story_tokens = text_string.split(" ")
    return(story_tokens)
tokenized_story = tokenize(story_string,clean_chars,clean = True)
tokenized_vocabulary = tokenize(vocabulary,clean_chars)
misspelled_words = []
for i in tokenized_story:
    if i in tokenized_vocabulary:
        misspelled_words.append(i)

def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string, special_characters, clean = False):
    cleaned_text = text_string
    if clean:
        cleaned_text = clean_text(text_string, special_characters)
    tokens = cleaned_text.split(" ")
    return(tokens)

final_misspelled_words = []
def spell_check(vocabulary_file,text_file,special_characters = [",",".","'",";","\n"]):
    misspelled_words = []
    v = open(vocabulary_file).read()
    t = open(text_file).read()
    tokenized_vocabulary = tokenize(v,clean=True,special_characters = [",",".","'",";","\n"])
    tokenized_text = tokenize(t,clean = True,special_characters = [",",".","'",";","\n"])
    for i in tokenized_text:
        if i not in tokenized_vocabulary and i != '':
            misspelled_words.append(i)
    return(misspelled_words)
            
final_misspelled_words = spell_check("dictionary.txt","story.txt")
print(final_misspelled_words)

