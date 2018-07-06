import re

class IdMatcher(object):
    '''a class to help manage regex matches'''
    def __init__(self,name,regex,overmatch_fxn = None):
        self.name = name
        self.regex = regex
        if overmatch_fxn is not None:
            self.overmatch = lambda: overmatch_fxn(self)
        else:
            self.overmatch = lambda: None
        self.groups_list = []
        self.label_list = []
        self.found_label = None
        self.tested_list = []
        pass
    
    def match(self,string):
        self.tested_list.append(string)
        m = re.match(self.regex,string,flags=re.IGNORECASE)
        if m is not None:
            self.groups_list.append(m.groups())
            self.label_list.append(string)
            return True
        else:
            return False

    def get_unique(self):
        ''' should be called after match'''
        if len(self.groups_list)>1:
            self.overmatch()
        elif len(self.groups_list) == 1:
            self.found_label = self.label_list[0]
        elif len(self.groups_list) == 0:
            raise Exception('"{}" not found in {} with regex("{}")'.format(self.name,self.tested_list,self.regex))

        return self.found_label
        
    def clean(self):
        self.groups_list = []
        self.label_list = []
        self.tested_list = []
        self.found_label = None

