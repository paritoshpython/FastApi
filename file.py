from fastapi import APIRouter
import api
file_route=APIRouter(
    tags=['File']
)

app=file_route

@app.get("/")
def index():
    return {'helo':'welcome to file api'}

# =================================  file download  ======================================
#  for download file we will use custom http Response 
from fastapi.responses import Response ,RedirectResponse
from fastapi import File, UploadFile

# =================================== downloadfiles ( file from your system )===============
# checkout  http://127.0.0.1:8000/file/downloadfile/

@app.get("/downloadfile/")
def download_file():
    path=f'{api.FILE_ROOT}/first.txt'
    with open(path, 'rb') as f:
        data=f.read()
        headers={'Content-Language':'Gujarati' ,'Content-Type': 'text/plain'
                
                 }    
        headers['Content-Disposition']= "attachment;filename=okfilename.txt"
        response=Response(content=data,  headers=headers,media_type='text/plain')
        return response

# =============================== make redirect response and download file ===================
# checkout  http://127.0.0.1:8000/file/getmyfile/

@app.get("/getmyfile/")
def getmy_file():
    return RedirectResponse("http://127.0.0.1:8000/file/downloadfile/",status_code=303)

''' by using status_code=303 it is tempory response and thats cool nither when u do 
redirect it will show your content on webpage plus download your file but with code 303 it only
download file :)'''

# =================================== Upload and download file  =============================

@app.post("/uploadanddownload/")
async def upload_download(file: bytes = File()):

    #  do somrthing with your file and that output put in content
    # print(dir(file))
    headers={'Content-Language':'Gujarati' ,'Content-Type': 'text/plain'
            }    
    headers['Content-Disposition']= "attachment;filename=okfilename.txt"
    response=Response(content=file,  headers=headers,media_type='text/plain')
    return response

# =================================== Large size file =================================
#  here we will see mp4 video to text file 
# checkout  http://127.0.0.1:8000/file/mp4file/

'''
@app.get("/mp4file/")
def download_file():
    with open('files/veryhard.mp4', 'rb') as f:
        data=f.read()
        headers={'Content-Language':'Gujarati' ,'Content-Type': 'text/plain'
                
                 }    
        headers['Content-Disposition']= "attachment;filename=mp4okfilename.txt"
        response=Response(content=data,  headers=headers,media_type='text/plain')
        return response
''' 

# ================================== large size pdf =============================

@app.get("/pdf/")
def download_pdf_file():
    path=f'{api.FILE_ROOT}/mypdf.pdf'
    with open(path, 'rb') as f:
        data=f.read()
        headers={'Content-Language':'English' ,'Content-Type': 'application/pdf'
                
                 }    
        headers['Content-Disposition']= "attachment;filename=mypdf.pdf"
        response=Response(content=data,  headers=headers,media_type='application/pdf')
        return response

# -------------------------------- new style ------------------------------------------------------------

@app.get("/newstyle/")
def download_new_file():
    with open('files/first.txt', 'rb') as f:
        data=f.read()
        headers={'Content-Language':'Gujarati' ,'Content-Type': 'text/plain'
                
                 }   
        response=Response(content=data,media_type='text/plain',headers=headers)
        response.headers['Content-Disposition']="attachment;filename=okfilename.txt"
        return response

# ===================================== image converter   ==============================
from PIL import Image
from io import BytesIO

@app.get("/image/")
def image_converter():
        path=f'{api.IMAGE_ROOT}/myjpeg.jpeg'
        print("path:",path)
        image=Image.open(path)
        # image.format='jpeg'
        # ----------------------------
        image=image.convert('RGB')
        image_io = BytesIO()
        image.save(image_io, format='png')
        
        output=image_io.getvalue()
        # print(output) our output in bytes
 
        response=Response(content=output, media_type='Image/png')
        response.headers['Content-Disposition']="attachment;filename=your.png"
        return response

'''
in uper image_converter  we converted our image into rgb then we save image but we saved
in bytes by BytesIO and we have to return this image in response so that we need bytes
so that we get output=image_io.getvalue() and then that output we transfer in content=output
because our Reponse( content=only accpet bytes or srting )
our type(image) has PIL.image type so that we cant directly transfer int

''' 
    
    