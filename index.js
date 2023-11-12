async function submitForm() {
    // alert('submitted form');
    console.log('submitted form');

    var starttime = document.getElementById("starttime").value; 

    var errand1 = document.getElementById("errand1").value;  
    var tsTime1 = document.getElementById("tsTime1").value;  
    var specLoc1 = document.getElementById("specLoc1").value;
    // add more of these for input data
    var errand2 = document.getElementById("errand2").value;
    var tsTime2 = document.getElementById("tsTime2").value;  
    var specLoc2 = document.getElementById("specLoc2").value;

    var errand3 = document.getElementById("errand3").value;
    var tsTime3 = document.getElementById("tsTime3").value;  
    var specLoc3 = document.getElementById("specLoc3").value;

    var errand4 = document.getElementById("errand4").value;
    var tsTime4 = document.getElementById("tsTime4").value;  
    var specLoc4 = document.getElementById("specLoc4").value;

    var errand5 = document.getElementById("errand5").value;
    var tsTime5 = document.getElementById("tsTime5").value;  
    var specLoc5 = document.getElementById("specLoc5").value;

    // Send data to the backend
    const response = await fetch("http://127.0.0.1:5000/process", { 
        // if you have a different ip address when running flask, change the http address
        method: "POST",
        mode: "cors",
        headers: {
            "Content-Type": "text/plain"
        },
        body: JSON.stringify([{starttime: starttime}, { errand1: errand1, tsTime1: tsTime1, specLoc1: specLoc1}, { errand2: errand2, tsTime2: tsTime2, specLoc2: specLoc2}, { errand3: errand3, tsTime3: tsTime3, specLoc3: specLoc3}, { errand4: errand4, tsTime4: tsTime4, specLoc4: specLoc4}, { errand5: errand5, tsTime5: tsTime5, specLoc5: specLoc5}])  // add to this if you have more variables
        // body: JSON.stringify({ errand2: errand2, tsTime2: tsTime2, specLoc2: specLoc2})
    });
    //const data = await response.json();
    // console.log('data');
    // console.log(data);
}