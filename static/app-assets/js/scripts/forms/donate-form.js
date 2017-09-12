(function(window, document, $) {

    var donateStatus,
        amountTransfer,
        fund;

    $('.donate-form').find('input,select,textarea').not('[type=submit]').jqBootstrapValidation({
        submitSuccess: function ($form, event) {
            $.ajax({
                type: 'POST',
                url: $form.attr('action'),
                data: $form.serialize(),
                success: function(data) {
                    $form.parents('.modal').modal('toggle');
                    var amount = $form.find('input[name="amount"]').val(),
                        fundName = $form.find('input[name="fund_name"]').val();
                    $(window).trigger('donateDoneSuccess.kotiki', ['', amount, fundName]);
                },
                error: function (xhr, ajaxOptions, thrownError) {
                    console.log(xhr.status);
                    console.log(thrownError);
                    $form.parents('.modal').modal('toggle');
                    $(window).trigger('donateDoneError.kotiki', [xhr.status, 0, '']);
                }
            });
            event.preventDefault();
        }
    });

    $(window).on('donateDoneSuccess.kotiki', function(event, status, amount, name) {
        donateStatus = 'good';
        amountTransfer = amount;
        fund = name;
    });

    $(window).on('donateDoneError.kotiki', function(event, status, amount, name) {
        donateStatus = status;
        //todo
    });

    $('.modal').on('hidden.bs.modal', function (e) {
        if (donateStatus === 'good') {
            toastr.info('Ви відправили ' + amountTransfer + ' грн. фонду ' + fund, 'Дякуємо!');
        } else {
            toastr.error('Не вдалося перевести кошти', 'Помилка!'); //todo
        }
    })

})(window, document, jQuery);