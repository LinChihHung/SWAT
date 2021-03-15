import os
import shutil
from SWATmanipulate.start import SwatStart

# from SWATmanipulate.parameter import


def main():
    MODELPATH = r"D:\03.Model\SWAT\ShihmenReservoir\Run20210224\Scenarios"
    originFilePath = os.path.join(MODELPATH, "Default")
    newFilePath = os.path.join(MODELPATH, "Calib_V1")

    # 
    SwatStart(
        modelPath=MODELPATH, originFilePath=originFilePath, newFilePath=newFilePath
    )

    txtPath = os.path.join(newFilePath, "TxtInOut")
    os.chdir(txtPath)
    filesList = os.listdir()

    mgtFiles = [i for i in filesList if i.endswith(".mgt") and i[0].isdigit()]
    hruFiles = [i for i in filesList if i.endswith(".hru") and i[0].isdigit()]
    rteFiles = [i for i in filesList if i.endswith(".rte") and i[0].isdigit()]
    solFiles = [i for i in filesList if i.endswith(".sol") and i[0].isdigit()]
    gwFiles = [i for i in filesList if i.endswith(".gw") and i[0].isdigit()]


if __name__ == "__main__":
    main()