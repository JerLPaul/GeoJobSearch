function makeGoogleMapiFrame(origin, destination){
    originPlus = origin.replaceAll(" ", "+") //Turning plaintext into pluscode for Google Maps API call.
    destinationPlus = destination.replaceAll(" ", "+")
    ret = '<iframe id="mapFrame" width="1000" height="1000" frameborder="0" style="border:0" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps/embed/v1/directions?key=AIzaSyAB-fqyn8xxIfg7qo5-N8pl3TYbRL4Z3YA&origin=' + originPlus + '&destination=' + destinationPlus + '&avoid=tolls|highways" allowfullscreen></iframe>'
    return ret //Returns the iFrame element with 'origin' and 'destination' set accordingly.
}



$(document).ready(function(){
    $("#mapSubmit").click(function(){
        console.log("Generating Google map...")
        $("#map").empty() //Removing the last map, if one has been created already.
        $("#map").append(makeGoogleMapiFrame($("#origin").val(), $("#dest").val()))
    })
});

