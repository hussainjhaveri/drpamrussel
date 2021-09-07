import { initializeApp } from "firebase/app";
// import { getAnalytics } from "firebase/analytics";

// Your web app's Firebase configuration
// const firebaseConfig = {
//     apiKey: "AIzaSyAlhJkrsOrr1ZauG1VrXDVs605bkKyKCWY",
//     authDomain: "hbe-form.firebaseapp.com",
//     projectId: "hbe-form",
//     storageBucket: "hbe-form.appspot.com",
//     messagingSenderId: "241397882982",
//     appId: "1:241397882982:web:669f86e1c2d54746ed0da7",
//     measurementId: "G-LDKTDY7NP4"
//   }; -first one

const firebaseConfig = {
    apiKey: "AIzaSyDlh95_gsPRYlVEFknaBe2Qv3tM7WdvaH0",
    authDomain: "hbe-form-dos.firebaseapp.com",
    databaseURL: "https://hbe-form-dos-default-rtdb.firebaseio.com/",
    projectId: "hbe-form-dos",
    storageBucket: "hbe-form-dos.appspot.com",
    messagingSenderId: "1076769006611",
    appId: "1:1076769006611:web:23ad6aff669ac15db88be6"
  };


  const app = initializeApp(firebaseConfig);
    // const analytics = getAnalytics(app);
// Initialize Firebase
firebaseConfig.initializeApp(firebaseConfig);

// Reference contactInfo collections
let contactInfo = firebase.database().ref("infos");

// Listen for a submit
document.querySelector(".contact-form").addEventListener("submit", submitForm);


function submitForm(e) {
    e.preventDefault();
console.log(123)
    // get input Values
    let name = document.querySelector(".name").value;
    let email = document.querySelector(".email").value;
    let message = document.querySelector(".message").value;

    saveContactInfo(name, email, message);
//commented for test, uncomment later
    // document.querySelector(".contact-form").reset();

    // sendEmail(name, email, message);
}

// save infos to Firebase
function saveContactInfo(name, email, message) {
    let newContactInfo = contactInfo.push();

    newContactInfo.set({
        name: name,
        email: email,
        message: message,
    });

    retrieveInfos();
}

// retrieve infos
function retrieveInfos() {
    let ref = firebase.datebase().ref("infos");
    ref.on("value", gotData);
}

function gotData(data) {
    let info = data.val();
    let keys = Object.keys(info);

    for (let i = 0; i < keys.length; i++) {
        let infoData = keys[i];
        let name = info[infoData].name;
        let message = info[infoData].message;
        console.log(name, email, message);

        let infosresults = document.querySelector(".infosResults");

        infosresults.innerHTML += `<div>
        <p><strong>Name: <strong/>${name} <br/>
        <a><strong>Email: <strong/>${email}</a> <br/>
        <a><strong>Message: <strong/>${message}</a>
        </p>
        </div>`;
    }
}

retrieveInfos();

// Send Email Info
function sendEmail(name, email, message) {
    email.send({
        Host: "smtp.gmail.com",
        User: "runtimeready@gmail.com",
        Password: "eimnygvbbbejnszq",
        To: 'aidanfire360@gmail.com',
        From: 'runtimeready@gmail.com',
        Subject: `${name} sent you a message`,
        Body: `Name: ${name} <br/> Email: ${email} <br/> Message: ${message}`,
    }).then((message) => alert("mail has been succesfuly sent"))
}

function test() {
    
    // get input Values
    console.log("bark")
    console.log(name, email, message);


}