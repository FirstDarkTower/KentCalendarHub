/**
 * Created by Alex Clement on 8/12/2014.
 */

$('document').ready(function() {
    $('.period1class').change(function() {
        var class_name;
        class_name = $(".period1class").val();
        $.get('/studentsite/teacher_list/', {class_name: class_name, period: 1}, function(data) {
           $('.period1teacher').html(data);
        });

    });
    $('.period1teacher').change(function() {
        var class_name;
        class_name = $(".period1class").val();
        var teacher_name;
        teacher_name = $('#border.period1teacher').val();
        $.get('/studentsite/cal_id/', {class_name: class_name, period: 1, teacher_name: teacher_name}, function(data) {
           $('.period1calid').html(data);
        });

    });
});
