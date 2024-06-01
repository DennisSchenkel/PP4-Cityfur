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