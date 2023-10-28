$(document).ready(function(){

$('#data').hide()
let dataString = $('#data').text();

let loc = JSON.parse(dataString);

//По координатам  Перми
var map = L.map('map').setView([58.00, 56.15], 6);
// По координатам по IP
//var map = L.map('map').setView(loc, 6);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);


});

