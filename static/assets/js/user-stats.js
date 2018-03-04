(function(window, document, $) {
    'use strict';

    function getUserStats() {
        var userEventsJson = '/gamification/users/me/state',
            userEvents = $.getJSON( userEventsJson, function() {
            })
            .done(function( data ) {
                fillUserStats(data.result.state);
            })
            .fail(function() {
                console.log( "error geeting user events" );
            })
    }

    function generateBadgeHtml(id, name, desc, url) {

        var html = '<div class="badge badge-' + id + '"><div class="card"><div class="card-body"><div class="media"><div class="p-2 text-xs-center media-left media-middle">'
            + '<img src="' + url + '" class="height-75 ib float-xs-left" alt="" />'
            + '</div><div class="p-2 media-body">'
            + '<h5>' + name + '</h5>'
            + '<h5 class="text-bold-400">' + desc + '</h5>'
            + '</div></div></div></div></div>';

        return html;
    }

    function formateDate(unixTime) {
        var date = new Date(unixTime * 1000);
        return date.getDate() + '.' + date.getMonth() + '.' +  date.getFullYear() + ' ' + date.getHours() + ':' + (date.getMinutes()<10?'0':'') + date.getMinutes();
    }

    function fillUserStats(state) {
        var badgesCount,
            actualCoins,
            potentialCoins,
            points,
            level,
            $container = $('#user-achievements');

        if (state.actual_coins) {
            actualCoins = state.actual_coins;
        }

        if (state.potential_coins) {
            potentialCoins = state.potential_coins;
        }

        if (state.points) {
            points = state.points;
        }

        if (state.level) {
            level = state.level;
        }

        if (state.achievements && state.achievements.length > 0 && $container.length > 0) {
            badgesCount = state.achievements.length;

            for (var i=0; i < badgesCount; i++) {
                var name = state.achievements[i].name,
                    desc = state.achievements[i].description,
                    id = state.achievements[i].id,
                    url = '/static/app-assets/images/badges/0' + id + '.png';
                $container.append(generateBadgeHtml(id, name, desc, url));
            }

            var $badges = $container.find('.badge'),
                wrapper = $('<div class="row" />');
            var badgesNum = $badges.length;

            for (var c = 0; c < badgesNum; c+=2){
                $badges.filter(':eq('+c+'),:eq('+(c+1)+')').wrapAll(wrapper);
            }

        }
    }

    $( document ).ready(function() {
        if ($('.logged-in .gamification-stats').length > 0) {
            getUserStats();
        }
    });

})(window, document, jQuery);
