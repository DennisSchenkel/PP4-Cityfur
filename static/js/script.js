
// Toggle for mobile sidebar

$(document).ready(function() {
    // Toggle sidebar visibility using a class
    $('#sidebarToggle').click(function() {
        $('#sidebar-menu').toggleClass('d-none');
    });
});


// Toggle for dropdown menu in profile

$(document).ready(function() {
    $(".img-prev-sm").click(function() {
        $(".profil-options-dropout").toggleClass("visually-hidden");
    });
});
