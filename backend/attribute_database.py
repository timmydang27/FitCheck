class AttributeDatabase:

    def __init__(self):
        self.database = {}

    def add_attribute(self, attribute, label):
        '''
        Adds an attribute : label pair to the database

        Ex. add('black', 'color') adds 'black' --> 'color' to database
        '''
        self.database[attribute] = label

    def label_for_attribute(self, attribute):
        '''
        Returns the label associated with a given attribute if available. 
        '''
        if attribute in self.database:
            return self.database[attribute]
        else:
            raise KeyError('attribute not found in database')