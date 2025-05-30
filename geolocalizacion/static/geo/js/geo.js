navigator.geolocation.getCurrentPosition(
    function(position) {
        var lat= position.coords.latitude;
        var lon= position.coords.longitude;

        fetch('/api/localizacion/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer TU_TOKEN',
            },
            body: JSON.stringify({
                latitud: lat,
                longitud: lon
            })
        });
    });