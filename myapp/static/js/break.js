function showtimerbreak() {
    $(".minutes").html(minutes);
    if (seconds < 10) {
        $(".seconds").html("0" + seconds);
    }
    else {
        $(".seconds").html(seconds);
    }
    console.log(minutes + seconds);
}

function stopbreak() {
    timerFlag = 0;
    pauseFlag = 0;
    minutes = 5;
    seconds = 0;
    showtimerbreak();
    $(".startbreak-stopbreak").html("Start");
    $(".pausebreak-area").hide();
    clearTimeout(t);
}

function startbreak() {
    timerFlag = 1;
    pauseFlag = 0;
    updateTimerbreak();
    $(".startbreak-stopbreak").html("Stop");
    $(".pausebreak-area").show();
    $(".pausebreak").text("Pause");
    $(".startbreak-stopbreak-areabreak").hide();
}

function pausebreak() {
    pauseFlag = 1;
    clearTimeout(t);
    $(".startbreak-stopbreak-areabreak").show();
    $(".pausebreak").html("Resume");
}

function resumebreak() {
    pauseFlag = 0;
    updateTimerbreak();
    $(".pausebreak").html("Pause");
    $(".startbreak-stopbreak-areabreak").hide();
}

function updateTimerbreak() {
    if (minutes == 0 && seconds == 0) {
        console.log();
        // calling route to store date_time
        $.getJSON('/send_datetime', function () { });
        minutes = 5;
        seconds = 0;
        showtimerbreak();
    }
    else if (seconds == 0) {
        minutes -= 1;
        seconds = 59;
        showtimerbreak();
        t = setTimeout(updateTimerbreak, 1000)
    }
    else {
        seconds -= 1;
        showtimerbreak();
        t = setTimeout(updateTimerbreak, 1000)
    }
}