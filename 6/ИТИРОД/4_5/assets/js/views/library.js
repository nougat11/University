let library = {
    render: async() => {
        let view =
            `
            <h2 class = "player-subheader" id = "title">Your library</h2>
            <ul id="hub" class = "songs-list">
            </ul>
            `
        return view
    },
    after_render: async() => {
        var songs_queue = [];
        var id = window.location.href;
        var j = id.length - 1;

        id = window.location.href.slice(j + 1);
        const dbRef = database.ref();
        var data;
        let snapshot = await database.ref('/songs/').once('value');
        data = snapshot.val();
        var title = document.getElementById("title");
        title.innerHTML = id;
        var j = -1;
        for (var i in data) {
            if (data[i].creator === firebase.auth().currentUser.email) {
                j++;
                songs_queue.push({
                    'song': data[i].song,
                    'index': j,
                    'key': i,
                    'title': data[i].title,
                    'author': data[i].author,
                    'img': data[i].img,
                    'lyrics': data[i].lyrics
                });
                var hub = document.getElementById('hub');
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


                localStorage.setItem("id_edit", songs_queue[l].key);
                window.location.hash = "#/editSong";







            });
        }
    }

}
export default library;