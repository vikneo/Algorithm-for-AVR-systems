const spanStatus = document.querySelectorAll('.status_def');

spanStatus.forEach(stat => {

    if (stat.id === "3") {
        stat.classList.add("color-status-yellow");
    } else if (stat.id === "2") {
        stat.classList.add("color-status-red");
    } else {
        stat.classList.add("color-status-green");
    };
    return true;
});
