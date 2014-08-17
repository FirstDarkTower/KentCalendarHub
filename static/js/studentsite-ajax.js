/**
 * Created by Alex Clement on 8/12/2014.
 */

$('document').ready(function() {
    $(document).on("change", ".border", function() {
        var source = $(this)[0];
        console.log(document.title);
        if (document.title == "Class Calendars - High School" || document.title == "Class Calendars - Middle School") {
            if (source.id.indexOf("class") > -1) {
                classchanged(source.id);
            } else if (source.id.indexOf("teacher") > -1) {
                teacherchanged(source.id);
            }
        } else if (document.title == "Class Calendars - Sixth Grade"){
            if(source.id.indexOf("homeroom") > -1) {
                sixthhomeroomchanged(source.id);
            } else if(source.id.indexOf()) {

            }
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

function sixthhomeroomchanged(id) {
    console.log("here");
    var teacher_name = $('#homeroom').val();
    $.get('/studentsite/cal_id/', {class_name: "6th Homeroom", period: 9, teacher_name: teacher_name}, function(data){
        $('#homeroomcalid').html(data);
    });
}