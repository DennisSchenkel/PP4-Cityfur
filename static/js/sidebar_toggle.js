// Toggle open mobile sidebar
$(document).ready(function() {
    $('#sidebar-toggle').click(function() {
        $('#sidebar-menu').removeClass('d-none');
        $('#sidebar-toggle').addClass('d-none');
    });
});

// Toggle close mobile sidebar
$(document).ready(function() {
    $('#closeSidebar').click(function() {
        $('#sidebar-menu').addClass('d-none');
        $('#sidebar-toggle').removeClass('d-none');
    });
});