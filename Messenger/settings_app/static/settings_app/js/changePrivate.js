$(document).ready(function() {
    $(".privateButton").each(function(){
        $(this).on("click", function() {
            $.ajax({
                url: $(this).val(),
                type: "get",
                success: function(response) {
                    console.log(response)
                    $("#private").text(response.text)
                }
            })
        })
    })
})