from functions import *
# print(readFile("../files/outputs/TEST.txt"))
files = getFiles()
# for file in files["outputs"]:
#     print(file)
processedFiles = processFiles(files)
a2 = calculateTextSimilarity(processedFiles)
generateExcelReport(a2)





