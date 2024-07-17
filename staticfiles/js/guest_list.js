$(document).ready(function() {
    
    // Toggle for dropout menu in profile
    $(".profile").click(function(event) {
        // Check if the click is on a modal-trigger element, so that it doesn't stop the opening of the modal
       if (!$(event.target).hasClass('modal-trigger')) {
            event.stopPropagation();
            const $dropout = $(this).find(".profile-options-dropout");
            const $guestImg = $(this).find(".guest-img");
            const $alerts = $(this).find(".alerts");
            const $alertsDropout = $(this).find(".alerts-dropout");
            $(".profile-options-dropout").not($dropout).addClass("visually-hidden");
            $(".guest-img").not($guestImg).removeClass("img-prev-md").addClass("img-prev-sm");
            $dropout.toggleClass("visually-hidden");
            $guestImg.toggleClass("img-prev-md img-prev-sm");
            $(".alerts").not($alerts).removeClass("visually-hidden");
            $(".alerts-dropout").not($alertsDropout).addClass("visually-hidden");
            $alerts.toggleClass("visually-hidden");
            $alertsDropout.toggleClass("visually-hidden");
        }
    });

    // Close dropout menu when clicking outside of it
    $(document).click(function(event) {
        if (!$(event.target).closest(".profile").length && !$(event.target).closest(".modal-content").length) {
            $(".profile-options-dropout").addClass("visually-hidden");
            $(".guest-img").removeClass("img-prev-md").addClass("img-prev-sm");
            $(".alerts").removeClass("visually-hidden");
            $(".alerts-dropout").addClass("visually-hidden");
        }
    });

    // Toggle for check-in list in guest list
    $("#checkin-toggle").click(function() {
        $("#checked-in").toggleClass("d-none");
        $("#checked-out").toggleClass("d-none");
        $("#not-checked-in").toggleClass("d-none");
        $("#checkin-toggle").toggleClass("btn-primary btn-danger");
        $("#close-checkin").toggleClass("d-none");
        $("#count-checked-in").toggleClass("d-none");
        $("#count-not-checked-in").toggleClass("d-none");
    });

    // Toggle for check-in list in guest list
    $("#checkin-toggle").click(function() {
        $("#check-in-tutorial").addClass("d-none");
        $("#filter-tutorial").addClass("d-none");
    });

    // Toggle for gender selection in guest list 
    // Select male guests
    $("#male-selector").click(function() {
        $(".Male").removeClass("d-none");
        $(".Female").addClass("d-none");
        $("#male-selector").addClass("selected-selector");
        $("#female-selector").removeClass("selected-selector");
        $("#all-selector").removeClass("selected-selector");
    });

    // Select female guests
    $("#female-selector").click(function() {
        $(".Female").removeClass("d-none");
        $(".Male").addClass("d-none");
        $("#female-selector").addClass("selected-selector");
        $("#male-selector").removeClass("selected-selector");
        $("#all-selector").removeClass("selected-selector");
    });

    // Select all guests
    $("#all-selector").click(function() {
        $(".Female").removeClass("d-none");
        $(".Male").removeClass("d-none");
        $("#all-selector").addClass("selected-selector");
        $("#female-selector").removeClass("selected-selector");
        $("#male-selector").removeClass("selected-selector");
    });

    // Prevent modal from closing when clicking inside the modal content
    $('.modal-content').on('click', function(event) {
        if (!$(event.target).closest('[data-dismiss="modal"]').length) {
            event.stopPropagation();
        }
    });

});
