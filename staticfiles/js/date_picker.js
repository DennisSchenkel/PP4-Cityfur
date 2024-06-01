
// Get the current date and set it as the default value for the date picker

// Get the current date in the format yyyy-mm-dd
function getCurrentDate() {
    const currentDate = new Date();
    const day = currentDate.getDate();
    const month = addjustMonth(currentDate)
    const year = currentDate.getFullYear();
    const currentFormattedDate = year + '-' + month + '-' + day;
    return currentFormattedDate;
}

// Add a zero to the month if it is less than 10
function addjustMonth(currentDate){
    if (currentDate.getMonth() < 9) { 
        return '0' + (currentDate.getMonth() + 1); 
        } 
        else { 
            return currentDate.getMonth() + 1; 
        };
}

// Get the date from the URL
function getDateFromURL() {
    const urlDate = new URLSearchParams(window.location.search);
    return urlDate.get('date');
}

// Get the final formatted date for datepicker
function getFormattedDate() {
    const dateFromURL = getDateFromURL();
    console.log(getCurrentDate());
    console.log(dateFromURL);
    return dateFromURL ? dateFromURL : getCurrentDate();
}

// Set the default value of the date picker to the current date
$(document).ready(function() {
    $('#datepicker').val(getFormattedDate());
});

// Add calendar functionality to the date picker
$('.datepicker').datepicker({
    format: 'yyyy-mm-dd',
    autoclose: true
}).on('changeDate', function() {
    const selectedDate = $(this).val();
    window.location.href = '/?date=' + selectedDate;
});


