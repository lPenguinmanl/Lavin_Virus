import os
import numpy as np
from multiprocessing import Pool 
import time


def Search_files(name_part):
  global all_files
  n_part = np.array(name_part, str)
  for address, dirs, files in os.walk('C:\\', topdown=True):
    for file in files:
      print(file)
    
if __name__ == "__main__":
  f = time.perf_counter()
  with Pool(3) as p:
    pass
    #p.map(Search_files, [part_one, part_two, part_three])
  

  #print(time.perf_counter() - f)
