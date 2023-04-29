



class Character:
    
    def __init__(self, name:str):
        self.name = name
        
    def set_attribute(self, attr, value):
        try:
            # print(f'adding: {attr} -> {value}')
            self.__dict__[attr] = value
        
        except Exception as e:
            print(e)
            exit()
            
    def get_attribute(self, attr):
        return self._get(attr)
    
    def _get(self, attr):
        if attr.lower().replace(' ', '_') in self.__dict__:
            return self.__dict__[attr.lower().replace(' ', '_')]
        
        else:
            return None
            
            
    def __repr__(self):
        return f"{self.name} ({self.gender})"
            
            
            
            
            
            
            