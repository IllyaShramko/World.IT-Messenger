const blockImages = document.querySelector('.modal-images')
const inputImages = document.getElementsByName("images")[0]

inputImages.addEventListener('change', function(event) {
    const image = event.target.files[0];
    if (image) {
        const reader = new FileReader();
        reader.addEventListener('load', function(e) {
            let imageElement = document.createElement("img")
            let imageDelete = document.createElement("img")
            let divImageDelete = document.createElement("button")
            let imageDiv = document.createElement('div')
            imageElement.src = e.target.result
            imageElement.className = "preview-img"
            imageDelete.src = "/static/my_post_app/images/delete.png"
            divImageDelete.className = "preview-delete-img"
            divImageDelete.id = "deleteImage"
            divImageDelete.type = "button"
            imageDiv.className = "images-div"
            blockImages.appendChild(imageDiv)
            imageDiv.appendChild(imageElement)
            imageDiv.appendChild(divImageDelete)
            divImageDelete.appendChild(imageDelete)
            divImageDelete.addEventListener(
                "click",
                function () {
                    console.log("dslfdkfasdf")
                    inputImages.value = ""
                    imageDiv.remove()
                    imageElement.remove()
                    divImageDelete.remove()
                }
            )
        });
        reader.readAsDataURL(image);
    }
});
