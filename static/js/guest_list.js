$(document).ready(function() {
    
    // Toggle for dropdown menu in profile
    $(".profile").click(function(event) {
        // Check if the click is on a modal-trigger element, so the it doesn't stop the opening of the modal
        if (!$(event.target).hasClass('modal-trigger')) {
            event.stopPropagation();
            const $dropdown = $(this).find(".profil-options-dropout");
            $(".profil-options-dropout").not($dropdown).addClass("visually-hidden");
            $dropdown.toggleClass("visually-hidden");
        }
    });

    // Close dropdown menu when clicking outside of it
    $(document).click(function(event) {
        if (!$(event.target).closest(".profile").length) {
            $(".profil-options-dropout").addClass("visually-hidden");
        }
    });

    // Toggle for check-in list in guest list
    $("#checkin-toggle").click(function() {
        $("#checked-in").toggleClass("d-none");
        $("#checked-out").toggleClass("d-none");
        $("#not-checked-in").toggleClass("d-none");
        $("#checkin-toggle").toggleClass("btn-primary btn-danger");
        $("#close-checkin").toggleClass("d-none")


    });
});

