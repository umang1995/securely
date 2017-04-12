$('document').ready(function(){
var latitude;
var longitude;
    $('#back').click(function(e){
        e.preventDefault();
        $("#actual_file").empty();
        $("#list_section").show();
        $("#user_file").hide();

    });
if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
            };
            latitude = pos['lat']
            longitude = pos['lng']
console.log('latitude',latitude);

var file_list = $('#file_list');
    $.ajax({
               type:'POST',
               url:'/download',
               data: {'latitude' : latitude, 'longitude':longitude},
               success: function(files){
                    $('#mapSection').hide();
                    $('#div1').show();
                    $('#list_section').show();
                    console.log(files);
                    console.log(typeof(files));
                    file_list = files.data;

                    for(file_details in file_list)
                    {
                            filename = file_list[file_details].file_name
                            console.log(file_list[file_details].file_name);

                            $('#file_list').append("<li class = 'file_items'>" + filename + "</li>")
                    }

                    $("#file_list").on("click", ".file_items", function(event){
                        file_to_download = $(this).text();
                        var pswd = prompt("enter password","******");
                        console.log(pswd);
                        if(pswd!=null)
                         {
                            $.ajax({
                                type:'POST',
                                url:'/get_file',
                                data:{'file_name':file_to_download,'password':pswd},
                                success: function(file){
                                    console.log(file)
                                    $("#list_section").hide()
                                    $("#user_file").show()
                                    $("#actual_file").empty()
                                    console.log(typeof(file.file))
                                    $("#actual_file").append("<p>"+file.file+"</p>")
                                }
                             });
                         }
                    });

                },
               error: function()
               {
                alert('some error');
               }
         });
 });
}

});

