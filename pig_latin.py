# ============= A Pig Latin is a Program that translate ==========
# ============= the given sentence into some other language =======



original=input('Enter the sentence= ').strip().lower()

#converted to list of words
words=original.split() 

new_words=[]

#looping the words and convert to pig latin

for word in words:
    if word[0] in 'aeiou':
        new_word=word+'yay'
        new_words.append(new_word)
    else:
        vowel_pos=0
        for letter in word:
            if letter not in 'aeiou':
                vowel_pos=vowel_pos+1
            else:
                break
        cons=word[:vowel_pos]
        the_rest=word[vowel_pos:]
        new_word=the_rest+cons+'ay'
        new_words.append(new_word)

#final result 
encoded=" ".join(new_words)
#print the result 
print('Here is Your encoded sentence= ',encoded)
