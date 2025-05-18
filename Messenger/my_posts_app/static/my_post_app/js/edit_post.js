$(document).ready(function(){
    console.log($(".editButton"))
    $(".editButton").each(function(){
        $(this).on("click", function(){
            $.ajax({
                url: $(this).val(),
                type: "get",
                success: function(response){
                    console.log(response)
                    $(".popups").html(response)
                },
                error: function(xhr, status, error) {
                    console.log('Error:', status, error);
                }
            })
        })
    })
})