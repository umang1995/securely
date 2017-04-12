var map;
var marker;
function initMap() {
if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function(position) {
            var result = [];
            var pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
            };
            var latitude = pos['lat']
            var longitude = pos['lng']
            var map = new google.maps.Map(document.getElementById('map'), {
            center: {lat:latitude,lng:longitude},
            zoom: 6
            }
            );
            var marker = new google.maps.Marker({
            position: {lat:latitude,lng:longitude},
            map: map,
            draggable: true
            });
            marker.setPosition(pos);
            map.setCenter(pos);
            google.maps.event.addListener(marker, "click", function (event) {
            latitude = event.latLng.lat();
            longitude = event.latLng.lng();
                   var infowindow = new google.maps.InfoWindow();

            google.maps.event.addListener(marker,'click',function(e){
                infowindow.open(map,marker);
                infowindow.setContent('<strong>Position: <br>Latitude: ' +latitude+ '<br> longitude : ' + longitude + '</strong>')
            })
            google.maps.event.addListener(infowindow,'places_changed',function(e){
                infowindow.close(map,marker);
            })
            var elemLatitude = document.getElementById('latitude')
            var elemLongitude = document.getElementById('longitude')
            var valLatitude = elemLatitude.value
            var valLongitude = elemLongitude.value
            var latlondict = {}
            latlondict['latitude'] = latitude
            latlondict['longitude'] = longitude
            result.push(latlondict)
            json_result = JSON.stringify(result)
            var result_dom = document.getElementById('result_coords')
            result_dom.value = json_result

            if(elemLatitude.value=="")
            {
            valLatitude  = valLatitude + latitude
            elemLatitude.value = valLatitude
            valLongitude = valLongitude + longitude
            elemLongitude.value = valLongitude
            }
            else
            {
            valLatitude  = valLatitude + "," + latitude
            elemLatitude.value = valLatitude
            valLongitude = valLongitude + "," + longitude
            elemLongitude.value = valLongitude
            }


            console.log( latitude + ', ' + longitude );
            });
            });
}
else {
// Browser doesn't support Geolocation
document.getElementById('map').value('maps not supported');
}


}
