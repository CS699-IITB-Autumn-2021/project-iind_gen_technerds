$(document).ready(
    /** 
     * Enables and Disables the Read PDF Button when file is Uploaded or not
     */
    function change_pdf_reader_btn() {
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
