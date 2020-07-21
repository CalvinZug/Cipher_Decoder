import sys

shift_num = 0
word_amt = 0
word_amt_list = []
message = input("input a message to decode: ")
decoded_message = ""
new_message = ""
user_file = open(sys.argv[1])
dictionary = user_file.read()

def check_shift(word):
    for c in word:
        global decoded_message
        if c.islower():
            value = (ord(c) - 97 + shift_num) % 26
            new_char = chr(value + 97 ) 
            decoded_message += new_char
        elif c.isupper():
            decoded_message += c
    return(decoded_message)
    

while shift_num <= 25:
    each_word = message.split(" ")
    for word in each_word:
        check_shift(word)
        if decoded_message.lower() in dictionary:
            word_amt += 1
        decoded_message = ""
    shift_num +=1
    word_amt_list += [word_amt]
    word_amt = 0
    
shift_num = word_amt_list.index(max(word_amt_list))
for c in message:
    if c.islower():
        value = (ord(c) - 97 + shift_num) % 26
        new_char = chr(value + 97 )
        new_message += new_char
    else:
        new_message += c

print(new_message)


            
    

        

