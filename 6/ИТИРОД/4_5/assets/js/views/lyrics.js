let lyrics = {
    render: async() => {
        let view =
            `
            <dialog id = "lyricsDiaglog">
            <b id ="lyricsDialogdisplay"></b>
        </dialog>
            `
        return view
    },
    after_render: async() => {
        var fragment = document.getElementById("lyricsDiaglog");
        fragment.showModal();
        fragment.addEventListener('click', function(event) {
            var rect = fragment.getBoundingClientRect();
            if (!(rect.top <= event.clientY && event.clientY <= rect.top + rect.height &&
                    rect.left <= event.clientX && event.clientX <= rect.left + rect.width)) {

                window.history.back();
            }
        });
        var lyricsDialogdisplay = document.getElementById("lyricsDialogdisplay");
        lyricsDialogdisplay.innerHTML = localStorage.getItem("lyrics");



    }

}
export default lyrics;