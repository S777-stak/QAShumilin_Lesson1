
import re

text = """\
Adam Jones Jr. thinks he didn't. In any case, this isn't true... 
"""
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)

for stuff in sentences:
        print(stuff)    
