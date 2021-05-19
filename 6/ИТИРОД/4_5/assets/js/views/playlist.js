let playlist = {
    render: async() => {
        let view =
            `
            <section class="playlist-playlist">
            <img class="playlist-playlist-cover"  id = "cover">
            <div class="playlist-playlist-information">
                <h2 class = "playlist-playlist-subheader">PLAYLIST</h2>
                <h1 class = "playlist-playlist-header" id = "title">PLAYLIST NAME</h1>
                <h2 class = "playlist-playlist-subheader" id = "description">228 songs</h2>

            </div>
            

        </section>
        <ul class="genres" id = "hub">
            </ul>
        <button id ="addSong">Add Song</button>
        <button id = "deletePlaylist">Delete Playlist</button>
        <button id = "editPlaylist">Edit Playlist</button>
        <button id = "dublicatePlaylist" style = "display:none;">Dublicate Playlist</button>
            `
        return view
    },
    after_render: async() => {
        var playlist_id = window.location.href;
        var deletePlaylist = document.getElementById("deletePlaylist");
        var editPlaylist = document.getElementById("editPlaylist");
        var dublicatePlaylist = document.getElementById("dublicatePlaylist");
        var id = document.getElementById("addSong");
        // var fragment = document.getElementById("addSongDiaglog");
        id.addEventListener('click', function(event) {
            window.location.hash = '#/addSong';
        });
        var j = playlist_id.length - 1;
        while (playlist_id[j] !== '/') {
            j--;

        }

        playlist_id = window.location.href.slice(j + 1);
        const dbRef = database.ref();
        var data;
        let snapshot = await database.ref('/playlists/' + playlist_id).once('value');

        data = snapshot.val();
        if (firebase.auth().currentUser.email !== data.creator) {
            id.style.cssText = "display:none;";
            deletePlaylist.style.cssText = "display:none;";
            editPlaylist.style.cssText = "display:none;"
            dublicatePlaylist.style.cssText = "";
        }

        var titl = document.getElementById("title");
        var img = document.getElementById("cover");
        var description = document.getElementById("description");
        description.innerHTML = data.desription;
        titl.innerHTML = data.title;
        cover.src = data.img;
        var data;
        snapshot = await database.ref('/play_song/').once('value');
        data = snapshot.val();
        var songs_queue = [];
        var id_queue = [];
        var j = -1;
        for (var i in data) {
            if (data[i].playlist == playlist_id) {
                var subdata;
                let snapshot2 = await database.ref('/songs/' + data[i].song + '/').once('value');
                subdata = snapshot2.val();
                j++;
                songs_queue.push({
                    'song': subdata.song,
                    'index': j,
                    'key': data[i].song,
                    'title': subdata.title,
                    'author': subdata.author,
                    'img': subdata.img,
                    'lyrics': subdata.lyrics
                });
                id_queue.push(data[i].song);

                var li = document.createElement('li');
                var article = document.createElement('article');
                var section = document.createElement('section');
                var img = document.createElement('img');
                var div = document.createElement('div');
                var title = document.createElement('h4')
                var artist = document.createElement('h4')
                artist.innerHTML = subdata.author;
                title.innerHTML = subdata.title;
                div.appendChild(artist);
                div.appendChild(title);
                div.className = 'song-song-information';
                img.className = 'song-song-cover';
                img.src = subdata.img;
                section.appendChild(img);
                section.appendChild(div);
                section.className = 'song-section';

                article.appendChild(section);

                article.className += "song-all"
                article.className += ' ' + j;
                li.appendChild(article);
                hub.appendChild(li);
            }


        }

        var songs = document.querySelectorAll('article');
        for (var i of songs) {
            i.addEventListener('click', async function(e) {
                var l = parseInt(e.currentTarget.classList[1]);
                var ll = document.getElementById("audioplayer");
                ll.src = songs_queue[l].song;
                ll.play();
                ll.innerHTML = "asd";
                var cover = document.getElementById("scover");
                cover.src = songs_queue[l].img;
                var title = document.getElementById("st");
                title.innerHTML = songs_queue[l].title;
                var author = document.getElementById("sa");
                author.innerHTML = songs_queue[l].author;
                localStorage.setItem("author", songs_queue[l].author);
                localStorage.setItem("title", songs_queue[l].title);
                localStorage.setItem("song", songs_queue[l].song);
                localStorage.setItem("cover", songs_queue[l].img);
                localStorage.setItem("lyrics", songs_queue[l].lyrics);

            });
        }
        var data;
        snapshot = await database.ref('/playlists/' + playlist_id).once('value');
        data = snapshot.val();
        if (firebase.auth().currentUser.email === data.creator) {

            var songs = document.querySelectorAll('article');


            for (var i of songs) {
                i.addEventListener('dblclick', async function(e) {
                    var data1;
                    var snapshot3 = await database.ref('/play_song/').once('value');
                    data1 = snapshot3.val();
                    var l = parseInt(e.target.classList[1]);
                    for (var j in data1) {
                        console.log(playlist_id);
                        if (data1[j].playlist.toString() === playlist_id && data1[j].song.toString() === songs_queue[l].key.toString()) {
                            var node = database.ref('play_song/' + j);
                            node.remove().then(function() { document.location.reload() }).catch(function(error) { console.log("error") });

                        }
                    }








                });

            }
        }

        localStorage.setItem("playlistSongs", id_queue);
        localStorage.setItem("playlist", playlist_id);

        deletePlaylist.addEventListener('click', async function(event) {
            var data;
            var snapshot = await database.ref('/play_song/').once('value');
            data = snapshot.val();
            for (var i in data) {
                if (data[i].playlist.toString() === playlist_id.toString()) {
                    var node = database.ref('play_song/' + i);
                    node.remove().then(function() { document.location.reload() }).catch(function(error) { console.log("error") });
                }
            }
            var node = database.ref('playlists/' + playlist_id);
            node.remove().then(function() { document.location.reload() }).catch(function(error) { console.log("error") });
            window.location.hash = '#';

        });
        editPlaylist.addEventListener('click', async function(event) {
            localStorage.setItem("id_edit", playlist_id);
            window.location.hash = "#/editPlaylist";

        });
        dublicatePlaylist.addEventListener('click', async function(event) {
            var data;
            let snapshot = await database.ref('/playlists/').once('value');
            data = snapshot.val();
            var id = 1;
            for (var key in data) {
                id++;
            }

            snapshot = await database.ref('/playlists/' + playlist_id).once('value');

            data = snapshot.val();
            firebase.database().ref('playlists/' + id).set({
                title: data.title,
                desription: data.desription,
                img: data.img,
                creator: firebase.auth().currentUser.email

            });
            snapshot = await database.ref('/play_song/').once('value');
            data = snapshot.val();
            var data2;
            let snapshot2 = await database.ref('/play_song/').once('value');
            data2 = snapshot.val();
            var new_id;
            if (data2 !== null) {
                new_id = data.length;

            } else {
                new_id = 1;
            }
            for (var i in data) {
                if (data[i].playlist == playlist_id) {
                    firebase.database().ref('play_song/' + new_id).set({
                        playlist: id,
                        song: data[i].song


                    });
                    new_id++;

                }
            }
            window.location.hash = '#';

        });

    }
}
export default playlist;