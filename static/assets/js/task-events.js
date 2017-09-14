(function(window, document, $) {
    'use strict';

    var badgesCount,
        actualCoins,
        potentialCoins,
        points,
        level;

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
                        //console.log(data.result.state.achievements);
                        var newBadgesCount = data.result.state.achievements.length,
                            newPotentialCoins = data.result.state.potential_coins,
                            newActualCoins = data.result.state.actual_coins,
                            newPoints = points = data.result.state.points,
                            newLevel = data.result.state.level;

                        //update notification dropdown
                        getUserEvents();

                        if(newPotentialCoins > potentialCoins) {
                            var delta = newPotentialCoins - potentialCoins;
                            toastr.success('Ви щойно заробили ' + delta + ' потенційних грн.', 'Вітаємо!', {"showMethod": "slideDown", "hideMethod": "slideUp", timeOut: 2000});
                            potentialCoins = newPotentialCoins;
                            $('.nav-block-money .potential-coins').html(potentialCoins);
                        }

                        if(newActualCoins > actualCoins) {
                            var delta = newActualCoins - actualCoins;
                            toastr.success('Ви щойно заробили ' + delta + ' активних грн.', 'Вітаємо!', {"showMethod": "slideDown", "hideMethod": "slideUp", timeOut: 2000});
                            actualCoins = newActualCoins;
                            $('.nav-block-money .actual-coins').html(actualCoins);
                        }

                        if(newPoints > points) {
                            var delta = newPoints - points;
                            toastr.info('Ви щойно здобули ' + delta + ' активних грн.', 'Вітаємо!', {"showMethod": "slideDown", "hideMethod": "slideUp", timeOut: 2000});
                            points = newPoints;
                        }

                        if(newLevel > level) {
                            toastr.info('Ви щойно здобули новий рівень', 'Вітаємо!', {"showMethod": "slideDown", "hideMethod": "slideUp", timeOut: 2000});
                            level = newLevel;
                            $('.nav-block-donats .current-level').html(level);
                        }

                        if(newBadgesCount > badgesCount) {
                            var delta = newBadgesCount - badgesCount;
                            //toastr.info('Ви щойно здобули ' + delta + ' активних грн.', 'Вітаємо!', {"showMethod": "slideDown", "hideMethod": "slideUp", timeOut: 2000});
                            badgesCount = newBadgesCount;
                        }
                    }
                })
                .fail(function() {
                    console.log( "error geeting user stats" );
                })
    }

    $('body').on('vulyk.next', function(event) {
        console.log('next task');

        if (typeof points === 'undefined') {
            getUserStats(true);
        } else {
            getUserStats();
        }
    });

})(window, document, jQuery);
