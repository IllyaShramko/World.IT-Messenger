$(document).ready(function(){
    console.log($(".editButton"))
    $(".editButton").each(function(){
        $(this).on("click", function(){
            $.ajax({
                url: $(this).val(),
                type: "get",
                success: function(response){
                    $(".popups").html(response);

                    const blockImages = document.querySelector('.modal-images');
                    const inputImages = document.getElementById("images");
                    let selectedFiles = [];

                    inputImages.addEventListener('change', function (event) {
                        const files = Array.from(event.target.files);

                        files.forEach(file => {
                            if (selectedFiles.some(f => f.name === file.name && f.size === file.size)) return;

                            selectedFiles.push(file);

                            const reader = new FileReader();
                            reader.onload = function (e) {
                                const imageDiv = document.createElement("div");
                                imageDiv.className = "images-div";

                                const imageElement = document.createElement("img");
                                imageElement.className = "preview-img";
                                imageElement.src = e.target.result;

                                const deleteButton = document.createElement("button");
                                deleteButton.type = "button";
                                deleteButton.className = "preview-delete-img";

                                const deleteIcon = document.createElement("img");
                                deleteIcon.src = "/static/my_post_app/images/delete.png";
                                deleteButton.appendChild(deleteIcon);

                                deleteButton.addEventListener("click", function () {
                                    imageDiv.remove();
                                    selectedFiles = selectedFiles.filter(f => !(f.name === file.name && f.size === file.size));

                                    const dt = new DataTransfer();
                                    selectedFiles.forEach(f => dt.items.add(f));
                                    inputImages.files = dt.files;
                                });

                                imageDiv.appendChild(imageElement);
                                imageDiv.appendChild(deleteButton);
                                blockImages.appendChild(imageDiv);
                            };
                            reader.readAsDataURL(file);
                        });

                    });
                    document.querySelectorAll(".modal-images .preview-delete-img").forEach(button => {
                        button.addEventListener("click", function () {
                            const imageDiv = this.closest(".images-div");
                            const imageId = imageDiv.dataset.imageId; 
                            imageDiv.remove();

                            let deleted = document.getElementById("deletedImagesInput");
                            if (!deleted) {
                                deleted = document.createElement("input");
                                deleted.type = "hidden";
                                deleted.name = "deleted_images";
                                deleted.id = "deletedImagesInput";
                                document.querySelector("form").appendChild(deleted);
                            }

                            const deletedIds = deleted.value ? deleted.value.split(",") : [];
                            deletedIds.push(imageId);
                            deleted.value = deletedIds.join(",");
                        });
                    });
                    const addTagBtn = document.getElementById('addTagBtn');
                    const tagsContainer = document.getElementById('tagsContainer');
                    const hiddenInput = document.getElementById('tags');
                    let tags = [];
                    addTagBtn.addEventListener('click', () => {
                        if (document.getElementById('tagInput')) return;
                        const input = document.createElement('input');
                        input.type = 'text';
                        input.id = 'tagInput';
                        input.className = "input-tags-input"
                        input.placeholder = 'Введіть тег';
                        input.style.margin = '4px';
                        input.style.padding = '6px';
                        input.style.borderRadius = '8px';
                        input.style.border = '1px solid #ccc';
                        tagsContainer.appendChild(input);
                        input.focus();
                        input.addEventListener('keydown', (e) => {
                            if (e.key === 'Enter') {
                                e.preventDefault();
                                const tagValue = input.value.trim();
                                if (tagValue && !tags.includes(tagValue)) {
                                    tags.push(tagValue);
                                    renderTag(tagValue);
                                    updateHiddenInput();
                                }
                                input.remove();
                            } else if (e.key === 'Escape') {
                                input.remove();
                            }
                        });
                    });
                    function renderTag(tag) {
                        const span = document.createElement('span');
                        span.className = 'tag';
                        span.textContent = `#${tag}`;
                        tagsContainer.appendChild(span);
                    }
                    function updateHiddenInput() {
                        hiddenInput.value = tags.join(',');
                    }
                },
                error: function(xhr, status, error) {
                    console.log('Error:', status, error);
                }
            })
        })
    })
})