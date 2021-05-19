let profile = {
    render: async() => {
        let view =
            `
            <article class = "profile-article">
        <button class = "profile-buttons" id = "cs">UPLOAD SONG</button>
        <button id ="out" class = "profile-buttons">LOG OUT</button>
        <button id ="cp" class = "profile-buttons">CREATE PLAYLIST</button>
    </article>
            `
        return view
    },
    after_render: async() => {
        var outButton = document.getElementById('out');
        outButton.addEventListener('click', function(event) {
            logout();
        });
        var cpButton = document.getElementById('cp');
        cpButton.addEventListener('click', function(event) {
            window.location.hash = '/cp';
        });
        var csButton = document.getElementById('cs');
        csButton.addEventListener('click', function(event) {
            window.location.hash = '/cs';
        });
    }

}
export default profile;