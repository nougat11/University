let editSong = {
    render: async() => {
        let view =
            `
            <form class="form-player" action="javascript:void(0);">
            <fieldset class = "form-fieldset">
                <legend class="form-legend">EDIT SONG</legend>
                <input type="text" placeholder="Title" class = "form-input" id = "title1">
                <input class = "form-input" type="text" placeholder="Artist" id = "desription1">

                <input class = "form-input cover1" name="file" id="file" type="file" accept="image/*">
                <div class="cover"><label for="file">Choose a cover</label></div>
                
                <select name="select" id="select">
                        <option value="rap">Rap</option>
                        <option value="pop">Pop</option>
                        <option value="rock">Rock</option>
                    </select>
                <textarea class = "form-input lyrics-input" id = "lyricsinput" placeholder="lyrics"></textarea>
                <button class = "form-button" id="editButton">Edit</button>
            </fieldset>
        </form>
            `
        return view
    },
    after_render: async() => {
        var id = localStorage.getItem("id_edit");
        var data;
        let snapshot = await database.ref('/songs/' + id).once('value');

        data = snapshot.val();
        var title1 = document.getElementById('title1');
        var desription1 = document.getElementById('desription1');
        var select1 = document.getElementById('select');
        var lyrics = document.getElementById('lyricsinput');

        var picture;
        var song;

        console.log(data.title);
        title1.value = data.title;
        desription1.value = data.author;
        select1.value = data.genre;
        lyrics.innerHTML = data.lyrics;

        var button = document.getElementById('createButton');

        button.addEventListener('click', async function(e) {
            var title1 = document.getElementById('title1').value;
            var desription1 = document.getElementById('desription1').value;
            var select1 = document.getElementById('select').value;
            var lyrics = document.getElementById('lyricsinput').value;

            if (picture === undefined) {
                const snapshot = firebase.storage().ref();
                const img = snapshot.child("cover" + id + ".png");
                const url = await img.getDownloadURL();
                picture = url;
            }
            firebase.database().ref('songs/' + id).update({
                title: title1,
                author: desription1,
                img: picture,

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




    }

}
export default editSong;