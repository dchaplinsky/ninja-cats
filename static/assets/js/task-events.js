(function(window, document, $) {
    'use strict';

    var badgesCount,
        badges,
        actualCoins,
        potentialCoins,
        points,
        level;

    function generateBadgeAlertHtml(id, desc, url) {

        var html = '<div class="badge badge-' + id + '">'
            + '<img src="' + url + '" />'
            + '<h5 class="text-bold-400">' + desc + '</h5>'
            + '<a href="/cms/achievement/' + id + '" class="btn btn-social btn-min-width  mt-1 btn-facebook"><i class="fa fa-facebook"></i> Поділитись на Facebook</a>'
            + '</div>';

        return html;
    }

    function getUserStats(firstFun) {
        var userEventsJson = '/gamification/users/me/state',
            userEvents = $.getJSON( userEventsJson, function() {
                })
                .done(function( data ) {
                    if(firstFun) {
                        badgesCount = data.result.state.achievements.length;
                        badges = data.result.state.achievements;
                        potentialCoins = data.result.state.potential_coins;
                        actualCoins = data.result.state.actual_coins;
                        points = points = data.result.state.points;
                        level = data.result.state.level;
                    } else {
                        var newBadgesCount = data.result.state.achievements.length,
                            newBadges = data.result.state.achievements,
                            newPotentialCoins = data.result.state.potential_coins,
                            newActualCoins = data.result.state.actual_coins,
                            newPoints = points = data.result.state.points,
                            newLevel = data.result.state.level;

                        //update notification dropdown
                        getUserEvents();

                        if(newPotentialCoins > potentialCoins) {
                            var deltaPC = newPotentialCoins - potentialCoins;
                            toastr.success('Ви щойно заробили ' + deltaPC + ' потенційних кткв.', 'Вітаємо!', {"showMethod": "slideDown", "hideMethod": "slideUp", timeOut: 2000});
                            potentialCoins = newPotentialCoins;
                            $('.nav-block-money .potential-coins').html(potentialCoins);
                        }

                        if(newActualCoins > actualCoins) {
                            var deltaAC = newActualCoins - actualCoins;
                            toastr.success('Ви щойно заробили ' + deltaAC + ' активних кткв.', 'Вітаємо!', {"showMethod": "slideDown", "hideMethod": "slideUp", timeOut: 2000});
                            actualCoins = newActualCoins;
                            $('.nav-block-money .actual-coins').html(actualCoins);
                        }

                        if(newPoints > points) {
                            var deltaP = newPoints - points;
                            toastr.info('Ви щойно здобули ' + deltaP + ' активних кткв.', 'Вітаємо!', {"showMethod": "slideDown", "hideMethod": "slideUp", timeOut: 2000});
                            points = newPoints;
                        }

                        if(newLevel > level) {
                            toastr.info('Ви щойно здобули новий рівень', 'Вітаємо!', {"showMethod": "slideDown", "hideMethod": "slideUp", timeOut: 2000});
                            level = newLevel;
                            $('.nav-block-donats .current-level').html(level);
                        }

                        if (newBadgesCount > badgesCount) {
                            var oldBadgesID = $.map(badges, function( val, i ) { return val.id });
                            var newBadgesIndexes = $.map(newBadges, function( val, i ) {
                                if (oldBadgesID.indexOf(val.id) != -1) {
                                    return null;
                                }
                                return i;
                            });

                            if (newBadgesIndexes.length) {
                                badgesCount = newBadgesCount;
                                badges = newBadges;

                                var name = data.result.state.achievements[newBadgesIndexes[0]].name,
                                    desc = data.result.state.achievements[newBadgesIndexes[0]].description,
                                    id = data.result.state.achievements[newBadgesIndexes[0]].id,
                                    url = "/" + data.result.state.achievements[newBadgesIndexes[0]].badge;

                                swal({
                                    title: 'Ви отримали новий бейдж: <br />"' + name + '"!',
                                    type: 'success',
                                    html: true,
                                    text: generateBadgeAlertHtml(id, desc, url),
                                    showCloseButton: true
                                });

                                var snd = new Audio("/static/app-assets/sounds/purr.mp3"); // buffers automatically when created
                                snd.play();
                            }
                        }
                    }
                })
                .fail(function() {
                    console.log( "error geeting user stats" );
                })
    }

    $('body').on('vulyk.next', function(event) {
        if (typeof points === 'undefined') {
            getUserStats(true);
        } else {
            getUserStats();
        }
    });

})(window, document, jQuery);
