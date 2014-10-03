/**
 * Created by Alex Clement on 8/12/2014.
 */

$('document').ready(function() {
    $(document).on("change", ".border", function() {
        var source = $(this)[0];
        if (document.title == "Class Calendars - High School" || document.title == "Class Calendars - Middle School") {
            if (source.id.indexOf("class") > -1) {
                classchanged(source.id);
            } else if (source.id.indexOf("teacher") > -1) {
                teacherchanged(source.id);
            }
        } else if (document.title == "Class Calendars - Sixth Grade"){
            if(source.id.indexOf("homeroom") > -1) {
                sixthhomeroomchanged(source.id);
            } else if(source.id.indexOf("class") > -1){
                sixthclasschanged(source.id);
            } else if(source.id.indexOf('teacher') > -1){
                sixthteacherchanged(source.id);
            } else if(source.id.indexOf("rotation") > -1){
                rotationchanged(source.id)
            }
        } else if (document.title == "Class Calendars - Other Calendars") {
            console.log(source.id);
            if(source.id.indexOf('other') > -1){
                otherchanged(source.id);
            } else if(source.id.indexOf("electives") > -1) {
                otherelectivechanged(source.id);
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

function sixthclasschanged(id) {
    var period;
    period = $("#"+id).val();
    var idshort = id.substring(0, id.indexOf("class"));
    var class_name;
    switch (idshort) {
        case "science":
            class_name = '6th Science';
            break;
        case 'math':
            class_name = '6th Math';
            break;
        case 'langarts':
            class_name = '6th Language Arts';
            break;
        case 'socstud':
            class_name = '6th Social Studies';
            break;
    }
    $.get('/studentsite/teacher_list/', {class_name: class_name, period: parseInt(period)}, function(data) {
       $('#'+idshort+'tdiv').html(data);
    });

}

function teacherchanged(id) {
    var period;
    period = id.split("d")[1].substring(0, 1);
    var class_id;
    class_id = id.substring(0, id.indexOf("teacher"));
    var class_name;
    class_name = $("#" + class_id + "class").val();
    var teacher_name;
    teacher_name = $('#'+id).val();
    $.get('/studentsite/cal_id/', {class_name: class_name, period: period, teacher_name: teacher_name}, function(data) {
       $('#period'+period+'calid').html(data);
    });
}

function sixthteacherchanged(id) {
    var idshort = id.substring(0, id.indexOf("teacher"));
    var period;
    period = $("#"+idshort+"class").val();
    var class_name;
    switch (idshort) {
        case "science":
            class_name = '6th Science';
            break;
        case 'math':
            class_name = '6th Math';
            break;
        case 'langarts':
            class_name = '6th Language Arts';
            break;
        case 'socstud':
            class_name = '6th Social Studies';
            break;
    }
    var teacher_name;
    teacher_name = $('#'+id).val();
    $.get('/studentsite/cal_id/', {class_name: class_name, period: period, teacher_name: teacher_name}, function(data) {
       $('#'+idshort+'calid').html(data);
    });
}

function rotationchanged(id) {
    rotation = $("#"+id).val();
    $.get('/studentsite/sixth_rotations/', {rotation: parseInt(rotation)}, function(data) {
       $('#rotationcalid').html(data);
    });
}

function sixthhomeroomchanged(id) {
    var teacher_name = $('#homeroom').val();
    $.get('/studentsite/cal_id/', {class_name: "6th Homeroom", period: 9, teacher_name: teacher_name}, function(data){
        $('#homeroomcalid').html(data);
    });
}

function otherelectivechanged(id) {
    var period = 8;
    var class_title = $('#'+id).val();
    $.get('/studentsite/cal_id/', {class_name: class_title, period: period, teacher_name: ""}, function(data){
        $('#'+id+'calid').html(data);
    });
}

function otherchanged(id) {
    var period = 10;
    var class_title = $('#'+id).val();
    $.get('/studentsite/cal_id/', {class_name: class_title, period: period, teacher_name: ""}, function(data){
        $('#othercalid').html(data);
    });
}