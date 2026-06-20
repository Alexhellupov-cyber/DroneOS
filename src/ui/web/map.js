let followDrone = true;

const map = L.map("map").setView([47.397742, 8.545594], 18);
// Если пользователь начал двигать карту
map.on("dragstart", function () {

    followDrone = false;

    console.log("Follow OFF");

});

// Если пользователь начал менять масштаб
map.on("zoomstart", function () {

    followDrone = false;

    console.log("Follow OFF");

});
L.tileLayer(
    "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    {
        maxZoom: 20,
        attribution: "© OpenStreetMap"
    }
).addTo(map);

let lastLat = 0;
let lastLon = 0;
// =====================================================
// Drone Icon
// =====================================================

const droneIcon = L.icon({

    iconUrl: "drone.svg",

    iconSize: [48, 48],

    iconAnchor: [24, 24]

});


// =====================================================
// Drone Marker
// =====================================================

const marker = L.marker(

    [47.397742, 8.545594],

    {
        icon: droneIcon
    }

).addTo(map);

// =====================================================
// Home
// =====================================================

let homeMarker = null;
let homeSet = false;

// =====================================================
// Flight Path
// =====================================================

const path = [];

const polyline = L.polyline(

    path,

    {
        color: "#00ff00",
        weight: 3
    }

).addTo(map);


// =====================================================
// Update
// =====================================================

function updateDrone(lat, lon){

    if(!homeSet)
        setHome(lat, lon);

    marker.setLatLng([lat, lon]);

    const dist = Math.abs(lat-lastLat)+Math.abs(lon-lastLon);

    if(dist>0.00001){

        path.push([lat,lon]);

        polyline.setLatLngs(path);

        lastLat=lat;
        lastLon=lon;

    }

    if (followDrone) {

    map.panTo(
        [lat, lon],
        {
            animate: true,
            duration: 0.3
        }
    );

}

}

function setHome(lat, lon){

    if(homeSet)
        return;

    homeSet = true;

    homeMarker = L.marker(
        [lat, lon]
    ).addTo(map);

    homeMarker.bindPopup("🏠 Home");
}


function followDroneEnable() {

    followDrone = true;

    map.panTo(
        marker.getLatLng(),
        {
            animate: true,
            duration: 0.3
        }
    );

}