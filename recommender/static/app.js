window.onload = function() {
    let elements = document.querySelectorAll(".article-title");

    elements.forEach(function(elem) {
        elem.addEventListener('auxclick', function() {
            // if (e.button === 1) { 
            elem.innerHTML = "testing2"; //Here you will need to use the param.
            sendLinkData(elem)
            // }
        });
        elem.addEventListener('click', function() {
            elem.innerHTML = "testing"; //Here you will need to use the param.
            sendLinkData(elem)
        });        
    });
}


function sendLinkData(element) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/redirect", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        id: element.dataset.id,
        link: element.href
    }));
}