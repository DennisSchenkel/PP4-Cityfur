console.log("Hello from script.js!")


$(document).ready(function() {
    $('#sidebarToggle').click(function() {
        $('#sidebar').toggleClass('d-none');
    });
});

function toggleSidebar() {
    var sidebar = document.getElementById("sidebar-menu");
    if (sidebar.style.display === "none" || sidebar.style.display === "") {
        sidebar.style.display = "block";
    } else {
        sidebar.style.display = "none";
    }
}




$(document).ready(function () {
    $(".navbar-toggler").click(function () {
        $(".sidebar-collapse").toggleClass("active");
        if ($(".sidebar-collapse").hasClass("active")) {
            $(".sidebar-collapse").css("max-width", "250px"); // Breite der Sidebar, wenn ausgefahren
        } else {
            $(".sidebar-collapse").css("max-width", "80px"); // Dünne Spalte
        }
    });
});





$(document).ready(function() {


    $("#success-btn").click(function() {
        $("li").css("background", "green");
    }); 

    $("#ddd").click(function() {
        $(this).css("background", "red");
    });

    $("#success-btn").hover(function() {
        $("#text").toggle("slow");
        $("li").css("color", "yellow").slideUp(2000).slideDown(2000);
    });



});



const API_KEY_TWO = "VZn-Fx2ohpPGHAs_RhP_m6IgxYA";
const API_URL_TWO = "https://ci-jshint.herokuapp.com/api";
// const resultsModal = new bootstrap.Modal(document.getElementById("resultsModal"));

document.getElementById("status").addEventListener("click", eventObject => getStatus(eventObject));

async function getStatus(eventObject) {

    const queryString = `${API_URL_TWO}?api_key=${API_KEY_TWO}`;

    const response = await fetch(queryString);

    const data = await response.json();

    if (response.ok) {
        console.log(data.expiry);
    } else {
        console.log(eventObject);
        throw new Error(data.error);
    }

}    