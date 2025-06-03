$(document).ready(function() {
    $(".editButton").each(function(){
        $(this).on("click", function() {
            $.ajax({
                url: $(this).val(),
                type: "get",
                success: function(response) {
                    console.log(response)
                    $(".popups").html(response)
                }
            })
        })
    })
})