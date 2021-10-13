$(document).ready(
    function() {
        $('input:file').change(
            function() {
                if ($(this).val()) {
                    $('button:submit').attr('disabled', false);
                    // or, as has been pointed out elsewhere:
                    // $('input:submit').removeAttr('disabled'); 
                } else {
                    $('button:submit').attr('disabled', true);
                }
            }
        );
    });

$('#compress-btn').click(function() {
    window.location.href = 'download-page-compress.html';
    return false;
});