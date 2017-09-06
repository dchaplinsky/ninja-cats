(function(window, document, $) {
    'use strict';

    function getUserEvents() {
        var userEventsJson = '/gamification/events/all',
            userEvents = $.getJSON( userEventsJson, function() {
            })
            .done(function( data ) {
                fillUserEvents(data.result.events);
            })
            .fail(function() {
                console.log( "error geeting user events" );
            })
    }

    function generateEventHtml(className, points, pointsText, pointsHistory, pointsDate) {
        var hiddenClass = '';

        if (pointsHistory.length === 0) {
            hiddenClass = ' hidden-xs-up';
        }

        var html = '<div class="list-group-item ' + className + '"><div class="media">'
            + '<div class="media-left valign-middle"></div>'
            + '<div class="media-body">'
            + '<h6 class="media-heading">' + points + ' ' + pointsText + '</h6>'
            + '<p class="notification-text font-small-3 text-muted' + hiddenClass + '">' + pointsHistory + '</p>'
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
            badgesCount,
            coins,
            points,
            level,
            $container = $('nav .dropdown-notification'),
            $containerList = $container.find('.dropdown-menu .list-group');

        for (var e = 0; e < events.length; e++) {
            var isViewed = events[e].viewed;

            if(!isViewed) {
                if (events[e].achievements && events[e].achievements.length > 0) {
                    badgesCount = events[e].achievements.length;
                    eventsCount = eventsCount + badgesCount;

                    for (var i=0; i < badgesCount; i++) {
                        $containerList.append(generateEventHtml('badge', '', 'отримано новий бейдж', events[e].achievements[i].name, formateDate(events[e].timestamp)));
                    }
                }

                if (events[e].coins) {
                    eventsCount++;
                    coins = events[e].coins;
                    $containerList.append(generateEventHtml('coins', coins, 'потенційних гривень зароблено', '', formateDate(events[e].timestamp)));
                }

                if (events[e].level_given) {
                    eventsCount++;
                    level = events[e].level_given;
                    if (level !== null) {
                        $containerList.append(generateEventHtml('level', level, 'рівень здобуто', '', formateDate(events[e].timestamp)));
                    }
                }

                if (events[e].points_given) {
                    eventsCount++;
                    points = events[e].points_given;
                    $containerList.append(generateEventHtml('points', points, 'балів зароблено', '', formateDate(events[e].timestamp)));
                }

                if (eventsCount > 0) {
                    $container.find('.tag-pill').removeClass('hidden-xs-up').html(eventsCount);
                }
            }
        }
    }

    $( document ).ready(function() {
        if ($('.logged-in').length > 0) {
            getUserEvents();
        }
    });

})(window, document, jQuery);
