from docx import Document
import pandas as pd
import os
import time
# fileType -> "excel"|"word"|"txt"|"none"
def checkAndUpdated(filePath:str=None,searchKeys:str=None):
    if(filePath == None or searchKeys == None):
        raise ValueError("文件路径和搜索关键字不能为空")
    
    try:
        if filePath.endswith(".xlsx") or filePath.endswith(".xls"):
            file = pd.read_excel(filePath)
            updatedExcel(file,searchKeys)
        elif filePath.endswith(".docx"):
            file = Document(filePath)
            updatedWord(file,searchKeys)
        elif filePath.endswith(".txt"):
            with open(filePath,"r",encoding="utf-8") as file:
                file_content = file.read()
            file = file_content
            updatedTxt(file,searchKeys)
        else:
            raise ValueError("不支持当前文件类型")
    except Exception as e:
        print(f"读取文件出错：{e}")
        return
    return

def updatedExcel(file,keys):
    return
def updatedWord(file,keys):
    for paragraph in file.paragraph:
        if text==keys in paragraph.text:
            paragraph.text = paragraph.text.replace(text)
    return
def updatedTxt(file,keys):
    return
