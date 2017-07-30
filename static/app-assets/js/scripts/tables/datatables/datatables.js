$(document).ready(function() {

    var allTasksListTable, tSettings;

    allTasksListTable = $('#user-tasks-table').dataTable( {
        "language": {
            "sProcessing":   "Зачекайте...",
            "sLengthMenu":   "Показати _MENU_ записів",
            "sZeroRecords":  "Записи відсутні.",
            "sInfo":         "Записи з _START_ по _END_ із _TOTAL_ записів",
            "sInfoEmpty":    "Записи з 0 по 0 із 0 записів",
            "sInfoFiltered": "(відфільтровано з _MAX_ записів)",
            "sInfoPostFix":  "",
            "sSearch":       "Пошук:",
            "sUrl":          "",
            "oPaginate": {
            "sFirst": "Перша",
                "sPrevious": "Попередня",
                "sNext": "Наступна",
                "sLast": "Остання"
            },
            "oAria": {
            "sSortAscending":  ": активувати для сортування стовпців за зростанням",
                "sSortDescending": ": активувати для сортування стовпців за спаданням"
            }
        },
        "pageLength": 5,
        "pagingType": "simple",
        "drawCallback": function( settings ) {
             tSettings = new $.fn.dataTable.Api( settings );
        }
    } );

    $('#user-tasks-table-controls .show-all').click(function(e){
        e.preventDefault;
        var totalRecords = allTasksListTable.fnSettings().fnRecordsTotal();
        allTasksListTable.fnSettings()._iDisplayLength = totalRecords;
        allTasksListTable.fnDraw();

        $('#user-tasks-table_wrapper .dataTables_info, #user-tasks-table_wrapper .dataTables_paginate').hide();
    });

    $('#user-tasks-table-controls .sort-by-user').click(function(e){
        e.preventDefault;
        allTasksListTable.fnSort([ [4,'desc']] );
        $('.sord-opt').removeClass('active');
        $(this).addClass('active');
    });

    $('#user-tasks-table-controls .sort-by-points').click(function(e){
        e.preventDefault;
        allTasksListTable.fnSort([ [2,'desc']] );
        $('.sord-opt').removeClass('active');
        $(this).addClass('active');
    });

    $('#user-tasks-table-controls .sort-by-money').click(function(e){
        e.preventDefault;
        allTasksListTable.fnSort([ [3,'desc']] );
        $('.sord-opt').removeClass('active');
        $(this).addClass('active');
    });
});