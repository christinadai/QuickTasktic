async function submitForm() {
    // alert('submitted form');
    console.log('submitted form');
    var name = document.getElementById("name").value;  
    // add more of these for input data
    var email = document.getElementById("email").value;

    // Send data to the backend
    const response = await fetch("http://127.0.0.1:5000/process", {
        method: "POST",
        mode: "cors",
        headers: {
            "Content-Type": "text/plain"
        },
        body: JSON.stringify({ name: name, email: email })
    });
    const data = await response.json();
    console.log('data');
    console.log(data);
}