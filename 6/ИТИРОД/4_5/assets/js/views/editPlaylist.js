let editPlaylist = {
    render: async() => {
        let view =
            `
            <form class="form-player" action="javascript:void(0);">
            <fieldset class = "form-fieldset">
                <legend class="form-legend">EDIT PLAYLIST</legend>
                <input type="text" placeholder="Title" class = "form-input" id = "title">
                <input class = "form-input" type="text" placeholder="Description" id = "desription">

                <input class = "form-input cover1" name="file" id="file" type="file" accept="image/*">
                <div class="cover"><label for="file">Choose a cover</label></div>

                <button class = "form-button" id="editButton">EDIT</button>
            </fieldset>
        </form>
            `
        return view
    },
    after_render: async() => {
        var id = localStorage.getItem("id_edit");
        var data;
        let snapshot = await database.ref('/playlists/' + id).once('value');
        var data = snapshot.val()
        var title1 = document.getElementById('title');
        var desription1 = document.getElementById('desription');
        title1.value = data.title;
        desription1.value = data.desription;
        var picture;


        var button = document.getElementById('editButton');

        button.addEventListener('click', async function(e) {
            var title1 = document.getElementById('title').value;
            var desription1 = document.getElementById('desription').value;
            if (picture === undefined) {
                const snapshot = firebase.storage().ref();
                const img = snapshot.child("playlist" + id + ".png");
                const url = await img.getDownloadURL();
                picture = url;
            }
            firebase.database().ref('playlists/' + id).update({
                title: title1,
                desription: desription1,
                img: picture,


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
export default editPlaylist;