$(document).ready(
    /**
     * Enables and Disables the Convert Button when file is Uploaded or not
     */
    function change_pdf2w_btn(){
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
