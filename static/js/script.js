// Toggle for dropdown menu in profile
$(document).ready(function() {
    $(".profile").click(function(event) {
        // Check if the click is on a modal-trigger element, so the it doesn't stop the opening of the modal
        if (!$(event.target).hasClass('modal-trigger')) {
            event.stopPropagation();
            const $dropdown = $(this).find(".profil-options-dropout");
            $(".profil-options-dropout").not($dropdown).addClass("visually-hidden");
            $dropdown.toggleClass("visually-hidden");
        }
    });

    $(document).click(function(event) {
        if (!$(event.target).closest(".profile").length) {
            $(".profil-options-dropout").addClass("visually-hidden");
        }
    });
});