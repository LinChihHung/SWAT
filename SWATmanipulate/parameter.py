"""Chih Hung, Lin 2021.03.16
完成初步的參數配置，能將參數透過code寫入並改變參數值，無須透過GUI。
但僅限格是簡單的參數，如:gw、rte等。sol較為複雜，尚未寫完。
"""

import os
import numpy as np
import re


class InputFileManipulator(object):
    def __init__(self, fileName, parList):
        self.fileName = fileName
        self.textOrigin = self.loadText(fileName)
        self.subbasin = None
        self.landuse = None
        self.soil = None
        self.slope = None
        self.attributes()
        self.initialParValue(parList)
        self.prepareChangePar()

    def loadText(self, fileName):
        with open(fileName, "r") as f:
            textOrigin = f.readlines()

        return textOrigin

    def attributes(self):
        attributes = re.split(":| ", self.textOrigin[0])
        while "" in attributes:
            attributes.remove("")

        self.subbasin = attributes[attributes.index("Subbasin") + 1]
        self.landuse = attributes[attributes.index("Luse") + 1]
        self.soil = attributes[attributes.index("Soil") + 1]
        self.slope = attributes[attributes.index("Slope") + 1]

    def initialParValue(self, parList):
        for namePar in parList:
            row, col1, col2, dig = self.parInfo[namePar]
            self.parValue[namePar] = [float(self.textOrigin[row - 1][col1:col2])]

    def prepareChangePar(self):
        self.textNew = self.textOrigin[:]  # copy instead of new name allocation

    # built to be overridden if one parameter exists several times in each file, e.g. for different soil layers
    def setChangePar(self, namePar, changePar, changeHow):
        self.changePar(namePar, changePar, changeHow)

    # built to be overridden if one parameter exists several times in each file, e.g. for different soil layers to change single Layers by S.Julich apr 09
    def setChangeParLay(self, namePar, changePar, changeHow):
        self.changePar(namePar, changePar, changeHow)

    # offset- and index-values are only relevant, if setChangePar is overridden

    def changePar(self, namePar, changePar, changeHow):
        # change initial parameter depending on chosen method
        changePar = float(changePar)
        if changeHow == "+":
            changedPar = self.parValue[namePar][index] + changePar
        elif changeHow == "*":
            changedPar = (
                self.parValue[namePar][index]
                + self.parValue[namePar][index] * changePar
            )
        elif changeHow == "s":
            changedPar = changePar
        # insert changed Parameter in textNew
        row, col1, col2, dig = self.parInfo[namePar]
        format = "%" + str(col2 - col1 + 1) + "." + str(dig) + "f"
        self.textNew[row - 1] = (
            self.textNew[row - 1][: col1 - 1]
            + (format % changedPar).rjust(col2 - col1 + 1)
            + self.textNew[row - 1][col2:]
        )

    # save textNew in file (file ready for SWAT)
    def finishChangePar(self):
        with open(self.fileName, "w") as f:
            f.writelines(self.textNew)
        self.prepareChangePar()


class gwManipulator(InputFileManipulator):

    # information about parameters:
    # (1)row in file, (2) first and (2) last relevant column in row
    # and (4) digits
    parInfo = {
        "SHALLST": (2, 1, 16, 5),
        "DEEPST": (3, 1, 16, 5),
        "GW_DELAY": (4, 1, 16, 5),
        "ALPHA_BF": (5, 1, 16, 5),
        "GWQMN": (6, 1, 16, 5),
        "GW_REVAP": (7, 1, 16, 5),
        "REVAPMN": (8, 1, 16, 5),
        "RCHRG_DP": (9, 1, 16, 5),
        "GWHT": (10, 1, 16, 5),
        "GW_SPYLD": (11, 1, 16, 5),
        "SHALLST_N": (12, 1, 16, 5),
        "GWSOLP": (13, 1, 16, 5),
        "HLIFE_NGW": (14, 1, 16, 5),
        "LAT_ORGN": (15, 1, 16, 5),
        "LAT_ORGP": (16, 1, 16, 5),
        "ALPHA_BF_D": (17, 1, 16, 5),
    }

    # expands init-method of FileManipulator to generate parValue-dictionaries for individual instances
    def __init__(self, filename, parList):
        self.parValue = {
            "SFTMP": None,
            "SHALLST": None,
            "DEEPST": None,
            "GW_DELAY": None,
            "ALPHA_BF": None,
            "GWQMN": None,
            "GW_REVAP": None,
            "REVAPMN": None,
            "RCHRG_DP": None,
            "GWHT": None,
            "GW_SPYLD": None,
            "SHALLST_N": None,
            "GWSOLP": None,
            "HLIFE_NGW": None,
            "LAT_ORGN": None,
            "LAT_ORGP": None,
            "ALPHA_BF_D": None,
        }
        InputFileManipulator.__init__(self, filename, parList)


if __name__ == "__main__":
    """Test Example"""
    # os.chdir(
    #     r"D:\03.Model\SWAT\ShihmenReservoir\Run20210224\Scenarios\Calib_V1\TxtInOut"
    # )
    # filesList = os.listdir()
    # gwfiles = [i for i in filesList if i.endswith(".gw") and i[0].isdigit]
    # gw = []
    # for i in gwfiles:
    #     gw.append(
    #         gwManipulator(
    #             i, ["GW_DELAY", "ALPHA_BF", "GW_REVAP", "GWQMN", "RCHRG_DP", "REVAPMN"]
    #         )
    #     )

    # delay = "300"
    # for d in gw:
    #     d.setChangePar("GW_DELAY", delay, "s")
    #     d.finishChangePar()