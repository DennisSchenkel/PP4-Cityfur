// Get the date from the datepicker and display it on the page as part of the headline
$(document).ready(function() {
    const date = document.getElementById('datepicker').value;

    const formattedDate = new Date(date).toLocaleDateString('en-US', { day: 'numeric', month: 'long', year: 'numeric' });

    $(".date-selection").text(formattedDate);
});
