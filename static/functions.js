
const imgcontent = document.querySelector('.profile-photo-content');

const img = document.querySelector('#photo');

const file = document.querySelector('#profile-photo');

const uploadBtn = document.querySelector('#btnupload');


//if user hover on profile div
imgcontent.addEventListener('mouseenter', function(){
    uploadBtn.style.display = "block"
});

// if we hover out from img div
imgcontent.addEventListener('mouseleave', function(){
    uploadBtn.style.display = "none"
});

//lets work for image showing funcion
file.addEventListener('change', function(){
    const choosedFile = this.files[0];

    if (choosedFile) {
        const reader = new FileReader();

        reader.addEventListener('load', function(){
            img.setAttribute('src', reader.result);
        });

        reader.readAsDataURL(choosedFile);
    }

});