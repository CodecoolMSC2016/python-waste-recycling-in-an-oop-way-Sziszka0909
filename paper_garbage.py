from garbage import Garbage


class PaperGarbage(Garbage):
    def __init__(self, garbage_name, is_squeezed):
        super().__init__(garbage_name)
        self.is_squeezed = is_squeezed

    def squeeze(self):
        self.is_squeezed = True
