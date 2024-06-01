(document).ready(function() {
    $('#search').on('keyup', function() {
        var query = $(this).val().toLowerCase();
        $('.result-item').each(function() {
            var text = $(this).text().toLowerCase();
            if (text.includes(query)) {
                $(this).removeClass('hidden');
            } else {
                $(this).addClass('hidden');
            }
        });
    });
});