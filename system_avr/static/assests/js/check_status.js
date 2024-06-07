const spanStatus = document.querySelectorAll('.status_def');

spanStatus.forEach(stat => {
    if (stat.innerText === "В работе") {
        stat.classList.add("color-status-yellow");
        
    } else if (stat.innerText === 'Проверка') {
        stat.classList.add("color-status-red");
    } else {
        stat.classList.add("color-status-green");
    };
    return true;
});
