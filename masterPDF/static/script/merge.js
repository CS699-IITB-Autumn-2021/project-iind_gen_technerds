$(document).ready(
    function(){
        $('input:file').change(
            function(){
                if ($(this).val()) {
                    $('button:submit').attr('disabled',false);
                    // or, as has been pointed out elsewhere:
                    // $('input:submit').removeAttr('disabled');
                }else{
                    $('button:submit').attr('disabled',true);
                }
            }
        );
});

$('#merge-btn').click(function() {
    window.location.href = "{% url 'merge_download' %}";
    return false;
});


updateList = function() {
    var input = document.getElementById('myFile');
    var output = document.getElementById('fileList');
    var children = "";
    if (input.files.length>0){
        for (var i = 0; i < input.files.length; ++i) {
            children += '<li class="list-group-item">' + input.files.item(i).name + '</li>';
        }
        output.innerHTML = '<p>Files will be merged in the Following Order:</p><ul class="list-group">'+children+'</ul>';
    }
    else{
        output.innerHTML="";
    }
}
