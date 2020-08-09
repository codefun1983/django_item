# django_item 
## linux only

- [youtube_downloader](https://github.com/codefun1983/django_item/tree/master/youtube_download)
  - usage : create two terminal
    1. terminal 1 : run web server, ex:apache, nginx, django runserver 
    2. terminal 2 : run celery
       - command: 
        ```html 
        celery -A app worker -l info

- [qrcode_online_scanner](https://github.com/codefun1983/django_item/tree/master/qrcode_online_scanner)
  - notice : ssl needs if static file exist
    - use web server, ex : apache, nginx, django ssl-runserver or socat(port-forward app) etc..
  - this function is experimental ; in my opinion, this is not useful.
