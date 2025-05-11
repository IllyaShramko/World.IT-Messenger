
document.addEventListener('DOMContentLoaded', function() {
        const inputs = document.querySelectorAll('.input-number');
        
        inputs.forEach((input, index) => {
            input.addEventListener('input', function(e) {
                if (this.value.length === 1) {
                    if (index < inputs.length - 1) {
                        inputs[index + 1].focus();
                    }
                }
            });
            
            input.addEventListener('keydown', function(e) {
                if (e.key === 'Backspace' && this.value === '') {
                    if (index > 0) {
                        inputs[index - 1].focus();
                    }
                }
            });
        });
    });