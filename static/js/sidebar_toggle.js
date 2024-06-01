// Toggle open mobile sidebar
$(document).ready(function() {
    $('#sidebarToggle').click(function() {
        $('#sidebar-menu').removeClass('d-none');
    });
});

// Toggle close mobile sidebar
$(document).ready(function() {
    $('#closeSidebar').click(function() {
        $('#sidebar-menu').addClass('d-none');
    });
});