import os
import shutil

def upsampleAndDuplicateFiles(wakewordsDir, copyDestination, copyNumber):
    ones = os.listdir(wakewordsDir)
    destDir = os.path.join(copyDestination, 'subfolder')
    os.makedirs(destDir, exist_ok=True)

    for file in ones:
        if file.endswith(".wav") or file.endswith(".mp3"):
            srcFile = os.path.join(wakewordsDir, file)

            destFile = os.path.join(destDir, file)
            shutil.copy(srcFile, destFile)
            newDestFile = os.path.join(destDir, str(0) + "_" + file)
            os.rename(destFile, newDestFile)

            for i in range(1, copyNumber):
                newDestFile = os.path.join(destDir, str(i) + "_" + file)
                shutil.copy(srcFile, newDestFile)

if __name__ == "__main__":
    wakewordsDir = "C:\Code\HoyaHacks2024\one"
    copyDestination = "C:\Code\HoyaHacks2024\one\sub"
    copyNumber = 84  

    upsampleAndDuplicateFiles(wakewordsDir, copyDestination, copyNumber)
