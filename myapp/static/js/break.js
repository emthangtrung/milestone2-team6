function showbreakTimer() {
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
    pausebreakFlag = 0;
    minutes = 25;
    seconds = 0;
    showbreakTimer();
    $(".startbreak-stopbreak").html("startbreak");
    $(".pausebreak-area").hide();
    clearTimeout(t);
}

function startbreak() {
    timerFlag = 1;
    pausebreakFlag = 0;
    updatebreakTimer();
    $(".startbreak-stopbreak").html("stopbreak");
    $(".pausebreak-area").show();
    $(".pausebreak").text("pausebreak");
    $(".startbreak-stopbreak-area").hide();
}

function pausebreak() {
    pausebreakFlag = 1;
    clearTimeout(t);
    $(".startbreak-stopbreak-area").show();
    $(".pausebreak").html("resumebreak");
}

function resumebreak() {
    pausebreakFlag = 0;
    updatebreakTimer();
    $(".pausebreak").html("pausebreak");
    $(".startbreak-stopbreak-area").hide();
}

function updatebreakTimer() {
    if (minutes == 0 && seconds == 0) {
        console.log("Store to databse and reset");
        // calling route to store date_time
        $.getJSON('/send_datetime', function () { });
        minutes = 25;
        seconds = 0;
        showbreakTimer();
    }
    else if (seconds == 0) {
        minutes -= 1;
        seconds = 59;
        showbreakTimer();
        t = setTimeout(updatebreakTimer, 1000)
    }
    else {
        seconds -= 1;
        showbreakTimer();
        t = setTimeout(updatebreakTimer, 1000)
    }
}