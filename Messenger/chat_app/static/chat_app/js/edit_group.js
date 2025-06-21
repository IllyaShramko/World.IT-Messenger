$(document).ready(function(){
    $("#editButton").on("click", function(){
        $.ajax({
            url: $(this).val(),
            type: "get",
            success: function(response){
                console.log(response)
                $(".popups").html(response)
            },
            error: function(){
                console.log("error")
            }

        })
    })
})
