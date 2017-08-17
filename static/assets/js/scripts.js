(function(window, document, $) {
    'use strict';

    $(window).load(function() {
        //close menu only at task-page
        if($('.task-page').length > 0) {
            // Toggle menu
            $.app.menu.toggle();

            setTimeout(function(){
                $(window).trigger( "resize" );
            },100);
        }
    });

    if($('.steps-page').length > 0) {
        $('#stepbanner-1-2-3').fsBanner();
    }

})(window, document, jQuery);
