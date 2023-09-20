import os
import openpyxl
from difflib import SequenceMatcher


def getFiles():
    dirOutputs = "../files/outputs/"
    dirModels = "../files/models/"
    outputs = os.listdir(dirOutputs)
    models = os.listdir(dirModels)
    filesOutput = {}
    filesModel = {}
    files =  {}
    for file in outputs:
        filePath = dirOutputs + file
        reading = readFile(filePath)
        fileObject = {
            "name":file,
            "directory": filePath,
            "content":reading["content"],
            #"content":"aaa",
            "length": reading["length"]
        }
        filesOutput[file] = fileObject
    for file in models:
        filePath = dirModels + file
        reading = readFile(filePath)
        fileObject = {
            "name":file,
            "directory": filePath,
            "content":reading["content"],
            #"content":"aaa",
            "length": reading["length"]
        }
        filesModel[file] = fileObject
    files = {
        "outputs":filesOutput,
        "models": filesModel
    }
    return files


def readFile(path):
    with open(path, 'r') as file:
        content = file.read()
        lines = content.split('\n')
        reading = {
            "content":content,
            "length": len(lines)
        }
    return reading

def generateExcelReport(files):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet['A1'] = "FILE"
    sheet['B1'] = "LENGTH OUTPUT"
    sheet['C1'] = "LENGTH MODEL"
    sheet['D1'] = "% SIMILARITY"
    i = 2
    for file in files:
        currentFile = files[file]
        columnFile = "A"+str(i)
        columnLengthOutput = "B"+str(i)
        columnLengthModel = "C"+str(i)
        columnSimilarity = "D"+str(i)
        sheet[columnFile] = currentFile["name"]
        sheet[columnLengthOutput] = currentFile["output"]["length"]
        sheet[columnLengthModel] = currentFile["model"]["length"]
        sheet[columnSimilarity] = currentFile["similarity"]
        i= i+1
    workbook.save("../files/reports/report.xlsx")





def processFiles(files):
    outputs = files["outputs"]
    models = files["models"]
    processedFiles = {}
    for file in models:
        if(file in outputs):
            fileObject = {
                "name": file,
                "output": {
                    "content": outputs[file]["content"],
                    "length": outputs[file]["length"]
                },
                "model": {
                    "content": models[file]["content"],
                    "length": models[file]["length"]
                }
            }
            processedFiles[file] = fileObject
    return processedFiles

def calculateTextSimilarity(files):
    for file in files:
        similarity = (SequenceMatcher(None, files[file]["output"]["content"], files[file]["model"]["content"]).ratio())*100
        files[file]["similarity"] = similarity
    return files