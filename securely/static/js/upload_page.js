/**
 * Created by umangt on 2/16/2017.
 */
$('document').ready(function(){
$('#nextBtn').click( function(e){
e.preventDefault();
var file = $('#file_to_upload').val();
var password = $("#password_for_file").val();

if(file=="")
{
     $("#error_message").empty()
     $.ajax({
        type:'POST',
        url:'/error',
        data:{'type':1},
        success: function(message){
            console.log(message);
            $("#error_message").append("<p id=message>"+ message +  "</p>")
        }
     });
}
else if (password=="")
{
     $("#error_message").empty()
     $.ajax({
        type:'POST',
        url:'/error',
        data:{'type':2},
        success: function(message){
            console.log(message);
            $("#error_message").append("<p id=message>"+ message +  "</p>")
        }
     });

}
else
{$('#div3').hide();
$('#map').show();
$('#div1').show();
$('#mapSection').show()
}
});
});
