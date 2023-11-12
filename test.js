async function submitForm() {
    // alert('submitted form');
    console.log('submitted form');
    var name = document.getElementById("name").value;  
    var email = document.getElementById("email").value;
    // add more of these for input data

    // Send data to the backend
    const response = await fetch("http://127.0.0.1:5000/process", { 
        // if you have a different ip address when running flask, change the http address
        method: "POST",
        mode: "cors",
        headers: {
            "Content-Type": "text/plain"
        },
        body: JSON.stringify({ name: name, email: email })  // add to this if you have more variables
    });
    const data = await response.json();
    // console.log('data');
    // console.log(data);
}