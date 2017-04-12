$('document').ready(function(){
    $('#back').click(function(e){
        e.preventDefault();
        $("#actual_file").empty();
        $("#list_section").show();
        $("#user_file").hide();

    });
    $('#choose_coord').click(function(e){
        e.preventDefault();
        $("#file_list").empty();
        $("#mapSection").show();
        $("#list_section").hide();
    });

    $('#nextBtn').click(function(e){
    e.preventDefault();
    var input_coords = $('#result_coords').val();
    var file_list = $('#file_list');
    console.log(input_coords);
    if(input_coords=="")
    {
     $.ajax({
     type:'POST',
     url:'/error',
     data:{'type':3},
     success: function(message){
            console.log(message);
            $("#mapForm").append("<p id=message>"+ message +  "</p>")
        }
     });
    }
    else
    {
    $.ajax({
               type:'POST',
               url:'/download',
               data: {'result_coords' : input_coords},
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
         }
    });

});
