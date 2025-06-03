const input = document.getElementById('image-input');
const grid = document.getElementById('image-preview-grid');
const albumIdInput = document.getElementById('album-id');

input.addEventListener('change', () => {
    const files = Array.from(input.files);
    const formData = new FormData();
    files.forEach(file => {
        formData.append('images', file);
    });
    formData.append('album_id', albumIdInput.value);
    $.ajax({
        url: '/settings/upload/',
        type: 'POST',
        data: formData,
        processData: false, 
        contentType: false, 
        success: function(response) {
            console.log('Успешно загружено', response);
            files.forEach(file => {
                const reader = new FileReader();
                reader.onload = e => {
                const card = document.createElement('div');
                card.className = 'image-card';
                card.innerHTML = `<img src="${e.target.result}" alt="preview">`;
                
                grid.insertBefore(card, grid.lastElementChild);
                };
                reader.readAsDataURL(file);
            });
            
        },
        error: function(xhr, status, error) {
        console.error('Ошибка при загрузке:', error);
        }
    });
});