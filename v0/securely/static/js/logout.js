$('document').ready(function(){
$('#logout').click( function(e){
$.cookie('user_id',null,{path:'/'});
});
});
