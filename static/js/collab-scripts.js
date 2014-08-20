/**
 * Created by aclement on 8/18/14.
 */

$('document').ready(function() {
    $('#datepicker').datepicker({
        onSelect:function() {
            var dateText = $('#datepicker').val();
            $.get('/collabcheckout/period_list', {dateText: dateText}, function(data) {
                $('#Periods').html(data);
                $('#PeriodsName').show();
            });
        }, beforeShowDay: $.datepicker.noWeekends, minDate: 0, maxDate
        : +14 });
    $('#Periods').change(function() {
        var period = $('#Periods').val();
        var dateText = $('#datepicker').val();
        var email = $('#email').val();
        console.log("Period: " + period + "  Date: " + dateText + "  Email: " + email)
        $.get('/collabcheckout/room_list', {dateText: dateText, period:period, email:email}, function(data) {
            $('#Rooms').html(data);
            $('#RoomsName').show();
        });

    });
});

