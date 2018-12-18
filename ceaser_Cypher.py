def cypher(key, text):
    
    cyphered_Text = ''
    
    key = int(key)
    
    for char in text:
        
        if char == ' ':
            
            cyphered_Text += char
        
        else:
            ascii_char = ord(char)
            
            ascii_char += key
            
            cyphered_Text += chr(ascii_char)
        
    return cyphered_Text

def decypher(key, cyphered_Text):
    
    plain_Text = ''
    
    key = int(key)
    
    for char in cyphered_Text:
        
        if char == ' ':
            
            cyphered_Text += char
        
        else:
            ascii_char = ord(char)
            
            ascii_char -= key
            
            plain_Text += chr(ascii_char)
            
    
    return plain_Text
        
    

print('Enter Plain Text: ')

text = input()


print('Enter Key: ')
    
key = input()



while not key.isdigit():
    
    print('Please enter the text again : ')
    
    key = input()
    
cypher_Text = cypher(key, text)
print ('Cypher Text : ' + cypher_Text)
print ('Plain Text : ' + decypher(key, cypher_Text))   
    
    
