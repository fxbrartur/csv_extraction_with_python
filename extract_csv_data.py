# code to read a column in a CSV (Comma-separated values) file, printing the text with no quotation marks, just separated by commas.

def extract_column_csv(name_archive: str, column_index: int, data_type: str):

  column = []
  with open(file=name_archive, mode='r', encoding='utf8') as fp:
    line = fp.readline()
    line = fp.readline()
    while line:
      divided_line = line.split(sep=',') # commas are the elements which have the role to separate data in CSV (Comma-separated values) files
      column_index = divided_line
      if data_type == 'str': # for string data extraction
        column_index = divided_line[1] # select the line you want to extract if str data
        columns = str(column_index)
        column.append(columns)
        line = fp.readline()
      elif data_type == 'int': # for integer data extraction
        column_index = divided_line[1] # select the line you want to extract if int data
        columns = int(column_index)
        column.append(columns)
        line = fp.readline()

  return column

# extract the column you informed before, it'll print up to 600 columns side by side separated by commas. For my use case was very useful, if you need to print more, is very simple to make it.

consult = extract_column_csv(name_archive='test.csv', column_index=1, data_type='int') # where I typed the word 'test' please inform the name and direction of your CSV file. I chose the column = 1 and my data was int, you can choose what you need.
print(consult)
