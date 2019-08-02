class Cell:
    def __init__(self, temp, category):
        self.__temp = temp
        self.__category = category

    def get_temp(self):
        return self.__temp

    def set_temp(self, temp):
        self.__temp = temp

    def get_category(self):
        return self.__category
