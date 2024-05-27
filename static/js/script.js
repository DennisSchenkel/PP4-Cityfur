
// Toggle for mobile sidebar

$(document).ready(function() {
    // Toggle sidebar visibility using a class
    $('#sidebarToggle').click(function() {
        $('#sidebar-menu').toggleClass('d-none');
    });
});


// Toggle for dropdown menu in profile

$(document).ready(function() {
    $(".profile").click(function(event) {
        event.stopPropagation();
        var $dropdown = $(this).find(".profil-options-dropout");
        $(".profil-options-dropout").not($dropdown).addClass("visually-hidden");
        $dropdown.toggleClass("visually-hidden");
    });

    $(document).click(function(event) {
        if (!$(event.target).closest(".profile").length) {
            $(".profil-options-dropout").addClass("visually-hidden");
        }
    });
});