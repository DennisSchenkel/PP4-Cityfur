
// Get the current date and set it as the default value for the date picker

// Define the current date
var currentDate = new Date();
var day = currentDate.getDate();
var month = currentDate.getMonth() + 1;
var year = currentDate.getFullYear();
var formattedDate = year + '-' + month + '-' + day;

// Set the default value of the date picker to the current date
$(document).ready(function() {
    $('#datepicker').val(formattedDate);
});

// Add calendar functionality to the date picker
$('.datepicker').datepicker({
    format: 'yyyy-mm-dd',
    autoclose: true
}).on('changeDate', function() {
    var selectedDate = $(this).val();
    window.location.href = '/?date=' + selectedDate;
});


