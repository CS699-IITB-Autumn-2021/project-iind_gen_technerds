$(document).ready(
    /**
     * Used to make the navigation sticky
     */
    function sticky_nav() {
    $('.js--section-features').waypoint(function(direction) {
        if (direction == "down") {
            $('nav').addClass('sticky');
        } else {
            $('nav').removeClass('sticky');
        }
    }, {
        offset: '60px;'
    });

    $('.js--nav-icon').click(
        /**
         * Used to make the navigation for smaller screen sizes
         */
        function toggle_nav(direction) {
            var nav = $('.js--main-nav');
            var icon = $('.js--nav-icon i');
            nav.slideToggle(200);
            if (icon.hasClass('fa-bars')) {
                icon.addClass('fa-times');
                icon.removeClass('fa-bars');
            } else {
                icon.removeClass('fa-times');
                icon.addClass('fa-bars');
            }
    })
});
