const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');


function startdown(){
    navigator.mediaDevices.getUserMedia({   //if not work please refer coomplete writing on network
        audio:false,
        video:{facingMode:'environment'}    //facingmode not work please update your browser and try again
    }).then(stream =>{
        video.srcObject = stream;
        localStream = stream;
    }).catch(console.error)

}

function success(stream){
    var CompatibleURL=window.URL || window.webkitURL;
    video.src=CompatibleURL.createObjectURL(stream);
    video.play();
    getpost();
}

function error(error){
    console.log('found erro: ',error.name,error.message);
}

function stopvideo(){
    this.video.pause();
    this.video.src='';
    this.video.srcObject=null;
    if(this.localStream=stream)
        this.localStream.getVideoTracks().forEach(track=>track.stop());
}

var postval = function(){
                vv = document.getElementById('ajx').innerHTML
                context.drawImage(video,0,0,1000,1000)
                img = canvas.toDataURL('image/jpg')
                img = img.split(',')[1]
                $.post({
                    url:'/scanner/scanner/',
                    data:{
                      mg :img
                    },
                    success:function(data){
                            $('#ajx').html(data)
                    },
                    error:function (callback){
                        $('#ajx').val(callback);
                    }
                });
                if (vv !== "hello"&& vv !=="not read" && vv !=="check"){
                stopvideo();
                (function(){ window.setTimeout(()=>{return 0;},5000);
                });}}

window.addEventListener('load',startdown,false)
$(document).ready(function(){
    $("#b1").click(function(){
        startdown();
        var tt = window.setInterval(postval,150);
        $("#b2").click( async function(){
        window.clearInterval(tt);
        document.getElementById('ajx').innerHTML = 'check';
    });
    });

});
