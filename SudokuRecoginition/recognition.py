import os
import pickle
import sys

import numpy as np

from Script.sudokuExtractor import Extractor
from Script.train import NeuralNetwork
from Script.sudoku_str import SudokuStr
from Script.cells import get_cells
from Script.
def recognize(image, model, old_sudoku):
    # Your recognize function code here
    pass

import cv2
import numpy as np

def snap_sudoku(image_path):
    grid = ''.join(cell for cell in get_cells(image_path))
    s = SudokuStr(grid)

if __name__ == "__main__":
    input_image_path = "C:/Users/Modi Yash/Desktop/Sudoku/Streamlit-Sudoku-Solver-Python-master/data/s3.png"  
    output_image = snap_sudoku(input_image_path)
    
    # cv2.imshow("Sudoku Grid", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

