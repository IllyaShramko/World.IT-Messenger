const blockImages = document.querySelector('.modal-images')
const inputImages = document.getElementsByName("images")[0]

inputImages.addEventListener('change', function(event) {
    const image = event.target.files[0];
    if (image) {
        const reader = new FileReader();
        reader.addEventListener('load', function(e) {
            let imageElement = document.createElement("img")
            imageElement.src = src=e.target.result
            imageElement.className = "preview-img"
            blockImages.appendChild(imageElement)
        });
        reader.readAsDataURL(image);
    }
});