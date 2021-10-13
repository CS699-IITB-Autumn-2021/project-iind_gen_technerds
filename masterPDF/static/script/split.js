$("input[type='number']").on("keyup", function(){
    if($(this).val() != ""){
        $("#split-btn").removeAttr("disabled");
    }
});

$(document).ready(
    function(){
        $('input:file').change(
            function(){
                if ($(this).val()) {
                    $('#upload-btn').attr('disabled',false);
                    // or, as has been pointed out elsewhere:
                    // $('input:submit').removeAttr('disabled');
                }
                else{
                    $('#upload-btn').attr('disabled',true);
                }
            }
        );
});


$('#split-btn').click(function() {
    window.location.href = "{% url 'split_downlaod' %}";
    return false;
});

$(document).on('click', '.addrange', function(){
    var html = '<div class="range" style="display: flex; margin-bottom: 10px;"><div class="input-group"><div class="input-group-prepend"><div class="input-group-text">From</div></div><input type="number" class="form-control" required min="1" max=""></div><div class="input-group"><div class="input-group-prepend"><div class="input-group-text">To</div></div><input type="number" class="form-control" required min="1" max=""></div>';
  $(this).parent().append(html);
});

uploadbtn = document.getElementById('upload-btn');

uploadbtn.addEventListener('click', function(){
    range_div_classes = document.querySelector('.range-main-div').classList;
    if(range_div_classes.contains('hide')){
        range_div_classes.remove('hide');
    }
})
