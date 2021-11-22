from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

class hopefully_sudoku:
  def __init__(self):
    self.solved_board_num = ""
    self.missing_board_num = ""

  def webscraper(self):
    page_url = "https://grid.websudoku.com/?level=1&amp;set_id=1" # scrapes data from grid.websudoku.com

    uClient = uReq(page_url) # downloads the html page from page_url

    page_soup = soup(uClient.read(), "html.parser") # parses html into a soup data structure (readable)

    board_container = page_soup.find("form", {"name": "board"}) # narrows html down to the 'board'

    self.solved_board_num = board_container.find(attrs = {"name": "cheat"})["value"] # grabs solved numbers
    self.missing_board_num = board_container.find(attrs = {"id": "editmask"})["value"] # grabs 'missing' numbers

  def format(self):
    array_of_rows = [] # 2d list / array of rows
    for index in range(0, len(self.solved_board_num) - 1, 9):
      row = self.solved_board_num[index:index + 9] # initializes row every 9 chars
      row = row[:3] + " " + row[3:6] + " " + row[6:] # space between each 3x3 square

      row_arr = []
      row_arr.insert(0, row) # reverses the row
      array_of_rows.append(row_arr)

    sudoku_puzzle = ""
    index_row = 0
    for row in array_of_rows: # iterates through each row
      for char in row:
        row = char + " " # adds spaces between numbers
        
      if index_row == 3 or index_row == 6:
        sudoku_puzzle = sudoku_puzzle + "\n" # inserts a new line every 3rd and 6th row

      sudoku_puzzle = sudoku_puzzle + ' '.join(row) + "\n" # inserts a new line for the next row
      index_row += 1
    print(sudoku_puzzle)

  def play(self):
    print("play")

  def run(): # welcome prompt / "user interface" on the terminal
    print("Welcome to Sudoku!")
    test = hopefully_sudoku()

    playing = True
    while (playing):
      test.webscraper()
      test.format()

      print("load another solved sudoku? y/n")
      if (str(input()) == 'n'):
        exit()
      else:
        break

loop = True # loops until player doesn't wanna play anymore
while (loop):
  hopefully_sudoku.run()