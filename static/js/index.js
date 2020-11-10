balls = document.getElementsByClassName("numberCircle");
function onClick() {
       for (var i in balls){
           balls[i].innerHTML = "";
       }
    setTimeout(function(){
        // 1초 후 작동해야할 코드
        $.ajax({
            url: "http://localhost:8080/lotto",

            // Request headers.
            beforeSend: function(xhrObj){
                xhrObj.setRequestHeader("Content-Type","application/json");
            },

            type: "GET",
        })

        .done(function(data) {
            // Show formatted JSON on webpage.

            for (var i in balls){
                balls[i].innerHTML = data[i];
            }

        })

        .fail(function(jqXHR, textStatus, errorThrown) {
            // Display error message.
            var errorString = (errorThrown === "") ?
                "Error. " : errorThrown + " (" + jqXHR.status + "): ";
            errorString += (jqXHR.responseText === "") ?
                "" : (jQuery.parseJSON(jqXHR.responseText).message) ?
                    jQuery.parseJSON(jqXHR.responseText).message :
                        jQuery.parseJSON(jqXHR.responseText).error.message;
            alert(errorString);
        });
    }, 1000);



}