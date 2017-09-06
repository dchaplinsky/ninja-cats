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

    function generateEventHtml(className, points, pointsText, /*pointsHistory,*/ pointsDate) {
        var html = '<div class="list-group-item ' + className + '"><div class="media">'
            + '<div class="media-left valign-middle"></div>'
            + '<div class="media-body">'
            + '<h6 class="media-heading">' + points + ' ' + pointsText + '</h6>'
            //+ '<p class="notification-text font-small-3 text-muted">' + pointsHistory + '</p>'
            + '<small><time datetime="' + pointsDate + '" class="media-meta text-muted">' + pointsDate + '</time></small>'
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
            $containerList.append(generateEventHtml('coins', coins, 'потенційних гривень зароблено', /*'опис тексту за що'*/ formateDate(events.timestamp)));
        }

        if (events.level_given) {
            eventsCount++;
            level = events.level_given;
            $containerList.append(generateEventHtml('level', level, 'рівень здобуто', /*'опис тексту за що'*/ formateDate(events.timestamp)));
        }

        if (events.points_given) {
            eventsCount++;
            points = events.points_given;
            $containerList.append(generateEventHtml('points', points, 'балів зароблено', /*'опис тексту за що'*/ formateDate(events.timestamp)));
        }

        if (eventsCount > 0) {
            $container.find('.tag-pill').removeClass('hidden-xs-up').html(eventsCount);
        }
    }

    $( document ).ready(function() {
        if ($('.logged-in').length > 0) {
            getUserEvents();
        }
    });

})(window, document, jQuery);
