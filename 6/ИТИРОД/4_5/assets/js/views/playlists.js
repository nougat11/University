let playlists = {
    render: async() => {
        let view =
            `
            
        <div class="subheader">
            <h1 class="player-header">HELLO</h1>
            <button class = "profile-button" id = "profileButton">Menu</button>
        </div>
        <h2 class = "player-subheader">Playlists</h2>
        <ul id = "playlists-list">
        </ul>
            `
        return view
    },
    after_render: async() => {
        const dbRef = database.ref();
        var data;
        let snapshot = await database.ref('/playlists/').once('value');
        data = snapshot.val();
        var hub = document.getElementById("playlists-list");
        if (data !== undefined) {
            for (var i in data) {

                var tag = document.createElement("li");

                var article = document.createElement("article")
                article.className += "playlist-all"
                article.className += " playlist" + i;
                var div1 = document.createElement("div");
                div1.className = "playlist-info"
                var img = document.createElement("img");
                img.className = "playlis-cover";
                img.src = data[i].img;
                var div2 = document.createElement("div");
                div2.className = "playlist-text";
                var h3 = document.createElement("h3");
                h3.innerHTML = data[i].title;
                h3.className = "playlist-title";
                var h4 = document.createElement("h4");
                h4.className = "playlist-description";
                h4.innerHTML = data[i].desription;
                div2.appendChild(h3);
                div2.appendChild(h4);
                div1.appendChild(img);
                div1.appendChild(div2);
                article.appendChild(div1);
                tag.appendChild(article);
                hub.appendChild(tag);

            }
        }
        var profileButton = document.getElementById('profileButton');
        profileButton.addEventListener('click', function(event) {
            window.location.hash = '/profile';
        });
        var playlist = document.querySelectorAll('article');
        for (i of playlist) {
            i.addEventListener('click', async function(e) {
                var l = e.currentTarget.classList[1].slice(8);
                window.location.hash = '#/playlist/' + l;
                localStorage.setItem('currentPlaylistId', l);

            });
        }


    }

}
export default playlists;