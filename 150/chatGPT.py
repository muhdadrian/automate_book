import pyperclip

text = [
    'Lists of animals',
    'Lists of aquarium life', 
    'Lists of biologists by author abbreviation',
    'Lists of cultivars',
]

# Add stars to each line
lines = ['* ' + line for line in text]

# Join lines into a single string
text_with_stars = '\n'.join(lines)

# Copy to clipboard
pyperclip.copy(text_with_stars)
