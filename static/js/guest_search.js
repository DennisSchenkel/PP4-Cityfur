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