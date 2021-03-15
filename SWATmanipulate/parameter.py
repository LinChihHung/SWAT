"""Chih Hung, Lin 2021.03.15

"""

import os
import numpy as np


class InputFileManipulator(object):
    def __init__(self, fileName):
        self.fileName = fileName
        parFile = open(self.fileName, "r")
        self.textOld = parFile.readlines()
        parFile.close()
