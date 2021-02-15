(function(window, document, $) {
    'use strict';

    var oldPopupUrl,
        newPopupUrl,
        showSubscribePopup = false;

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

    function createCookie(name,value) {
        document.cookie = name+"="+value+"; path=/";
    }

    function readCookie(name) {
        var nameEQ = name + "=";
        var ca = document.cookie.split(';');
        for(var i=0;i < ca.length;i++) {
            var c = ca[i];
            while (c.charAt(0)==' ') c = c.substring(1,c.length);
            if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
        }
        return null;
    }

    function eraseCookie(name) {
        createCookie(name,"",-1);
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

        oldPopupUrl = readCookie('seenPopupCookie');
        var $subscribePopup = $('#subscribePopup');

        if($subscribePopup.length !==0) {
            newPopupUrl = $subscribePopup.data('yt-id');

            if (newPopupUrl !== oldPopupUrl) {
                createCookie('seenPopupCookie', newPopupUrl);
                showSubscribePopup = true;
                oldPopupUrl = newPopupUrl;
            }
        }

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

        if (showSubscribePopup) {
            $('#subscribePopup').modal('show');
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
    });
})(window, document, jQuery);
