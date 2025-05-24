const blockImages = document.querySelector('.modal-images');
const inputImages = document.getElementsByName("images")[0];

inputImages.addEventListener('change', function(event) {
    const files = event.target.files;

    for (let i = 0; i < files.length; i++) {
        const image = files[i];
        const reader = new FileReader();

        reader.addEventListener('load', function(e) {
            const imageElement = document.createElement("img");
            const imageDelete = document.createElement("img");
            const divImageDelete = document.createElement("button");
            const imageDiv = document.createElement('div');

            imageElement.src = e.target.result;
            imageElement.className = "preview-img";

            imageDelete.src = "/static/my_post_app/images/delete.png";
            divImageDelete.className = "preview-delete-img";
            divImageDelete.id = "deleteImage";
            divImageDelete.type = "button";

            imageDiv.className = "images-div";

            blockImages.appendChild(imageDiv);
            imageDiv.appendChild(imageElement);
            imageDiv.appendChild(divImageDelete);
            divImageDelete.appendChild(imageDelete);

            divImageDelete.addEventListener("click", function () {
                imageDiv.remove();
            });
        });

        reader.readAsDataURL(image);
    }
});
