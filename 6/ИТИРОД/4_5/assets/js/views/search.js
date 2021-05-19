let search = {
    render: async() => {
        let view =
            `
            <h2 class = "player-subheader">Search</h2>
        <input type="text" placeholder="songs" class="search" id ="searchField">
        <h2 class = "player-subheader" id ="searchText">Genres</h2>
        <ul class="genres" id = "hub">
            <li class = "genre rap">Rap</li>
            <li class = "genre pop">Pop</li>
            <li class = "genre rock">Rock</li>
        </ul>
            `
        return view
    },
    after_render: async() => {
        var genres = document.querySelectorAll('li');
        for (var i of genres) {
            i.addEventListener('click', async function(e) {
                var l = e.currentTarget.classList[1];
                window.location.hash = '#/genre/' + l;


            });
        }
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
            for (var i in data) {
                if (data[i].author.toLowerCase().includes(field.value.toLowerCase()) || data[i].title.toLowerCase().includes(field.value.toLowerCase())) {
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
        });



    }

}
export default search;