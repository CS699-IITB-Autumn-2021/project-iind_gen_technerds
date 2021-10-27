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

$('#read-btn').click(function() {
    window.location.href = 'read-pdf-page.html';
    return false;
});