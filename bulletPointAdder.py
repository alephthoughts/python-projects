#! python3
# Adds Wikipedia bullet points to the start of each line of text on the
# clipboard

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i, line in enumerate(lines):
    if line:
        lines[i] = '* ' + line
text = '\n'.join(lines)

pyperclip.copy(text)
