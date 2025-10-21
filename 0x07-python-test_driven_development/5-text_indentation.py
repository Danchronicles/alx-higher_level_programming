#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new line
    s after each of these characters '.', '?', ':'
    
    Args:
        text(string):  The input string, 
    
    Raises:
        TypeError: If text is not a string
    
    """
    
    # 1. Validate 'text' type
    if not isinstance(text, str):
        raise TypeError("Text must be a string")
    
    # 2. Define delimeters and replacement
    delimeters = ['-', '?', ':']
    
    # 3. Process the Text: Replace delimeters with the delimeter followed by a unique placeholder
    processed_text = text
    for delim in delimeters:
        processed_text = processed_text.replace(delim, delim + '|||')
        # We replace the delimeter followed by any potential spaces(s) with the delimiter and a placeholder. This handles cases like "Hello. world" -> 'Hello. ||| World'
        
    # 4. Split the text using the Placeholder
    sentences = processed_text.split('|||')
    
    # 5. Print the reformatted text
    for i, sentence in enumerate(sentences):
        cleaned_sentences = sentence.strip()
        # Remove leading/trailing spaces as reguired (i.e " no spaces at the beginning or at the end of each printed line")
        if  cleaned_sentences:
            if i == len(sentences) -1:
                # last segment (no extra newlines needed)
                print(cleaned_sentences, end="")
            else:
                #print segmented followed by two new lines
                print(cleaned_sentences, end="\n\n")
    # Ensure a final newline if the text ended in a delimeter
    if processed_text.endswith('|||'):
        print()

