(function(window, document, $) {
    'use strict';

    var badgesCount,
        actualCoins,
        potentialCoins,
        points,
        level;

    function generateBadgeAlertHtml(id, desc, url) {

        var html = '<div class="badge badge-' + id + '">'
            + '<img src="' + url + '" />'
            + '<h5 class="text-bold-400">' + desc + '</h5>'
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
                        potentialCoins = data.result.state.potential_coins;
                        actualCoins = data.result.state.actual_coins;
                        points = points = data.result.state.points;
                        level = data.result.state.level;
                    } else {
                        var newBadgesCount = data.result.state.achievements.length,
                            newPotentialCoins = data.result.state.potential_coins,
                            newActualCoins = data.result.state.actual_coins,
                            newPoints = points = data.result.state.points,
                            newLevel = data.result.state.level;

                        //update notification dropdown
                        getUserEvents();

                        if(newPotentialCoins > potentialCoins) {
                            var deltaPC = newPotentialCoins - potentialCoins;
                            toastr.success('Ви щойно заробили ' + deltaPC + ' потенційних грн.', 'Вітаємо!', {"showMethod": "slideDown", "hideMethod": "slideUp", timeOut: 2000});
                            potentialCoins = newPotentialCoins;
                            $('.nav-block-money .potential-coins').html(potentialCoins);
                        }

                        if(newActualCoins > actualCoins) {
                            var deltaAC = newActualCoins - actualCoins;
                            toastr.success('Ви щойно заробили ' + deltaAC + ' активних грн.', 'Вітаємо!', {"showMethod": "slideDown", "hideMethod": "slideUp", timeOut: 2000});
                            actualCoins = newActualCoins;
                            $('.nav-block-money .actual-coins').html(actualCoins);
                        }

                        if(newPoints > points) {
                            var deltaP = newPoints - points;
                            toastr.info('Ви щойно здобули ' + deltaP + ' активних грн.', 'Вітаємо!', {"showMethod": "slideDown", "hideMethod": "slideUp", timeOut: 2000});
                            points = newPoints;
                        }

                        if(newLevel > level) {
                            toastr.info('Ви щойно здобули новий рівень', 'Вітаємо!', {"showMethod": "slideDown", "hideMethod": "slideUp", timeOut: 2000});
                            level = newLevel;
                            $('.nav-block-donats .current-level').html(level);
                        }

                        if(newBadgesCount > badgesCount) {
                            //var bDelta = newBadgesCount - badgesCount;
                            badgesCount = newBadgesCount;

                            var name = data.result.state.achievements[badgesCount-1].name,
                                desc = data.result.state.achievements[badgesCount-1].description,
                                id = data.result.state.achievements[badgesCount-1].id,
                                url = '/static/app-assets/images/badges/0' + id + '.png';

                            swal({
                                title: 'Ви отримали новий бейдж: <br>"' + name + '"!',
                                type: 'success',
                                html: true,
                                text: generateBadgeAlertHtml(id, desc, url),
                                showCloseButton: true
                            });

                            var snd = new Audio("/static/app-assets/sounds/tada.mp3");
                            snd.play();
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
