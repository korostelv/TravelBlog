$(document).ready(function(){

    $('#data').hide()

    let cityString = $('#user_city').text();
    let cityDict = JSON.parse(cityString);

///////////////////////////////////////////////////////////////////////////////////////

//  Геолокация в JS определяется только при защищенном соединении


  function getCurrentLocation() {
        return new Promise((resolve, reject) => {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    position => resolve([position.coords.latitude, position.coords.longitude]),
                    error => reject(error)
                );
            } else {
                reject("Геолокация не поддерживается этим браузером.");
            }
        });
    }

    let map = L.map('map').setView([58.00, 56.15], 6);

    const basemaps = {
        StreetView: L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{attribution: '&copy; OpenStreetMap'}),
        Topography: L.tileLayer.wms('http://ows.mundialis.de/services/service?',   {layers: 'TOPO-WMS'}),
        Places: L.tileLayer.wms('http://ows.mundialis.de/services/service?', {layers: 'OSM-Overlay-WMS'}),
        };
    basemaps.StreetView.addTo(map);

    L.control.layers(basemaps).addTo(map);
    
    const flagIcon = L.icon({iconUrl: 'https://raw.githubusercontent.com/korostelv/image/main/flag.png',iconSize: [40, 40],});
    for ( let i in cityDict) {
        L.marker([cityDict[i]['lat'], cityDict[i]['long']], {icon: flagIcon}).bindPopup(i).addTo(map);
    }

    function addMarker(coordinates){
        L.marker(coordinates).bindPopup('Вы находитесь здесь.').addTo(map); //метка местоположения по IP
    }
    
    getCurrentLocation()
        .then(coordinates => {
            console.log("Координаты местоположения: " + coordinates);
            addMarker(coordinates); 
        })
        .catch(error => {
            console.error("Ошибка получения координат:", error);
            console.log("Координаты не найдены. Ориентировка по городу Пермь.");
        });

  /////////////////////////////////////////////////////////////////////////////  
    let blockMap = $('#block-map');
    blockMap.hide();

    let showMap = $('.show-map');
    let hideMap = $('.hide-map');


    showMap.click(function(){
        blockMap.show();
        showMap.hide();
    });

    hideMap.click(function(){
        blockMap.hide();
        showMap.show();
    })





});
