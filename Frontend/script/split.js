$(document).ready(
    /** 
     * Enables and Disables the Split Button when file is Uploaded or not
     */
    function change_split_btn(){
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


$("#addrange").click(
    /** 
     * Used to add ranges in Split PDF page when Add Range button is clicked 
     */
    function add_range(){
    var html = '<div id="range-div" class="range" style="display: flex; margin-bottom: 10px;"><div class="input-group"><div class="input-group-prepend"><div class="input-group-text">From</div></div><input type="number" class="form-control" required min="1" max="" name="extra_range1"></div><div class="input-group"><div class="input-group-prepend"><div class="input-group-text">To</div></div><input type="number" class="form-control" required min="1" max="" name="extra_range2"><button id="delete_range" class="btn btn-danger">X</button></div>';

    $("#additional_range").append(html);

    var check = document.getElementById('merging-splitted');
    classes_check = check.classList;
    if(classes_check.contains('hide')){
        classes_check.remove('hide');
    }
});


/** 
 * Used to delete a range on clicking the X button
 */
$(document).on('click','#delete_range',function del_range(){
    $(this).closest('#range-div').remove();
});
