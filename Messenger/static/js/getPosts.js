$(document).ready(function (){
    let idsPosts = [];
    let stop = false;
    if (!stop) {
        $.ajax({
            url: '',
            method: 'GET',
            success: function (response) {
                console.log(response)
            }
        })
    }
})