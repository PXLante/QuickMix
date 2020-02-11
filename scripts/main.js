var username;
var link;


document.getElementById('submitbtn').addEventListener('click', function() {
    username = document.getElementById("myUserInput").value;
    console.log(username);

    // fetch('http://127.0.0.1:5000/2rwlc0q96u890d0ox3bci6p3p/https://open.spotify.com/playlist/4usZ5YmIumnPzXOcoWUUbC?si=8JA16Qc3QO-Fit-qDsa-Ug')
    // .then((response) => {
    //     return jsonCatalog.json();
    // })
    // .then ((jsonCatalog) => {
    //     console.log(jsonCatalog);
    // });
  });

document.getElementById('loginbtn').addEventListener('click', function() {
    link = document.getElementById("myLinkInput").value;
    console.log(link);

    //God if this works thank you. Request to backend shoutout flask
    fetch('http://127.0.0.1:5000/2rwlc0q96u890d0ox3bci6p3p/' + link)
    .then((response) => {
        return jsonCatalog.json();
    })
    .then ((jsonCatalog) => {
        console.log(jsonCatalog);
    });
});



