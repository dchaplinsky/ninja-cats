(function(window, document, $) {
    'use strict';

    function getUserEvents() {
        var userEventsJson = '/gamification/events/all',
            userEvents = $.getJSON( userEventsJson, function() {
                //console.log( "run" );
            })
            .done(function( data ) {
                console.log(data);
                var isViewed = data.result.events[0].viewed;

                if(!isViewed) {
                    fillUserEvents(data.result.events[0]);
                }
            })
            .fail(function() {
                console.log( "error geeting user events" );
            })
    }

    function generateEventHtml(iconClass, points, pointsText, /*pointsHistory,*/ pointsDate) {
        var html = '<div class="list-group-item"><div class="media">'
            + '<div class="media-left valign-middle"><i class="icon-bg-circle ' + iconClass + '"></i></div>'
            + '<div class="media-body">'
            + '<h6 class="media-heading yellow darken-3">' + points + ' ' + pointsText + '</h6>'
            //+ '<p class="notification-text font-small-3 text-muted">' + pointsHistory + '</p>'
            + '<small><time datetime="2015-06-11T18:29:20+08:00" class="media-meta text-muted">' + pointsDate + '</time></small>'
            + '</div></div></div>';

        return html;
    }

    function formateDate(unixTime) {
        var date = new Date(unixTime * 1000);
        return date.getDate() + '.' + date.getDate() + '.' +  date.getFullYear() + ' ' + date.getHours() + ':' + date.getMinutes();
    }

    function fillUserEvents(events) {
        var eventsCount = 0,
            coins,
            points,
            level,
            $container = $('nav .dropdown-notification'),
            $containerList = $container.find('.dropdown-menu .list-group');

        if (events.coins) {
            eventsCount++;
            coins = events.coins;
            $containerList.append(generateEventHtml('ft-plus-circle bg-yellow bg-darken-3', coins, 'потенційних гривень зароблено', /*'опис тексту за що'*/ formateDate(events.timestamp)));
        }

        if (eventsCount > 0) {
            $container.find('.tag-pill').removeClass('hidden-xs-up').html(eventsCount);
            $container.find('.notification-tag').html('Нових подій: ' + eventsCount);
        }
    }

    $( document ).ready(function() {
        if ($('.logged-in').length > 0) {
            getUserEvents();
        }
    });

})(window, document, jQuery);
