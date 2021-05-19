let createPlaylist = {
    render: async() => {
        let view =
            `
            <form class="form-player" action="javascript:void(0);">
            <fieldset class = "form-fieldset">
                <legend class="form-legend">CREATE PLAYLIST</legend>
                <input type="text" placeholder="Title" class = "form-input" id = "title">
                <input class = "form-input" type="text" placeholder="Description" id = "desription">

                <input class = "form-input cover1" name="file" id="file" type="file" accept="image/*">
                <div class="cover"><label for="file">Choose a cover</label></div>

                <button class = "form-button" id="createButton">CREATE</button>
            </fieldset>
        </form>
            `
        return view
    },
    after_render: async() => {
        var data;
        let snapshot = await database.ref('/playlists/').once('value');
        data = snapshot.val();
        var id = 1;
        for (var key in data) {
            id++;
        }


        var picture;


        var button = document.getElementById('createButton');

        button.addEventListener('click', async function(e) {
            var title1 = document.getElementById('title').value;
            var desription1 = document.getElementById('desription').value;
            firebase.database().ref('playlists/' + id).set({
                title: title1,
                desription: desription1,
                img: picture,
                creator: firebase.auth().currentUser.email

            });
            window.location.hash = '#';

        });
        var file = document.getElementById('file')
        file.addEventListener('change', async function(e) {
            var file = e.target.files[0];
            var storageRef = firebase.storage().ref('playlist' + id + '.png');
            picture = id;
            await storageRef.put(file);
            const snapshot = firebase.storage().ref();
            const img = snapshot.child("playlist" + id + ".png");
            const url = await img.getDownloadURL();
            picture = url;
        });



    }

}
export default createPlaylist;