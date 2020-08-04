import os
import PyPDF2
import json
arr = os.listdir()
l=[]
namess=[]
for pdf in arr:
    try:
        k=pdf.split(".")
        if k[1]=="pdf":
            l.append(pdf)
            namess.append(k[0])    
    except:
        pass
print(l)   
pagenumber=[]
result=[]
jos=0   
for filename in l:
    qa=[]
    page=[]
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader('GYANM-JUNE-GK-2019-ENGLISH-VERSION.pdf')
    number=pdfReader.numPages
    for filenumber in range(0,100):
        pageObj = pdfReader.getPage(filenumber)
        if "Latest" in pageObj.extractText() and "Bytes" in pageObj.extractText():
            number=filenumber
    try:          
        for j in range(number,101):
            pageObj = pdfReader.getPage(j)
            dict1={}
            x1=pageObj.extractText()
            x1=x1.replace("\n"," ")
            x2=x1.split(" ) ")
            x2.pop(0)
            for j in range(len(x2)):
                question=x2[j]
                question=question[:-3]
                q_and_a=re.split(r'[?]|[:]',question)
                dict1["page"]=i
                dict1["question%s"%j]=q_and_a

                qa.append(dict1)
    except:
        pass                
    pdfFileObj.close()
    namessss=namess[jos]+".json"    
    with open(namessss,'w') as f:
        json.dump(qa,f)
    jos=jos+1    
