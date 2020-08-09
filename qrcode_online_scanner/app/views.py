import base64
from io import BytesIO
from PIL import Image
from django.http import HttpResponse
from django.shortcuts import render
from pyzbar import pyzbar
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def scanner(req):
    if req.method=='POST':
        mg =req.POST['mg']
        imgdata = base64.b64decode(mg)
        imgdata=Image.open(BytesIO(imgdata))

        try:
            texts = pyzbar.decode(imgdata)
            if texts == []:
                return HttpResponse('not read') # here will return to html $("#ajx")
            else:
                for text in texts:
                        data = text.data.decode('utf8')
                        if data:
                            #<your scan strategy>
                return HttpResponse('read')
        except:
            pass
    context = {'data':'hello'}
    return render(req,'scanner.html',context=context)
