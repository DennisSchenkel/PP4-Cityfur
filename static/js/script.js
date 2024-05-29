


// Toggle open mobile sidebar
$(document).ready(function() {
    $('#sidebarToggle').click(function() {
        $('#sidebar-menu').removeClass('d-none');
    });
});

// Toggle close mobile sidebar
$(document).ready(function() {
    $('#closeSidebar').click(function() {
        $('#sidebar-menu').addClass('d-none');
    });
});

// Close mobile sidebar when clicking outside
/*
$(document).ready(function() {
    $(document).click(function() {
        if (!$('#sidebar-menu').hasClass('d-none')) {
            $('#sidebar-menu').addClass('d-none');
        }
    });
});
*/

// Toggle for dropdown menu in profile
$(document).ready(function() {
    $(".profile").click(function(event) {
        event.stopPropagation();
        const $dropdown = $(this).find(".profil-options-dropout");
        $(".profil-options-dropout").not($dropdown).addClass("visually-hidden");
        $dropdown.toggleClass("visually-hidden");
    });

    $(document).click(function(event) {
        if (!$(event.target).closest(".profile").length) {
            $(".profil-options-dropout").addClass("visually-hidden");
        }
    });
});