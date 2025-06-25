$(document).ready(function(){
    $("#editButton").on("click", function(){
        $.ajax({
            url: $(this).val(),
            type: "get",
            success: function(response){
                console.log(response)
                $(".popups").html(response)
                $("#closepopup1").on("click", function(){
                    $("#createGroupForm1").remove()
                    $("#blurform1").remove()
                })
            },
            error: function(){
                console.log("error")
            }

        })
    })
})
