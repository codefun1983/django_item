from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .function import tube_code_exc
from .task import ppop
# Create your views here.

@csrf_exempt
def youtube(req):
    if req.method == 'POST':
        posturl = req.POST.get('jk')
        vformat = req.POST.get('videotype')
        acheck = posturl.find('https://www.youtube.com/watch?v=')
        bcheck = posturl.find('https://www.youtube.com/emded/')
        if acheck == 0 or bcheck == 0:
            if vformat == 'mp3' or vformat == 'aviaudio':
                try:
                    if vformat == 'aviaudio':
                        vformat = 'avi'
                    fresult= tube_code_exc(req,media_type=1,exc=0)
                    ppop.delay(fresult['fchange'],fresult['fpn'])
                    return render(req, 'mp3.html', context=fresult)
                except:
                    if vformat == 'aviaudio':
                        vformat = 'avi'
                    fresult= tube_code_exc(req,media_type=1,exc=1)
                    ppop.delay(fresult['fchange'], fresult['fpn'])
                    return render(req, 'mp3.html', context=fresult)
            else:
                try:
                    fresult = tube_code_exc(req,media_type=2,exc=0)
                    ppop.delay(fresult['fchange'],fresult['fpn'])
                    return render(req, 'mp4.html', context=fresult)
                except:
                    fresult = tube_code_exc(req,media_type=2,exc=1)
                    ppop.delay(fresult['fchange'],fresult['fpn'])
                return render(req, 'mp4.html', context=fresult)
        else:
            return HttpResponse('Wrong site! This web only support Youtube download, please input Youtube website.')
    return render(req, 'mp3.html')
