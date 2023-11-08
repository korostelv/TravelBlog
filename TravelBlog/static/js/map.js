$(document).ready(function(){

    $('#data').hide()
    let dataString = $('#location').text();
    let loc = JSON.parse(dataString);

    let cityString = $('#user_city').text();
    let cityDict = JSON.parse(cityString);

    console.log($('.title h3').text())


    // let map = L.map('map').setView([58.00, 56.15], 6); //По координатам  Перми
    let map = L.map('map').setView(loc, 6); // По координатам по IP



    const basemaps = {
        StreetView: L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{attribution: '&copy; OpenStreetMap'}),
        Topography: L.tileLayer.wms('http://ows.mundialis.de/services/service?',   {layers: 'TOPO-WMS'}),
        Places: L.tileLayer.wms('http://ows.mundialis.de/services/service?', {layers: 'OSM-Overlay-WMS'}),
    };
    basemaps.StreetView.addTo(map);
    L.control.layers(basemaps).addTo(map);


  

    const flagIcon = L.icon({
        iconUrl: 'https://raw.githubusercontent.com/korostelv/image/main/flag.png',
        iconSize: [40, 40],
    });


    // L.marker([58.00, 56.15]).bindPopup('Вы находитесь здесь.').addTo(map);  //Метка местоположения Перми
    L.marker(loc).bindPopup('Вы находитесь здесь.').addTo(map); //метка местоположения по IP


    for ( let i in cityDict) {
        L.marker([cityDict[i]['lat'], cityDict[i]['long']], {icon: flagIcon}).bindPopup(i).addTo(map);
    }

    
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

