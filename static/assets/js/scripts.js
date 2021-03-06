(function(window, document, $) {
    'use strict';

    function populateFundList($fundsContainer) {
        var fundListJson = '/gamification/funds',
            fundList = $.getJSON( fundListJson, function() {
                })
                .done(function( data ) {
                    var fundsCount = data.result.funds.length;

                    if ( fundsCount > 0) {
                        var $containerList = $fundsContainer.find('.menu-content');
                        $fundsContainer.removeClass('hidden-xs-up');

                        for(var i = 0; i < fundsCount; i++) {
                            var html = '<li><a href="#" class="menu-item">' + data.result.funds[i].name + '</a></li>';
                            $containerList.append(html);
                        }
                    }
                })
                .fail(function() {
                    console.log( "error geeting funds list" );
                })
    }

    $('#inviteFriendModal input').on("click", function(e) {
        $(this).select();
        document.execCommand("copy");
        $('#inviteFriendModal .copy-notice').show();
    });

    $('#inviteFriendModal').on('hidden.bs.modal', function (e) {
        $('#inviteFriendModal .copy-notice').hide();
        $('#inviteFriendModal input').select();
        document.execCommand("copy");
    });

    $( document ).ready(function() {
        var $fundsContainer = $('#sidebar-fund-list');

        if($('.steps-page').length > 0) {
            $('#stepbanner-1-2-3').fsBanner();
        }

        $('.vertical-scroll').perfectScrollbar({
            suppressScrollX : true,
            theme: 'dark',
            wheelPropagation: true
        });

    });

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

    $(".share_on_fb").on("click", function(e) {
        e.preventDefault();

        var el = $(this);
        FB.ui({
                method: 'share',
                display: 'popup',
                quote: el.attr("title") || "",
                href: el.attr("href"),
                hashtag: "#Котики"
            },
            function(response){}
        );
    })
})(window, document, jQuery);
