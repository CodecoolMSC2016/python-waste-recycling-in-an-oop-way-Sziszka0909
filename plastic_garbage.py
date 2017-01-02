
from garbage import Garbage


class PlasticGarbage(Garbage):
    def __init__(self, garbage_name, is_clean):
        super().__init__(garbage_name)
        self.is_clean = is_clean

    def clean(self):
        self.is_clean = True
