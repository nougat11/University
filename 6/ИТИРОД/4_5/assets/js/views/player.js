let player = {
    render: async() => {
        let view =
            `
            <section class="song">
            <img class="song-cover" src="assets/images/wallpaper.jpg" id="scover">
            <div class="song-information">
                <h4 id = "st">Song name</h4>
                <h4 id = "sa">Song Artist</h4>

            </div>
        </section>
        <section class="player-buttons">
            
            <i class="fas fa-play fa-3x" id = "playButton"></i>
            
        </section>
        <section class="func-buttons" id = "funcButton">
            <i class="fas fa-comment fa-3x" id = "lyricsButton"></i>
        </section>
            `
        return view
    },
    after_render: async() => {

        var button = document.getElementById("playButton");
        var player = document.getElementById("audioplayer");
        var cover = document.getElementById("scover");
        cover.src = localStorage.getItem("cover");
        if (player.src === "") {
            player.src = localStorage.getItem("song");
        }
        var author = document.getElementById("sa");
        author.innerHTML = localStorage.getItem("author");
        var title = document.getElementById("st");
        title.innerHTML = localStorage.getItem("title")

        console.log(button.classList);
        if (!player.stopped && player.paused) {
            button.classList.remove('fa-pause');
            button.classList.add('fa-play');
        } else
        if (!player.stopped && !player.paused) {
            button.classList.add('fa-pause');
            button.classList.remove('fa-play');
        }
        console.log(button.classList);
        player.addEventListener('play', function(event) {
            button.classList.remove('fa-play');
            button.classList.add('fa-pause');
        });
        player.addEventListener('pause', function(event) {
            button.classList.remove('fa-pause');
            button.classList.add('fa-play');
        });
        console.log(button.classList);
        button.addEventListener('click', function(event) {
            if (button.classList.contains('fa-pause')) {
                player.pause();
            } else {
                player.play();
            }
        });
        var lyrics = document.getElementById("lyricsButton");
        lyrics.addEventListener('click', function(event) {
            window.location.hash = '#/lyrics';
        });
    }


}
export default player;