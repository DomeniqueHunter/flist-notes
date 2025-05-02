import re

characters = {}

def find_characters(html):
    m = re.search(r'<script>var characterdata = (.+);', html)
    characters_raw = eval(m.group(1))
    characters_swap = {v: k for k, v in characters_raw.items()}
    
    # for k, v in characters_swap.items():
    #     print(k, v)
    
    global  characters
    characters = characters_swap
    
    return characters_swap


def character_id(character:str):
    return characters[character]