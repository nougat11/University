let aside = {
    render: async() => {
        let view =
            `
            <a href="#"><img class="aside-whitelogo" src="assets/images/whitelogo.png"></a>
            <nav class="links">
                <a class="nav" href="#">Home</a>
                <a class="nav" href="#/search">Search</a>
                <a class = "nav" href = "#/library">Library</a>
                
            </nav>
            <hr>
            <nav class="playlists" id="playlists">
                
            </nav>
            `
        return view
    },
    after_render: async() => {
        const dbRef = database.ref();
        var data;
        let snapshot = await database.ref('/playlists/').once('value');
        data = snapshot.val();

        if (data !== undefined) {
            for (var i in data) {
                if (data[i].creator === firebase.auth().currentUser.email) {
                    var playlists = document.getElementById("playlists");
                    var tag = document.createElement("a");
                    tag.className = "playlist";
                    tag.href = "#/playlist/" + i;
                    tag.innerHTML = data[i].title;
                    playlists.insertAdjacentElement('afterbegin', tag);
                }
            }
        } else { var k = 5; }
    }

}
export default aside;