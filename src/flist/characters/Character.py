



class Character:
    
    def __init__(self, name:str):
        self.name = name
        self.age = None
        self.gender = None 
        self.orientation = None
        self.species = None 
        self.preference = None 
        self.dom_sub = None
        self.created = None
        self.last_updated = None
        self.views = None
        self.bookmars = None 
        
    def set_attribute(self, attr, value):
        if attr == 'Age':
            self.age = value
        
        elif attr == 'Gender':
            self.gender = value
            
        elif attr == 'Orientation':
            self.orientation = value
            
        elif attr == 'Species':
            self.species = value
        
        elif attr == 'Dom/Sub':
            self.dom_sub = value
            
        elif attr == 'created':
            self.created = value
            
        elif attr == 'Furry Preference':
            self.preference = value
            
        elif attr == 'Last updated':
            self.last_updated = value 
        
        elif attr == 'Views':
            self.views = value
            
        elif attr == 'Bookmars':
            self.bookmarks = value
            
        elif attr == 'Timezone':
            self.timezone = value
            
            
    def __repr__(self):
        return f"{self.name} ({self.gender})"
            
            
            
            
            
            
            