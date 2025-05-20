const blockImages = document.querySelector('.modal-images')
const inputImages = document.getElementsByName("images")[0]
let imageElement = document.createElement("img")
let imageDelete = document.createElement("img")
let divImageDelete = document.createElement("button")

inputImages.addEventListener('change', function(event) {
    const image = event.target.files[0];
    if (image) {
        const reader = new FileReader();
        reader.addEventListener('load', function(e) {
            imageElement.src = e.target.result
            imageElement.className = "preview-img"
            imageDelete.src = "/static/my_post_app/images/delete.png"
            divImageDelete.className = "preview-delete-img"
            divImageDelete.id = "deleteImage"
            divImageDelete.type = "button"
            blockImages.appendChild(imageElement)
            blockImages.appendChild(divImageDelete)
            divImageDelete.appendChild(imageDelete)
        });
        reader.readAsDataURL(image);
    }
});

divImageDelete.addEventListener(
    "click",
    function () {
        console.log("dslfdkfasdf")
        inputImages.value = ""
        imageElement.remove()
        divImageDelete.remove()
    }
)