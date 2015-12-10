# a simple path builder
class PathBuilder:
    LINUX_SEP = "/"
    WINDOWS_SEP = "\\"
    
    _elements = []
    _base = ""
    _sep = ""
    _current = []
    
    def __init__(self, root):        
        self._base = str(root).strip()
        if self._base.find(self.LINUX_SEP) != -1:
            self._sep = self.LINUX_SEP
        else:
            self._sep = self.WINDOWS_SEP
        
        self._elements = self._base.split(self._sep)
        self._current = self._elements

    # append sub path
    def append(self, sub):
        self._elements.append(str(sub).strip())
        self._current = self._elements

    # get parent path
    def parent(self):
        self._current.pop()
        return self._sep.join(self._current)

    # get full path
    def fullpath(self):
        return self._sep.join(self._elements)
