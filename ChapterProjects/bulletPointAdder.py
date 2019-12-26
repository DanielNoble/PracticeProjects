#  Adds Wikipedia bullet points to the start of each line copied to the clipboard

import pyperclip
text = pyperclip.paste()

#  TODO: Separate lines and add stars

pyperclip.copy(text)

#  Separate the lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)