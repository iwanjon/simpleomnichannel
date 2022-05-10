console.log('hello world upload')
console.log("ccc")
const uploadForm = document.getElementById('upload-form')
// console.log(uploadForm)
const input = document.getElementById('id_file')
const butttonsubmit = document.getElementById('buttoninput')

// console.log(input)
//  $('.form-group input').addClass("form-control")
const alertBox = document.getElementById('alert-box')
const imageBox = document.getElementById('image-box')
const progressBox = document.getElementById('progress-box')
const cancelBox = document.getElementById('cancel-box')
const cancelBtn = document.getElementById('cancel-btn')
// const submitbutton = document.getElementById('subsub')
// console.log(submitbutton,"ccc")

const csrf = document.getElementsByName('csrfmiddlewaretoken')

butttonsubmit.addEventListener("click", ()=>{
    progressBox.classList.remove('not-visible')
    // cancelBox.classList.remove('not-visible')

    const img_data = input.files[0]
    const url = URL.createObjectURL(img_data)
    console.log(img_data,"image data", img_data["File"], img_data['file'])

    let fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('file', img_data)
    console.log(fd,"fffdd")
    console.log(fd.file,"fffdd")
    console.log(fd.csrfmiddlewaretoken,"fffdd")

    $.ajax({
        type:'POST',
        url: uploadForm.action,
        enctype: 'multipart/form-data',
        data: fd,
        processData : false,
        contentType : false,
        beforeSend: function(){
            console.log('before', url,"ll")
            alertBox.innerHTML= ""
            imageBox.innerHTML = ""
        },
        xhr: function(){
            const xhr = new window.XMLHttpRequest();
            xhr.upload.addEventListener('progress', e=>{
                // console.log(e)
                if (e.lengthComputable) {
                    const percent = e.loaded / e.total * 100
                    console.log(percent)
                    progressBox.innerHTML = `<div class="progress">
                                                <div class="progress-bar" role="progressbar" style="width: ${percent}%" aria-valuenow="${percent}" aria-valuemin="0" aria-valuemax="100"></div>
                                            </div>
                                            <p>${percent.toFixed(1)}%</p>`
                }

            })
            cancelBtn.addEventListener('click', ()=>{
                xhr.abort()
                setTimeout(()=>{
                    uploadForm.reset()
                    progressBox.innerHTML=""
                    alertBox.innerHTML = ""
                    cancelBox.classList.add('not-visible')
                }, 2000)
            })
            return xhr
        },
        success: function(response){
            console.log(response)
            // imageBox.innerHTML = `<img src="${url}" width="300px">`
            alertBox.innerHTML = `<div class="alert alert-success" role="alert">
                                    Successfully uploaded the image below
                                </div>`
            cancelBox.classList.add('not-visible')
        },
        error: function(error){
            console.log(error)
            alertBox.innerHTML = `<div class="alert alert-danger" role="alert">
                                    Ups... something went wrong
                                </div>`
        },
        cache: false,
        contentType: false,
        processData: false,
    })
});
// uploadForm.addEventListener('submit', ()=>{
//     progressBox.classList.remove('not-visible')
//     cancelBox.classList.remove('not-visible')

//     const img_data = input.files[0]
//     const url = URL.createObjectURL(img_data)
//     console.log(img_data)

//     const fd = new FormData()
//     fd.append('csrfmiddlewaretoken', csrf[0].value)
//     fd.append('image', img_data)

//     $.ajax({
//         type:'POST',
//         url: uploadForm.action,
//         enctype: 'multipart/form-data',
//         data: fd,
//         beforeSend: function(){
//             console.log('before')
//             alertBox.innerHTML= ""
//             imageBox.innerHTML = ""
//         },
//         xhr: function(){
//             const xhr = new window.XMLHttpRequest();
//             xhr.upload.addEventListener('progress', e=>{
//                 // console.log(e)
//                 if (e.lengthComputable) {
//                     const percent = e.loaded / e.total * 100
//                     console.log(percent)
//                     progressBox.innerHTML = `<div class="progress">
//                                                 <div class="progress-bar" role="progressbar" style="width: ${percent}%" aria-valuenow="${percent}" aria-valuemin="0" aria-valuemax="100"></div>
//                                             </div>
//                                             <p>${percent.toFixed(1)}%</p>`
//                 }

//             })
//             cancelBtn.addEventListener('click', ()=>{
//                 xhr.abort()
//                 setTimeout(()=>{
//                     uploadForm.reset()
//                     progressBox.innerHTML=""
//                     alertBox.innerHTML = ""
//                     cancelBox.classList.add('not-visible')
//                 }, 2000)
//             })
//             return xhr
//         },
//         success: function(response){
//             console.log(response)
//             imageBox.innerHTML = `<img src="${url}" width="300px">`
//             alertBox.innerHTML = `<div class="alert alert-success" role="alert">
//                                     Successfully uploaded the image below
//                                 </div>`
//             cancelBox.classList.add('not-visible')
//         },
//         error: function(error){
//             console.log(error)
//             alertBox.innerHTML = `<div class="alert alert-danger" role="alert">
//                                     Ups... something went wrong
//                                 </div>`
//         },
//         cache: false,
//         contentType: false,
//         processData: false,
//     })
// })

