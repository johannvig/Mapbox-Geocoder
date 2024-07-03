document.getElementById('getAddresses').addEventListener('click', async () => {
    const token = document.getElementById('token').value;
    const latitude = document.getElementById('latitude').value;
    const longitude = document.getElementById('longitude').value;

    if (!token || !latitude || !longitude) {
        alert('Please fill in all fields.');
        return;
    }

    try {
        const coordinates = await getCoordinates(longitude, latitude, token);
        const addressList = document.getElementById('addresses');
        addressList.innerHTML = '';
        const uniqueAddresses = new Set();

        for (const coordinate of coordinates) {
            const [longitude_x, latitude_y] = coordinate.split(',');
            const address = await getAddress(longitude_x, latitude_y, token);
            if (!uniqueAddresses.has(address)) {
                uniqueAddresses.add(address);
                const listItem = document.createElement('li');
                listItem.textContent = address;
                listItem.dataset.latitude = latitude_y;
                listItem.dataset.longitude = longitude_x;
                listItem.addEventListener('click', () => {
                    openMap(listItem.dataset.latitude, listItem.dataset.longitude);
                });
                addressList.appendChild(listItem);
            }
        }
    } catch (error) {
        alert('Ohoh! Something went wrong!');
        console.error(error);
    }
});

async function getCoordinates(longitude, latitude, token) {
    const url = `https://api.mapbox.com/v4/mapbox.mapbox-streets-v8/tilequery/${longitude},${latitude}.json?radius=1000&limit=50&geometry=polygon&access_token=${token}`;
    const response = await fetch(url);
    if (!response.ok) {
        throw new Error('Failed to fetch coordinates');
    }
    const data = await response.json();
    return data.features.map(feature => feature.geometry.coordinates.join(','));
}

async function getAddress(longitude, latitude, token) {
    const url = `https://api.mapbox.com/geocoding/v5/mapbox.places/${longitude},${latitude}.json?access_token=${token}`;
    const response = await fetch(url);
    if (!response.ok) {
        throw new Error('Failed to fetch address');
    }
    const data = await response.json();
    return data.features[0].place_name;
}

function openMap(latitude, longitude) {
    const mapUrl = `https://www.openstreetmap.org/?mlat=${latitude}&mlon=${longitude}#map=18/${latitude}/${longitude}`;
    window.open(mapUrl, '_blank');
}
