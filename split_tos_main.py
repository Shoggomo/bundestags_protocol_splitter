
# needs pdftk installed and in PATH

import os
import re
import sys

# These differ for some WPs
FIRST_BOOKMARK_SPLIT = 2
SECOND_BOOKMARK_SPLIT = -1

'''
Exceptions: 
  For some files the first split does not work via bookmarks.
  Their first splits were checked manually. These values will be used to split.
'''
SPLIT_EXCEPTIONS = {
  "18002": 3,
  "18008": 5,
  "18012": 3,
  "18014": 9,
  "18020": 5,
  "18023": 9,
  "18026": 9,
  "18033": 9,
  "18036": 9,
  "18043": 5,
  "18046": 13,
  "18054": 9,
  "18057": 9,
  "18063": 13,
  "18064": 5,
  "18066": 9,
  "18070": 5,
  "18073": 9,
  "18076": 9,
  "18079": 9,
  "18082": 9,
  "18085": 5,
  "18088": 9,
  "18091": 9,
  "18097": 9,
  "18098": 5,
  "18100": 9,
  "18103": 9,
  "18106": 9,
  "18109": 9,
  "18112": 9,
  "18115": 13,
  "18117": 5,
  "18119": 3,
  "18124": 11,
  "18130": 11,
  "18136": 9,
  "18138": 3,
  "18140": 5,
  "18142": 9,
  "18144": 7,
  "18146": 9,
  "18152": 9,
  "18155": 7,
  "18159": 5,
  "18161": 7,
  "18164": 7,
  "18167": 11,
  "18170": 9,
  "18173": 9,
  "18176": 11,
  "18179": 9,
  "18180": 5,
  "18183": 13,
  "18184": 5,
  "18186": 3,
  "18190": 21,
  "18193": 7,
  "18196": 11,
  "18199": 13,
  "18200": 3,
  "18203": 5,
  "18206": 11,
  "18209": 11,
  "18212": 9,
  "18215": 11,
  "18218": 9,
  "18221": 15,
  "18223": 2,
  "18225": 9,
  "18228": 13,
  "18231": 13,
  "18234": 15,
  "18237": 19,
  "18240": 13,
  "18243": 17,
  "18245": 3, 
}


def extract_tos_main(path):
  if not path.endswith(".pdf"):
    print("Path to folder was entered. Every PDF in folder will be split.")
    for file in os.listdir(path):
        if file.endswith(".pdf"):
            split_single_file(path + "\\" + file)
  else:
    split_single_file(path)


def split_single_file(file_path):
  folder_path = "\\".join(file_path.split("\\")[:-1])
  file_name = file_path.split("\\")[-1]
  file_name_without_ending = file_name[0:-4]

  file_path_tos = folder_path + "\\tos\\" + file_name_without_ending + ".pdf"
  file_path_main = folder_path + "\\main\\" + file_name_without_ending + ".pdf"

  stream = os.popen(f'pdftk "{file_path}" dump_data')
  output = stream.read()

  outlined_pages = re.findall('BookmarkPageNumber: (.+)\n', output)
  
  # TODO if file name in dict use its values
  if file_name_without_ending in SPLIT_EXCEPTIONS:
    print("Split exception found for file " + file_name)
    first_split = SPLIT_EXCEPTIONS[file_name_without_ending]
  else:
    first_split = int(outlined_pages[FIRST_BOOKMARK_SPLIT])
  second_split = int(outlined_pages[SECOND_BOOKMARK_SPLIT])
  
  print("Splitting file: " + file_name + " at pages " + str(first_split), " and " + str(second_split))

  os.popen(f'pdftk "{file_path}" cat 1-{first_split-1} output "{file_path_tos}"')
  os.popen(f'pdftk "{file_path}" cat {first_split}-{second_split-1} output "{file_path_main}"')
  


file = sys.argv[1]

extract_tos_main(file)  
