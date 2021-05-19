let addSong = {
    render: async() => {
        let view =
            `
            <dialog id = "addSongDiaglog">
            <h2 class = "player-subheader">Search</h2>
        <input type="text" placeholder="songs" class="search" id ="searchField">
        <h2 class = "player-subheader" id ="searchText">Genres</h2>
        <ul class="genres" id = "hub">
            
        </ul>
        </dialog>
            `
        return view
    },
    after_render: async() => {
        var fragment = document.getElementById("addSongDiaglog");
        fragment.showModal();
        fragment.addEventListener('click', function(event) {
            var rect = fragment.getBoundingClientRect();
            if (!(rect.top <= event.clientY && event.clientY <= rect.top + rect.height &&
                    rect.left <= event.clientX && event.clientX <= rect.left + rect.width)) {

                window.history.back();
            }
        });
        var field = document.getElementById("searchField");
        field.addEventListener("input", async function(event) {
            var hub = document.getElementById('hub');
            var searchText = document.getElementById('searchText');
            searchText.innerHTML = 'Songs';
            hub.innerHTML = '';
            var data;
            let snapshot = await database.ref('/songs/').once('value');
            data = snapshot.val();
            var songs_queue = [];
            var j = -1;
            var id_queue = localStorage.getItem("playlistSongs");
            for (var i in data) {
                if ((data[i].author.toLowerCase().includes(field.value.toLowerCase()) || data[i].title.toLowerCase().includes(field.value.toLowerCase())) && !id_queue.includes(parseInt(i))) {
                    j++;
                    songs_queue.push({
                        'song': data[i].song,
                        'index': j,
                        'key': i,
                        'title': data[i].title,
                        'author': data[i].author,
                        'img': data[i].img
                    });

                    var li = document.createElement('li');
                    var article = document.createElement('article');
                    var section = document.createElement('section');
                    var img = document.createElement('img');
                    var div = document.createElement('div');
                    var title = document.createElement('h4')
                    var artist = document.createElement('h4')
                    artist.innerHTML = data[i].author;
                    title.innerHTML = data[i].title;
                    div.appendChild(artist);
                    div.appendChild(title);
                    div.className = 'song-song-information';
                    img.className = 'song-song-cover';
                    img.src = data[i].img;
                    section.appendChild(img);
                    section.appendChild(div);
                    section.className = 'song-section';

                    article.appendChild(section);

                    article.className += "song-all"
                    article.className += ' ' + j;
                    li.appendChild(article);
                    hub.appendChild(li);


                } else { var k = 5; }
            }
            var songs = document.querySelectorAll('article');
            for (var i of songs) {
                i.addEventListener('click', async function(e) {
                    var l = parseInt(e.currentTarget.classList[1]);
                    var data;
                    let snapshot = await database.ref('/play_song/').once('value');
                    data = snapshot.val();
                    if (data !== null) {
                        var id = data.length;

                    } else {
                        var id = 1;
                    }

                    firebase.database().ref('play_song/' + id).set({
                        playlist: localStorage.getItem("playlist"),
                        song: songs_queue[l].key


                    });
                    window.history.back();

                });


            }
        });



    }

}
export default addSong;