(function(window, document, $) {

    $('.donate-form').find('input,select,textarea').not('[type=submit]').jqBootstrapValidation({
        submitSuccess: function ($form, event) {
            $.ajax({
                type: 'POST',
                url: $form.attr('action'),
                data: $form.serialize(),
                success: function(data) {
                    console.log('submitted successfully!');
                },
                error: function (xhr, ajaxOptions, thrownError) {
                    console.log(xhr.status);
                    console.log(thrownError);
                }
            });
            event.preventDefault();
        }
    });

})(window, document, jQuery);