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
    window.location.href = 'download-page-merge.html';
    return false;
});


updateList = function() {
    var input = document.getElementById('myFile');
    var output = document.getElementById('fileList');

    const elem = document.createElement('p');
    elem.innerText = 'Drag the Files to arrange';

    var children = "";
    if (input.files.length>0){
        for (var i = 0; i < input.files.length; ++i) {
            children += '<div class="listitemClass list-group-item">' + input.files.item(i).name + '</div>';
        }
        output.parentNode.insertBefore(elem, output);
        output.innerHTML = children;
    }
    else{
        output.innerHTML="";
    }
}

$(function() {
    $( "#fileList" ).sortable({
    update: function(event, ui) {
    }//end update         
    });
});