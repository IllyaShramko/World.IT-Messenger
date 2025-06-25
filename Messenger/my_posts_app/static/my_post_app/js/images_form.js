const blockImages = document.querySelector('.modal-images');
const inputImages = document.getElementsByName("images")[0];

let selectedFiles = [];

inputImages.addEventListener('change', function (event) {
    const files = Array.from(event.target.files);

    files.forEach((file) => {
        if (selectedFiles.some(f => f.name === file.name && f.size === file.size)) {
            return; 
        }

        selectedFiles.push(file);

        const reader = new FileReader();

        reader.onload = function (e) {
            const imageElement = document.createElement("img");
            const imageDelete = document.createElement("img");
            const divImageDelete = document.createElement("button");
            const imageDiv = document.createElement('div');

            imageElement.src = e.target.result;
            imageElement.className = "preview-img";

            imageDelete.src = "/static/my_post_app/images/delete.png";
            divImageDelete.className = "preview-delete-img";
            divImageDelete.type = "button";

            imageDiv.className = "images-div";
            imageDiv.dataset.filename = file.name;

            blockImages.appendChild(imageDiv);
            imageDiv.appendChild(imageElement);
            imageDiv.appendChild(divImageDelete);
            divImageDelete.appendChild(imageDelete);

            divImageDelete.addEventListener("click", function () {
                imageDiv.remove();

                selectedFiles = selectedFiles.filter(f => !(f.name === file.name && f.size === file.size));

                const dataTransfer = new DataTransfer();
                selectedFiles.forEach(f => dataTransfer.items.add(f));
                inputImages.files = dataTransfer.files;
            });
        };

        reader.readAsDataURL(file);
    });

});

const addTagBtn = document.getElementById('addTagBtn');
const tagsContainer = document.getElementById('tagsContainer');
const hiddenInput = document.getElementById('tags');
const inputText = document.getElementById('text')

let tags = [];
addTagBtn.addEventListener('click', () => {
    if (document.getElementById('tagInput')) return;

    const wrapper = document.createElement('div');
    wrapper.className = 'tag-input-wrapper';

    const hash = document.createElement('span');
    hash.textContent = '#';

    const input = document.createElement('input');
    input.type = 'text';
    input.id = 'tagInput';

    const confirmBtn = document.createElement('button');
    const icon = document.createElement('img');
    icon.src = '/static/my_post_app/images/checkmark.png'; 
    confirmBtn.className = "confirm"
    confirmBtn.appendChild(icon);

    confirmBtn.addEventListener('click', () => {
        const tagValue = input.value.trim();
        if (tagValue && !tags.includes(tagValue)) {
            tags.push(tagValue);
            renderTag(tagValue);
            updateHiddenInput();
        }
        wrapper.remove();
        confirmBtn.remove();
        tagsContainer.appendChild(addTagBtn);
    });

    input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            confirmBtn.click();
            tagsContainer.appendChild(addTagBtn);
            
        } else if (e.key === 'Escape') {
            wrapper.remove();
            confirmBtn.remove();
            tagsContainer.appendChild(addTagBtn);
        }
    });

    addTagBtn.remove();
    wrapper.appendChild(hash);
    wrapper.appendChild(input);
    tagsContainer.appendChild(wrapper);
    tagsContainer.appendChild(confirmBtn);
    input.focus();
});

function renderTag(tag) {
    const span = document.createElement('span');
    span.className = 'tag';
    span.textContent = `#${tag}`;
    span.addEventListener('click', () => {
        
        let text = inputText.value
        let splitedText = text.split('#')[0];
        console.log(splitedText)
        inputText.value = `${splitedText}\n#${tag}`
    });
    tagsContainer.appendChild(span);
}

function updateHiddenInput() {
    hiddenInput.value = tags.join(',');
}

const linksContainer = document.getElementById("linksdiv")
const linksInput = document.getElementById("links")
const addLinkBtn = document.getElementById("addLinkBtn")
let links = []

function renderLinks(link) {
    const span = document.createElement('span');
    span.className = 'link';
    span.textContent = link;
    linksContainer.appendChild(span);
}


addLinkBtn.addEventListener('click', () => {
    if (document.getElementById('LinkInput')) return;

    const wrapper = document.createElement('div');
    wrapper.className = 'link-input-wrapper';


    const input = document.createElement('input');
    input.type = 'url';
    input.id = 'LinkInput';

    const confirmBtn = document.createElement('button');
    const icon = document.createElement('img');
    icon.src = '/static/my_post_app/images/checkmark.png'; 
    confirmBtn.className = "confirm"
    confirmBtn.appendChild(icon);

    confirmBtn.addEventListener('click', () => {
        const linkValue = input.value.trim();
        if (linkValue && !links.includes(linkValue)) {
            links.push(linkValue);
            renderLinks(linkValue);
            linksInput.value = links.join(",")
        }
        wrapper.remove();
        confirmBtn.remove();
    });

        input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            confirmBtn.click();
        } else if (e.key === 'Escape') {
            wrapper.remove();
            confirmBtn.remove();
        }
        });

    wrapper.appendChild(input);
    wrapper.appendChild(confirmBtn);
    linksContainer.appendChild(wrapper);
    input.focus();
});