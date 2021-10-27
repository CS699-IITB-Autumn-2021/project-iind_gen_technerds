// $("input[type='number']").on("keyup", function(){
//     if($(this).val() != ""){
//         $("#split-btn").removeAttr("disabled");
//     }
// });

$(document).ready(
    function(){
        $('input:file').change(
            function(){
                if ($(this).val()) {
                    range_div_classes = document.querySelector('.range-main-div').classList;
                    if(range_div_classes.contains('hide')){
                        range_div_classes.remove('hide');
                    }
                    $("#r2").on("keyup", function(){
                        if($(this).val() != ""){
                            $("#split-btn").removeAttr("disabled");
                        }
                        else{
                            $('#split-btn').attr('disabled',true);
                        }
                    });
                } 
                else{
                    $('#split-btn').attr('disabled',true);
                }
            }
        );
});


$('#split-btn').click(function() {
    window.location.href = 'download-page-split.html';
    return false;
});

// $(document).on('click', '.addrange', function(){
//     var html = '<div class="range" style="display: flex; margin-bottom: 10px;"><div class="input-group"><div class="input-group-prepend"><div class="input-group-text">From</div></div><input type="number" class="form-control" required min="1" max=""></div><div class="input-group"><div class="input-group-prepend"><div class="input-group-text">To</div></div><input type="number" class="form-control" required min="1" max=""><button class=" delete_range btn btn-danger" onclick="del_range()">X</button></div>';
//     $(this).parent().append(html);
//     var delete_range_btn = document.getElementsByClassName('delete_range');
//     console.log(delete_range_btn);
// });

// function del_range(){
//     console.log("hello");
//     console.log(del_range.caller)
// }

$("#addrange").click(function(){
    var html = '<div id="range-div" class="range" style="display: flex; margin-bottom: 10px;"><div class="input-group"><div class="input-group-prepend"><div class="input-group-text">From</div></div><input id="r1" type="number" class="form-control" required min="1" max=""></div><div class="input-group"><div class="input-group-prepend"><div class="input-group-text">To</div></div><input type="number" id="r2" class="form-control" required min="1" max=""><button id="delete_range" class="btn btn-danger">X</button></div>';

    $("#additional_range").append(html);

    var check = document.getElementById('merging-splitted');
    classes_check = check.classList;
    if(classes_check.contains('hide')){
        classes_check.remove('hide');
    }
});

$(document).on('click','#delete_range',function(){
    $(this).closest('#range-div').remove();
});

// uploadbtn = document.getElementById('upload-btn');

// uploadbtn.addEventListener('click', function(){
//     range_div_classes = document.querySelector('.range-main-div').classList;
//     if(range_div_classes.contains('hide')){
//         range_div_classes.remove('hide');
//     }
// })