from urllib import response
import requests
import io
from io import StringIO,BytesIO
# data=1.png
# print(type(data))

# with open('1.png', 'rb') as f:
#      print(type(f))
#     #  f=f.read()
#      # f.decode('cp1252')

f= {"file":open('files/first.txt','rb')}     
# response=requests.post("http://127.0.0.1:8000/doc/uploadfile/", files=f)

response=requests.post("http://127.0.0.1:8000/file/downloadfile/", files=f)
print((dir(response)))

#  Responce Data
print('--------------------------- Responce Data --------------------------')
print("response:",response)
print("content:",response.content)
print("response type:",type(response.content))
print("headers:",response.headers)
print("encoding:",response.encoding)
print("iter_content:",response.iter_content)
print('text:',response.text)

# request data
print("-------------------------  request data  -------------------------------")
print("headers :", response.request.headers) 
print("path_url :", response.request.path_url)
# print("body :", response.request.body) 
print("url :", response.request.url)