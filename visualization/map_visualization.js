// Initialize the map
var map = L.map('map', {
    center: [0, 0],
    zoom: 2
});

// Add OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Initialize layers
var geologicalLayer = null;
var volcanicLayer = null;
var mangroveLayer = null;

// Function to load and add geological features
function loadGeologicalFeatures() {
    fetch('../data/geological_features.json')
        .then(response => response.json())
        .then(data => {
            geologicalLayer = L.geoJSON(data, {
                style: function(feature) {
                    switch (feature.properties.type) {
                        case 'basalt': return {color: '#8B0000'};
                        case 'olivine': return {color: '#008B8B'};
                        default: return {color: '#808080'};
                    }
                },
                onEachFeature: function(feature, layer) {
                    layer.bindPopup(
                        `<strong>${feature.properties.name}</strong><br>` +
                        `Type: ${feature.properties.type}<br>` +
                        `Description: ${feature.properties.description}<br>` +
                        `Source: ${feature.properties.source}`
                    );
                    layer.on('mouseover', function(e) {
                        e.target.openPopup();
                    });
                    layer.on('mouseout', function(e) {
                        e.target.closePopup();
                    });
                }
            });
        });
}

// Function to load and add volcanic areas
function loadVolcanicAreas() {
    fetch('../maps/volcanic/data/volcanic_areas.geojson')
        .then(response => response.json())
        .then(data => {
            volcanicLayer = L.geoJSON(data, {
                pointToLayer: function(feature, latlng) {
                    return L.circleMarker(latlng, {
                        radius: 8,
                        fillColor: '#FF4500',
                        color: '#000',
                        weight: 1,
                        opacity: 1,
                        fillOpacity: 0.8
                    });
                },
                onEachFeature: function(feature, layer) {
                    layer.bindPopup(
                        `<strong>${feature.properties.name}</strong><br>` +
                        `Type: ${feature.properties.type}<br>` +
                        `Description: ${feature.properties.description}<br>` +
                        `Source: ${feature.properties.source}`
                    );
                    layer.on('mouseover', function(e) {
                        e.target.openPopup();
                    });
                    layer.on('mouseout', function(e) {
                        e.target.closePopup();
                    });
                }
            });
        });
}

// Function to load and add mangrove areas
function loadMangroveAreas() {
    fetch('../maps/mangrove/data/mangrove_areas.geojson')
        .then(response => response.json())
        .then(data => {
            mangroveLayer = L.geoJSON(data, {
                pointToLayer: function(feature, latlng) {
                    return L.circleMarker(latlng, {
                        radius: 6,
                        fillColor: '#008000',
                        color: '#000',
                        weight: 1,
                        opacity: 1,
                        fillOpacity: 0.8
                    });
                },
                onEachFeature: function(feature, layer) {
                    layer.bindPopup(
                        `<strong>${feature.properties.name}</strong><br>` +
                        `Type: ${feature.properties.type}<br>` +
                        `Description: ${feature.properties.description}<br>` +
                        `Source: ${feature.properties.source}`
                    );
                    layer.on('mouseover', function(e) {
                        e.target.openPopup();
                    });
                    layer.on('mouseout', function(e) {
                        e.target.closePopup();
                    });
                }
            });
        });
}

// Function to toggle layers
function toggleLayer(layerName) {
    switch (layerName) {
        case 'geological':
            if (geologicalLayer) {
                if (map.hasLayer(geologicalLayer)) {
                    map.removeLayer(geologicalLayer);
                } else {
                    map.addLayer(geologicalLayer);
                }
            } else {
                loadGeologicalFeatures();
            }
            break;
        case 'volcanic':
            if (volcanicLayer) {
                if (map.hasLayer(volcanicLayer)) {
                    map.removeLayer(volcanicLayer);
                } else {
                    map.addLayer(volcanicLayer);
                }
            } else {
                loadVolcanicAreas();
            }
            break;
        case 'mangrove':
            if (mangroveLayer) {
                if (map.hasLayer(mangroveLayer)) {
                    map.removeLayer(mangroveLayer);
                } else {
                    map.addLayer(mangroveLayer);
                }
            } else {
                loadMangroveAreas();
            }
            break;
    }
}

// Load all layers initially
loadGeologicalFeatures();
loadVolcanicAreas();
loadMangroveAreas();
