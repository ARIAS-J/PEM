
const img = document.querySelector('#photo');

const file = document.querySelector('#profile-photo');

const uploadBtn = document.querySelector('#btnupload');


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