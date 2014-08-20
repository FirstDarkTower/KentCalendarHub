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
        }, minDate: 0, maxDate
        : +14 });
});

