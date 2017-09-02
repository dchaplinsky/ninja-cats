;
"use strict";

var Vulyk = Vulyk || {
        State: {
            workplace: null,
            body: null,
            task_type: "",
            task_title: "",
            task_id: 0,
            task_init_state: null,
            task_state: null,
            task_wrapper: null,
            selected_terms: []
        },
        event_handlers: function () {
            var vu = this,
                vus = vu.State;

            vu.State.workplace
                .on("click", "a#save-button", function (e) {
                    e.preventDefault();
                    $("a#save-button, a#skip-button").addClass("disabled");

                    vus.body.trigger("vulyk.save", vu.save_report.bind(vu));
                })
                .on("click", "a#skip-button", function (e) {
                    e.preventDefault();
                    $("a#save-button, a#skip-button").addClass("disabled");

                    vus.body.trigger("vulyk.skip", vu.skip_task.bind(vu));
                });

            return vu;
        },
        load_next: function () {
            var vus = Vulyk.State;

            $.get(
                "/type/" + vus.task_type + "/next",
                function (data) {
                    vus.task_id = data.result.task.id;
                    vus.body.trigger("vulyk.next", data);
                }
            ).fail(function (data) {
                vus.body.trigger("vulyk.task_error", data.responseJSON);
            });
        },
        skip_task: function () {
            var vu = this,
                vus = vu.State;

            if (vus.task_id === 0) {
                return;
            }

            if (typeof(ga) !== "undefined") {
                ga('send', 'event', 'Task', 'Skip', vus.task_type);
            }

            $.post(
                "/type/" + vus.task_type + "/skip/" + vus.task_id,
                {},
                function (data) {
                    vu.load_next();
                }
            );
        },
        save_report: function (result) {
            var vu = this,
                vus = vu.State;

            if (typeof(result) !== "undefined") {
                if (typeof(ga) !== "undefined") {
                    ga('send', 'event', 'Task', 'Save', vus.task_type);
                }

                $.post(
                    "/type/" + vus.task_type + "/done/" + vus.task_id,
                    {result: JSON.stringify(result)},
                    function (data) {
                        vu.load_next();
                    });
            } else {
                $("a#save-button, a#skip-button").removeClass("disabled");
            }
        },

        /* http://xkcd.com/292/ */
        init: function () {
            var vu = this,
                vus = vu.State;

            $.ajaxSetup({traditional: true});

            $(function () {
                vus.workplace = $(".site-wrapper");
                vus.body = $(document.body);
                vus.task_wrapper = vus.workplace.find("#current_task");
                vu.event_handlers();

                if (vus.task_wrapper.length) {
                    vus.task_type = vus.task_wrapper.data("type");
                    vu.load_next();
                }

                vus.body.on("vulyk.next", function (e, data) {
                    $("a#save-button, a#skip-button").removeClass("disabled");
                });

                $('.popup-with-zoom-anim').magnificPopup({
                    type: 'inline',

                    fixedContentPos: false,
                    fixedBgPos: true,
                    overflowY: 'auto',
                    closeBtnInside: true,
                    preloader: false,

                    midClick: true,
                    removalDelay: 100,
                    mainClass: 'my-mfp-zoom-in'
                });
            });
        }
    };

Vulyk.init();
