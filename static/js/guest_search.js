$(document).ready(function() {
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