// Search logic for guest lists full page
$(document).ready(function() {
    $('#search').click(function() {
        $("#all-selector").addClass("selected-selector");
        $("#female-selector").removeClass("selected-selector");
        $("#male-selector").removeClass("selected-selector");
        $(".Male").removeClass("d-none");
        $(".Female").removeClass("d-none");
    });
    $('#search').on('keyup', function() {
        const query = $(this).val().toLowerCase();
        $('.list-item').each(function() {
            const text = $(this).find('.item-name').text().toLowerCase();
            if (text.includes(query)) {
                $(this).removeClass('d-none');
            } else {
                $(this).addClass('d-none');
            }
        });
    });
});

// Search logic for guest lists mobile page
$(document).ready(function() {
    $('#mobile-search-bar').click(function() {
        $("#all-selector").addClass("selected-selector");
        $("#female-selector").removeClass("selected-selector");
        $("#male-selector").removeClass("selected-selector");
        $(".Male").removeClass("d-none");
        $(".Female").removeClass("d-none");
    });
    $('#mobile-search-bar').on('keyup', function() {
        const query = $(this).val().toLowerCase();
        $('.list-item').each(function() {
            const text = $(this).find('.item-name').text().toLowerCase();
            if (text.includes(query)) {
                $(this).removeClass('d-none');
            } else {
                $(this).addClass('d-none');
            }
        });
    });
});

// Toggle guest search on mobile
$(document).ready(function() {
    $('#search-toggle').click(function() {
        $('#mobile-search').toggleClass('d-none');
    });
});
