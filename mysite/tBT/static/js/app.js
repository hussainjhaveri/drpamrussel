function initializeApp() {

    var firebaseConfig = {
    apiKey: "AIzaSyDlh95_gsPRYlVEFknaBe2Qv3tM7WdvaH0",
    authDomain: "hbe-form-dos.firebaseapp.com",
    databaseURL: "https://hbe-form-dos-default-rtdb.firebaseio.com/",
    projectId: "hbe-form-dos",
    storageBucket: "hbe-form-dos.appspot.com",
    messagingSenderId: "1076769006611",
    appId: "1:1076769006611:web:23ad6aff669ac15db88be6"
  };
//   const app = initializeApp(firebaseConfig);

// Initialize Firebase
firebaseConfig.initializeApp(firebaseConfig);

// Reference contactInfo collections
let contactInfo = firebase.database().ref("infos");

// Listen for a submit
document.querySelector(".contact-form").addEventListener("submit", submitForm);



function submitForm(e) {
    e.preventDefault();
    // get input Values
    let name = document.querySelector(".name").value;
    let email = document.querySelector(".email").value;
    let message = document.querySelector(".message").value;
    console.log(name, email, message);

    saveContactInfo(name, email, message);
}

// save infos to Firebase
function saveContactInfo(name, email, message) {
    let newContactInfo = contactInfo.push();

    newContactInfo.set({
        name: name,
        email: email,
        message: message,
    });
}
}

function test(event) {
    event.preventDefault();
    let name = document.querySelector(".name").value;
    console.log(name)
}

// document.querySelector(".").addEventListener("submit", console.log("anypting"));


function red() {
    e.preventDefault();
    // get input Values

    console.log(name, email, message);


}