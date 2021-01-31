const uploadform=document.getElementById('sample')

const input=document.getElementById('id_pic')
const progressbars=document.getElementById('progress-bar')

const cancel_btn=document.getElementById('cancel-btn')
const cancelbox=document.getElementById('cancel-box')
const alertbox=document.getElementById('alert-box')
const imagebox=document.getElementById('image-box')




const csrf=document.getElementsByName('csrfmiddlewaretoken')

input.addEventListener('change',()=>{
    progressbars.classList.remove('not-visible')
    cancelbox.classList.remove('not-visible')

    const img_data = input.files[0]
   
    const url=URL.createObjectURL(img_data)

    const fd= new FormData()
    fd.append('csrfmiddlewaretoken',csrf[0].value)
    fd.append('pic',img_data)

    $.ajax({

        type:'POST',
        url: uploadform.action,
        enctype:'multipart/form-data',
        data:fd,
        beforeSend: function(){
            alertbox.innerHTML=""

        },
        xhr: function(){

            const xhr = new window.XMLHttpRequest();
            xhr.upload.addEventListener('progress',e=>{
                if (e.lengthComputable){
                    const percent= e.loaded/e.total * 100
                    progressbars.innerHTML=`<div class="progress">
                    <div class="progress-bar" role="progressbar" style="width: ${percent}%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                    <p>${percent.toFixed(1)}%</p>`
  
                }
            })

            cancel_btn.addEventListener('click',()=>{
                xhr.abort();
                setTimeout(()=>{
                    uploadform.reset()
                    progressbars.innerHTML="";
                    cancelbox.classList.add('not-visible');

                },2000)
                
            })
            return xhr
            
        },
        success: function(response){
            imagebox.innerHTML=`<img src="${url}" width="150px">`
            alertbox.innerHTML=`<div class="alert alert-success" role="alert">
                                Profile Picture has been uploaded successfully.
                                </div>`
            progressbars.innerHTML=""
            cancelbox.classList.add('not-visible')
        },
        error: function(error){
          alertbox.innerHTML=`<div class="alert alert-danger" role="alert">
          Oops Some thing went wrong!!
          </div>`
        },
        cache: false,
        contentType: false,
        processData:false,
    })
    

})