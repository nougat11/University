let login = {
    render: async() => {
        let view =
            `
            <article>

            <form action="javascript:void(0);">
                <a><img class="blacklogo" src="assets/images/blacklogo.png"></a>
                <fieldset>
                    <legend>To continue, log in Nougatify.</legend>
                    <input type="email" placeholder="Email" id="email">
                    <input type="password" placeholder="Password" id = "password">
                    <button id ="submitAuthorization"  class="log">Log in</button>
                    <b>Don't have an account?</b>
                    <button class='registerButton' id = "register">Register</button>
                </fieldset>
            </form>
        </article>
            `
        return view
    },
    after_render: async() => {
        var submitButton = document.getElementById('submitAuthorization');
        submitButton.addEventListener('click', function(event) {
            login();
        });
        var reginsterButton = document.getElementById('register');
        reginsterButton.addEventListener('click', function(event) {
            window.location.hash = '#/register';
        });
        async function login() {
            var email = document.getElementById('email').value;
            var password = document.getElementById('password').value;

            firebase.auth().signInWithEmailAndPassword(email, password)
                .then((userCredential) => {
                    // Signed in
                    var user = userCredential.user;

                    localStorage.setItem('currentUserId', user.uid);
                    window.location.hash = '#';
                    history.pushState(null, null, '#')
                        // ...
                })
                .catch((error) => {
                    var errorCode = error.code;
                    var errorMessage = error.message;
                });
        }
    }

}
export default login;