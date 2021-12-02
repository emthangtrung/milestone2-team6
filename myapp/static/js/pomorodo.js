function showTimer() {
    $(".minutes").html(minutes);
    if (seconds < 10) {
        $(".seconds").html("0" + seconds);
    }
    else {
        $(".seconds").html(seconds);
    }
    console.log(minutes + seconds);
}

function stop() {
    timerFlag = 0;
    pauseFlag = 0;
    minutes = 25;
    seconds = 0;
    showTimer();
    $(".start-stop").html("Start");
    $(".pause-area").hide();
    clearTimeout(t);
}

function start() {
    timerFlag = 1;
    pauseFlag = 0;
    updateTimer();
    $(".start-stop").html("Stop");
    $(".pause-area").show();
    $(".pause").text("Pause");
    $(".start-stop-area").hide();
}

function pause() {
    pauseFlag = 1;
    clearTimeout(t);
    $(".start-stop-area").show();
    $(".pause").html("Resume");
}

function resume() {
    pauseFlag = 0;
    updateTimer();
    $(".pause").html("Pause");
    $(".start-stop-area").hide();
}

function updateTimer() {
    if (minutes == 0 && seconds == 0) {
        console.log();
        // calling route to store date_time
        $.getJSON('/send_datetime', function () { });
        minutes = 25;
        seconds = 0;
        showTimer();
    }
    else if (seconds == 0) {
        minutes -= 1;
        seconds = 59;
        showTimer();
        t = setTimeout(updateTimer, 1000)
    }
    else {
        seconds -= 1;
        showTimer();
        t = setTimeout(updateTimer, 1000)
    }
}