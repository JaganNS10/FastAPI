from fastapi import FastAPI,File,UploadFile
from typing import Annotated,List


app = FastAPI()



@app.post("/file")
def File_File(file:Annotated[bytes,File()]):
    return len(file)


@app.post("/")
def Upload_File(file:UploadFile):
    print(file.file)
    return file.filename


#upload multiple fields
@app.post("/multiplefiles")
def Multiple_Files_File(files:Annotated[List[bytes],File()]):
    return [len(i) for i in files]

@app.post("/multiplefilesupload")
def Multiple_Files_UploadFile(files:List[UploadFile]):
    return [i.filename  for i in files]


from fastapi.responses import HTMLResponse



@app.get("/usinghtml")
def UsingHtml():
    content = """ 
    <body>
    <form action='http://127.0.0.1:8000/multiplefilesupload' enctype='multipart/form-data' method='post'>
        Upload: <input type='file' name='files' multiple>
        <button type='submit'>Submit</button>
    </form>
    </body>
    """
    return HTMLResponse(content=content)
