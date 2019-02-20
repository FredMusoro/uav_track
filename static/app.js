
function makeMap() {
    var map = L.map('mapid').setView(points[0], 13);

    L.tileLayer(
        'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        {
            attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
        }).addTo(map);
    return(map)
}

$(function() {
    var map = makeMap();
    var routeGroup = L.featureGroup().addTo(map);

    map.on('pm:create', function(e) {
        routeGroup.addLayer(e.layer);
    });

    // var polyline = L.polyline(points, {color: 'red'}).addTo(map);
    // map.fitBounds(polyline.getBounds());
    // routeGroup.addLayer(polyline)

    map.pm.addControls({
        position: 'topleft',
        drawCircle: false,
    });

    $('#delete').click(function(e) {
        routeGroup.clearLayers();
    });

    $('#export').click(function(e) {
        var start_data = startPoints.toGeoJSON();
        var start_feature = start_data['features'][0];
        start_feature['properties'].name = 'start_point';

        var land_data = landPoints.toGeoJSON();
        var land_feature = land_data['features'][0];
        land_feature['properties'].name = 'land_point';

        var height_value = $('#height').val();

        var data = routeGroup.toGeoJSON();
        data.start_point = start_feature['geometry']['coordinates']
        data.land_point = land_feature['geometry']['coordinates']
        data.height = height_value;

        var xhr = new XMLHttpRequest();

        var url = 'http://127.0.0.1:5000/#';
        var requestData = JSON.stringify((data));
        console.log(requestData);

        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.send(requestData);
    });

    var startPoints = L.featureGroup().addTo(map);

    $('#start_point').click(function addStartPoint() {
        var startPointValue = $('#start_point :selected').val();
        console.log(startPointValue)
        // var startPointValue = $('#start_point').options[$('#start_point').selectedIndex].value;
        var position = JSON.parse(startPointValue);

        startPoints.clearLayers();
        var startPoint = L.marker([position[0], position[1]], {alt: 'startPoint'}).addTo(map);
        startPoints.addLayer(startPoint);
    });

    var landPoints = L.featureGroup().addTo(map);

    $('#land_point').click(function addLandPoint() {
        var landPointValue = $('#land_point :selected').val();
        var position = JSON.parse(landPointValue);

        landPoints.clearLayers();
        var landPoint = L.marker([position[0], position[1]], {alt: 'landPoint'}).addTo(map);
        landPoints.addLayer(landPoint);
    });
});
