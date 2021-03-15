import os
import shutil


class SwatStart:
    def __init__(self, modelPath, originFilePath, newFilePath):
        self.modelPath = modelPath
        self.originFilePath = originFilePath
        self.newFilePath = newFilePath
        self.makeDir()

    def makeDir(self):
        if os.path.exists(self.newFilePath):
            print("-----------------------------------")
            print("Deleting folder " + self.newFilePath)
            shutil.rmtree(self.newFilePath)
            print("-----------------------------------")
            print("Copying folder ", self.originFilePath)
            shutil.copytree(self.originFilePath, self.newFilePath)
        else:
            print("Copying folder ", self.originFilePath)
            shutil.copytree(self.originFilePath, self.newFilePath)

    # def makeDir(self):
    #     if os.path.exists(self.newFilePath):
    #         flag = True
    #         ask1 = input(
    #             "File already exist, do you want to overwrite the file? (y/n): "
    #         )
    #         while flag:
    #             if ask1 == "y":
    #                 flag2 = True
    #                 ask2 = input(
    #                     "Please confirm again, you really wnat to overwrite the file? (y/n): "
    #                 )
    #                 while flag2:
    #                     if ask2 == "y":
    #                         print("-----------------------------------")
    #                         print("Deleting folder " + self.newFilePath)
    #                         shutil.rmtree(self.newFilePath)
    #                         print("-----------------------------------")
    #                         print("Copying folder ", self.originFilePath)
    #                         shutil.copytree(self.originFilePath, self.newFilePath)
    #                         flag = False
    #                         flag2 = False
    #                     else:
    #                         flag2 = False
    #             elif ask1 == "n" or ask2 == "n":
    #                 raise FileExistsError
    #             else:
    #                 print("Please input 'y' or 'n' ")
    #     else:
    #         print("Copying folder ", self.originFilePath)
    #         shutil.copytree(self.originFilePath, self.newFilePath)