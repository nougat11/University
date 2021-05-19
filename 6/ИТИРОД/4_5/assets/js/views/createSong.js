let createSong = {
    render: async() => {
        let view =
            `
            <form class="form-player" action="javascript:void(0);">
            <fieldset class = "form-fieldset">
                <legend class="form-legend">CREATE SONG</legend>
                <input type="text" placeholder="Title" class = "form-input" id = "title">
                <input class = "form-input" type="text" placeholder="Artist" id = "desription">

                <input class = "form-input cover1" name="file" id="file" type="file" accept="image/*">
                <div class="cover"><label for="file">Choose a cover</label></div>
                <input class = "form-input cover1" name="file1" id="file1" type="file" accept="audio/*">
                <div class="cover"><label for="file1">Choose a song</label></div>
                <select name="select" id="select">
                        <option value="rap">Rap</option>
                        <option value="pop">Pop</option>
                        <option value="rock">Rock</option>
                    </select>
                <textarea class = "form-input lyrics-input" id = "lyricsinput" placeholder="lyrics"></textarea>
                <button class = "form-button" id="createButton">CREATE</button>
            </fieldset>
        </form>
            `
        return view
    },
    after_render: async() => {
        var data;
        let snapshot = await database.ref('/songs/').once('value');
        data = snapshot.val();
        var id = 1;
        for (var key in data) {
            id++;
        }

        var picture;
        var song;


        var button = document.getElementById('createButton');

        button.addEventListener('click', async function(e) {
            var title1 = document.getElementById('title').value;
            var desription1 = document.getElementById('desription').value;
            var select1 = document.getElementById('select').value;
            var lyrics = document.getElementById('lyricsinput').value;
            firebase.database().ref('songs/' + id).set({
                title: title1,
                author: desription1,
                img: picture,
                song: song,
                genre: select1,
                creator: firebase.auth().currentUser.email,
                lyrics: lyrics

            });
            window.location.hash = '#';

        });
        var file = document.getElementById('file')
        file.addEventListener('change', async function(e) {
            var file = e.target.files[0];
            var storageRef = firebase.storage().ref('cover' + id + '.png');
            picture = id;
            await storageRef.put(file);
            const snapshot = firebase.storage().ref();
            const img = snapshot.child("cover" + id + ".png");
            const url = await img.getDownloadURL();
            picture = url;
        });
        var file1 = document.getElementById('file1')
        file1.addEventListener('change', async function(e) {
            var file = e.target.files[0];
            var storageRef = firebase.storage().ref('song' + id + '.mp3');
            song = id;
            await storageRef.put(file);
            const snapshot = firebase.storage().ref();
            const mp3 = snapshot.child("song" + id + ".mp3");
            const url = await mp3.getDownloadURL();
            song = url;
        });



    }

}
export default createSong;