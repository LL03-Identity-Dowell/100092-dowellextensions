window.onload = (event) => { 
    event.default();
    revealImages() 
    };

function simClick(){
        
    document.getElementById('getFile').click();            
        };
function fileSelect(){    
    
    var file = document.getElementById('getFile').files[document.getElementById('getFile').files.length - 1];
    document.getElementById('fileName').innerHTML= `<b>${file.name}</b>`;    
    };

// Form Handling

function sendData () {    
    
  var username = document.getElementById('getUser').value;
  var sessId = document.getElementById('getSessId').value;      
  var imageFile = document.getElementById('getFile');    
  var data = new FormData(document.getElementById("demo"));
    
  data.append("session_id", sessId);
  data.append("username", username);   
  data.append("image", imageFile.files[0]);  
  
  fetch("http://100092.pythonanywhere.com/favourite/favouriteImage/", {
    method: "POST",    
    body: data    
  })  
  .then(res => res.json())   
  .then(res => console.log("Upload in Progress:", res))  
  .catch(err => console.error("Error:", err));
  return false;
 }

function revealImages(){
     window.getImages = document.getElementById('showImgs');
    fetch("http://100092.pythonanywhere.com/favourite/favouriteImage/")  
    .then(res => res.json())
    .then((res) => {
        res.map((data) => {
            //Adjust username below based on userinfo API
            if(data.username === 'Jude'){
                //getImages.innerHTML = data.image;
                getImages.appendChild(convertBase64ToImage(data.image));
                console.log("Base64 Image Conversion: Success!")
            }   } )   })
    .catch(err => console.error("Error:", err));   
    }

revealImages()

function convertBase64ToImage(base){
        var image = new Image();
        image.src = base; 
        image.loading = "lazy";
        //document.body.appendChild(image);
        return image;
}