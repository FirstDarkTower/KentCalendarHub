/**
 * Created by Alex Clement on 8/12/2014.
 */

$('document').ready(function() {
    $(document).on("change", ".border", function() {
        var source = $(this)[0];
        console.log(source.id);
        if (source.id.indexOf("class") > -1) {
            classchanged(source.id);
        } else if(source.id.indexOf("teacher") > -1) {
            teacherchanged(source.id);
        }

    });;
});

function classchanged(id) {
    var period;
    period = id.split("d")[1].substring(0, 1);
    var class_name;
    class_name = $("#"+id).val();
    $.get('/studentsite/teacher_list/', {class_name: class_name, period: parseInt(period)}, function(data) {
       $('#period'+period+'tdiv').html(data);
    });
}

function teacherchanged(id) {
    var period;
    period = id.split("d")[1].substring(0, 1);
    var class_id
    class_id = id.substring(0, id.indexOf("teacher"));
    var class_name;
    class_name = $("#" + class_id + "class").val();
    var teacher_name;
    teacher_name = $('#'+id).val();
    $.get('/studentsite/cal_id/', {class_name: class_name, period: period, teacher_name: teacher_name}, function(data) {
       $('#period'+period+'calid').html(data);
    });
}