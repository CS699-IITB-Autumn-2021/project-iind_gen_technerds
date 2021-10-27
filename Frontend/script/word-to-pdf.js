
$(document).ready(
    function(){
        $('input:file').change(
            function(){
                if ($(this).val()) {
                    $('button:submit').attr('disabled',false);
                    // or, as has been pointed out elsewhere:
                    // $('input:submit').removeAttr('disabled'); 
                }else{
                    $('#upload-btn').attr('disabled',true);
                }
            }
        );
});

$('#convert-btn').click(function() {
    window.location.href = 'download-page-w2p.html';
    return false;
});