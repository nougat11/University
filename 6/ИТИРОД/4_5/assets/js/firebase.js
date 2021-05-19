var firebaseConfig = {
    apiKey: "AIzaSyA5N967RfiNnUQwvhvxDyH8qa2WkyfvppY",
    authDomain: "fir-hosting-c6477.firebaseapp.com",
    databaseURL: "https://fir-hosting-c6477-default-rtdb.firebaseio.com",
    projectId: "fir-hosting-c6477",
    storageBucket: "fir-hosting-c6477.appspot.com",
    messagingSenderId: "298042876543",
    appId: "1:298042876543:web:f70a8a47740492fc01954a",
    measurementId: "G-8Q5T3DKNFL"
};


// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();
var database = firebase.database();

function logout() {
    history.pushState(null, null, '#/logout')
    firebase.auth().signOut();
    localStorage.removeItem('currentUserId');
    window.location.hash = '#/';
}