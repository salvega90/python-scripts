import sys
from modules.randomizer import Randomizer
from modules.file_module import FileModule
from modules.google_sheets import GoogleShit

class SuperBowlSquares:
    def __init__(self):
        self.butt = ""
        self.files = FileModule()
        self.rand = Randomizer()
        self.google = GoogleShit()

    def _create_squares(self):
        """
        Creates the 10 X 10 rows for the SuperBowl Squares with randomized names and numbers
        :return: A list of lists
        """
        first_row = self.rand.rand_rows()
        first_row.insert(0,'')
        second_row = self.rand.rand_rows()
        final_list = [first_row]
        for row in second_row:
            scrambled = Randomizer.rand_humans(self.files.load_names())
            current = [row]
            stuff = list(current + scrambled)
            print(stuff)
            final_list.append(stuff)
            scrambled.pop(0)
        return final_list

    def write_to_google(self):
        if sys.argv[1] == 'Clean':
            self.google.clear_cells()
        elif sys.argv[1] == 'Calculate':
            values = self._create_squares()
            self.google.write_to_sheet(values=values)



if __name__ == '__main__':
    run = SuperBowlSquares()
    run.write_to_google()

