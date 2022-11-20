const calculateWorkingDays = (startDate, endDate, weeklyOffDays, holidays) => {
     
    let count = 0;
    const start = moment(startDate);
    const end = moment(endDate);
    while( start.isBefore(end) ){
        if( !weeklyOffDays.includes(start.day()) && !holidays.includes(start.format('YYYY-MM-DD'))){
        count++;
        }
        start.add(1, 'day');
    }
    return count + 1;
    }
    
function CheckURL() {
    let URL = window.location.href
     
    if(URL.startsWith('http://127.0.0.1') || URL.startsWith('https://mot-automation-stage.herokuapp.com') ){
        $('.stage_warring').removeClass('hide');
    }

}

CheckURL();