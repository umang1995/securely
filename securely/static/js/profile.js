$('document').ready(function(){

$.ajax({
type:'POST',
url:'/profile'
})
.done(function(data){
console.log(data)
for( keys in data)
{
console.log('key : ',keys)
console.log('value : ',data[keys])
$("#"+keys).append("<td>"+data[keys]+"</td>")
}
});
});