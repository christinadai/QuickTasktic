async function submitForm() {
    // alert('submitted form');
    console.log('submitted form');
    var errand1 = document.getElementById("errand1").value;  
    var tsBool1 = document.getElementById("tsBool1").value;
    var tsTime1 = document.getElementById("tsTime1").value;  
    var specLocBool1 = document.getElementById("specLocBool1").value;
    var specLoc1 = document.getElementById("specLoc1").value;
    // add more of these for input data

    // Send data to the backend
    const response = await fetch("http://127.0.0.1:5000/process", { 
        // if you have a different ip address when running flask, change the http address
        method: "POST",
        mode: "cors",
        headers: {
            "Content-Type": "text/plain"
        },
        body: JSON.stringify({ errand1: errand1, tsBool1: tsBool1, tsTime1: tsTime1, specLocBool1: specLocBool1, specLoc1: specLoc1})  // add to this if you have more variables
    });
    //const data = await response.json();
    // console.log('data');
    // console.log(data);
}