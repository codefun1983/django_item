import os
import re
import string
from random import choices
from pytube import YouTube,request
from youtube_download.settings import BASE_DIR



def tube_code_exc(req,media_type,exc):
    posturl = req.POST.get('jk')
    vformat = req.POST.get('videotype')
    vloc = 'static/'
    vpath = os.path.join(BASE_DIR, vloc)
    messtr = string.ascii_letters + string.digits
    codemess = choices(messtr, k=10)
    mam = ''
    for mess in codemess:
        mam += mess
    os.system('touch %s%s.mp4' % (vpath, mam))
    vopen = open('%s%s.mp4' % (vpath, mam), 'wb')
    if media_type == 2:
        YouTube('%s'%posturl).streams.get_highest_resolution().stream_to_buffer(vopen)
    else:
        YouTube('%s'%posturl).streams.get_audio_only().stream_to_buffer(vopen)
    ftype = YouTube('%s' % posturl).streams.first().subtype
    fpn = '%s%s.%s' % (vpath, mam, ftype)
    meloc = '/'+vloc+mam+"."+ftype
    fchange = "'" + vpath + mam + '.' + vformat + "'"
    fileloc = '/' + vloc + mam + '.' + vformat
    if exc != 1:
        try:
            vname = YouTube('%s' % posturl).streams.first().title
            # if title disappear YouTube, using next method below this one
            '''
            hcontent = request.get('%s'%posturl)
            hstart = hcontent.find('\\"title\\"', 0)
            hend = hcontent.find(',', hstart)
            vname = hcontent[hstart+12:hend-2]
            '''
            for xfilter in string.punctuation:
                try:
                    vname = vname.replace(xfilter, '')
                except:
                    pass
            vname = vname.replace(' ', '-')
            fchange = "'" + vpath + vname + '.' + vformat + "'"
            fileloc = '/' + vloc + vname + '.' + vformat
        except:
            print('something wrong...')
    os.system('cp %s %s' % (fpn, fchange))
    aa = os.popen('mimetype %s' % fchange).read()
    fmine = re.split(':', aa)[1].lstrip(" ")
    context = {'meloc':meloc,'fileloc': '%s' % fileloc, 'fmine': fmine,'fpn':fpn,'fchange':fchange}
    print('now is delete....')
    return(context)