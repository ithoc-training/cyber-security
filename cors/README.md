# Cross-Origin Resource Sharing (CORS)

## Ursprung
CORS tritt auf, wenn ein Browser auf ein Backend zugreift, ohne dass die beiden auf demselben Host laufen.

## Problem
Um auf ein REST-Backend von einem JavaScript-Client im Browser zuzugreifen, verwenden wir typischerweise 
die ```fetch``` API. Diese API bietet eine leistungsfähige und flexible Schnittstelle für das Senden von 
HTTP-Requests.

```javascript
fetch('http://127.0.0.1:5003/sensitive')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
    });
```

## Lösung
Beachte, dass du je nach Sicherheitsrichtlinien des Servers (CORS - Cross-Origin Resource Sharing) möglicherweise 
nicht in der Lage bist, direkt von localhost oder einer anderen Domain aus auf das Backend zuzugreifen. Der Server muss 
entsprechende ```Access-Control-Allow-Origin-Header``` setzen, um solche Requests zu erlauben. 

## Anmerkung
Wenn du in einer Entwicklungsphase bist und keine Kontrolle über Backend-CORS-Einstellungen haben, kannst du Tools wie 
Proxy-Server verwenden, um CORS-Probleme zu umgehen. Das ist jedoch keine empfohlene Praxis für Produktionsumgebungen 
ist.
