let register = {
    render: async() => {
        let view =
            `
            <article>

            <form action="javascript:void(0);">
                <a><img class="blacklogo" src="assets/images/blacklogo.png"></a>
                <fieldset>
                    <legend>Sign up to free start listening.</legend>
                    <input type="email" placeholder="Email" id = "email">
                    <input type="password" placeholder="Password" id = "password">
                    <input type="text" placeholder="Profile name" id = "login">
                    <button id="submitRegistration">Sign up</button>
                    <a href="#/login">Have account? Log in.</a>
                </fieldset>
            </form>
        </article>
            `
        return view
    },
    after_render: async() => {
        var button = document.getElementById('submitRegistration');
        button.addEventListener('click', function(event) {
            register();
        });
        async function register() {
            var email = document.getElementById('email').value;
            var password = document.getElementById('password').value;
            var login = document.getElementById('login').value;
            firebase.auth().createUserWithEmailAndPassword(email, password)
                .then((userCredential) => {
                    // Signed in 
                    var user = userCredential.user;
                    window.location.hash = '#';
                })
                .catch((error) => {
                    var errorCode = error.code;
                    var errorMessage = error.message;
                    // ..
                });
        }
    }

}
export default register;