$(document).ready(function() {
    
    // Toggle for dropdout menu in profile
    $(".profile").click(function(event) {
        // Check if the click is on a modal-trigger element, so the it doesn't stop the opening of the modal
        if (!$(event.target).hasClass('modal-trigger')) {
            event.stopPropagation();
            const $dropout = $(this).find(".profil-options-dropout");
            const $guestImg = $(this).find(".guest-img");
            $(".profil-options-dropout").not($dropout).addClass("visually-hidden");
            $(".guest-img").not($guestImg).removeClass("img-prev-md").addClass("img-prev-sm");
            $dropout.toggleClass("visually-hidden");
            $guestImg.toggleClass("img-prev-md img-prev-sm");
        }
    });

    // Close dropout menu when clicking outside of it
    $(document).click(function(event) {
        if (!$(event.target).closest(".profile").length) {
            $(".profil-options-dropout").addClass("visually-hidden");
            $(".guest-img").removeClass("img-prev-md").addClass("img-prev-sm");
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

    // Toggle for gender selection in guest list 
    $("#male-selector").click(function() {
        $(".Male").removeClass("d-none");
        $(".Female").addClass("d-none");
        $("#male-selector").addClass("selected-selector");
        $("#female-selector").removeClass("selected-selector");
        $("#all-selector").removeClass("selected-selector");
    });

    $("#female-selector").click(function() {
        $(".Female").removeClass("d-none");
        $(".Male").addClass("d-none");
        $("#female-selector").addClass("selected-selector");
        $("#male-selector").removeClass("selected-selector");
        $("#all-selector").removeClass("selected-selector");
    });

    $("#all-selector").click(function() {
        $(".Female").removeClass("d-none");
        $(".Male").removeClass("d-none");
        $("#all-selector").addClass("selected-selector");
        $("#female-selector").removeClass("selected-selector");
        $("#male-selector").removeClass("selected-selector");
    });
    }   
);


