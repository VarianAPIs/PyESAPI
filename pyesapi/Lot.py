class Lot:
    '''a custom collection container for pysapi'''

    def __init__(self, some_collectable):
        self.collection = some_collectable

    def FirstOrDefault(self, fxn):
        result = list(filter(fxn, self.collection))
        if len(result) == 0:
            return None
        else:
            return result[0]

    def Select(self, fxn):
        '''returns a new lot of objects where fxn(object) == True'''
        if callable(fxn):
            return Lot(list(filter(fxn, self.collection)))
        else:
            raise TypeError('fxn is not callable')

    def __getitem__(self, key):
        if type(key) is int or type(key) is slice:
            # this could be slow:
            return [i for i in self.collection][key]
        else:
            if callable(key):
                obj = self.FirstOrDefault(key)
            else:
                obj = self.FirstOrDefault(lambda x: x.Id == key)
            if obj == None:
                print(type(key))
                raise KeyError('not found')
            else:
                return obj
