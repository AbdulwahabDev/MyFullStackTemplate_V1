var start = moment();
var end = moment().add(1, "days");

function cb(start, end) {
    // debugger
    // $('#kt_daterangepicker_4').val( end.format('YYYY/MM/DD') + ' - ' + start.format('YYYY/MM/DD'));
    // $("#kt_daterangepicker_4").html(start.format("MMMM D, YYYY") + " - " + end.format("MMMM D, YYYY"));
}

 

$("#kt_daterangepicker_4").daterangepicker({
    startDate: start,
    endDate: end,
    ranges: {
    "اليوم": [moment(), moment().add(1, "days")],
    "اليوم السابق": [moment().subtract(1, "days"), moment()],
    "أخر 7 أيام": [moment().subtract(6, "days"), moment()],
    "أخر 30 يوم": [moment().subtract(29, "days"), moment()],
    "هذا الشهر": [moment().startOf("month"), moment().endOf("month")],
    "الشهر السابق": [moment().subtract(1, "month").startOf("month"), moment().subtract(1, "month").endOf("month")]
    },
    locale : {
        direction: 'ltr',
        format: 'YYYY-MM-DD',
        // format: moment.localeData().longDateFormat('L'),
        separator: ' ~ ',
        applyLabel: 'تطبيق',
        cancelLabel: 'تراجع',
        weekLabel: 'W',
        customRangeLabel: ' تاريخ مخصص',
        daysOfWeek: moment.weekdaysMin(),
        monthNames: moment.monthsShort(),
        firstDay: moment.localeData().firstDayOfWeek()
    }
}, cb);

// cb(start, end);