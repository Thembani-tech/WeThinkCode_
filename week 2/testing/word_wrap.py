# Word Wrap with  paragraphs

def word_wrap(text, width):
    paragraphs = text.split("\n")
    wrapped_paragraphs = []
    
    for paragraph in paragraphs:
        words = paragraph.split()
        lines = []
        current_line = ""
        
        for word in words:
            if len(current_line) + len(word) + 1 <= width:
                if current_line:
                    current_line += " "
                current_line += word
            else:
                lines.append(current_line)
                current_line = word
                
        if current_line:
            lines.append(current_line)
            
        wrapped_paragraphs.append("\n".join(lines))
        
    return "\n\n".join(wrapped_paragraphs)


# Example usage:
text = """Starting a newjourney as a programmer is nice and fun challenge.
 
this is a second paragraph that is also quite long and needs to be wrapped properly."""
print(word_wrap(text, 20))