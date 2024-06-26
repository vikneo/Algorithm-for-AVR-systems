function searchID() {
    let search = document.getElementById('search')[0].value;

    btn_search.onclick = function (event) {
        if (event.which == 1) {
            console.log(`${event.which}; ${search}`);
            form.onsubmit = function () { return true; }
        }
    }

    if (search == 0) {
        console.log('В строке поиска должно быть число больше нуля!');
        form.onsubmit = function () { return false; }
    }

    if (!Number.isInteger(Number(search))) {
        alert('В строке поиска должно быть только целое число!')
        form.onsubmit = function () { return false; }
    }
}

function addToReestr() {
    let answer = confirm('Добавить заявку в Реестр прошивок?')

    if (answer) {
        return true;
    } else {
        return false;
    }
}

function Filter() {
    document.getElementById("filterSet").classList.toggle(".show");
}
// Закрыть раскрывающийся список, если пользователь щелкнет за его пределами.
window.onclick = function (event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName(".dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

function handleClick(e) {
    let folderPathInput = document.getElementById("folderPath");
    let folderPath = folderPathInput.value.trim();
    let currentButton = e.currentTarget;
    let copyfolder = `${folderPath}${currentButton.innerText}\\`

    navigator.clipboard.writeText(copyfolder).then(function (event) {
        const td = document.querySelector('.td');
        const span = document.createElement('span');
        span.classList.add('visit');
        span.textContent = 'Путь скопирован';
        const img = document.createElement('img');
        img.src = 'https://w7.pngwing.com/pngs/225/673/png-transparent-check-mark-tick.png';
        img.width = 30;
        img.alt = 'OK';
        // span.appendChild(img);
        td.appendChild(span);
        console.log(this)

    }, function (err) {
        console.error('Произошла ошибка при копировании текста: ', err);
    });

    setTimeout(() => { location.reload(); }, 5000);
}

function CopyPath() {
    let buttons = document.querySelectorAll('.a-active')

    buttons.forEach(button => {
        button.addEventListener('click', handleClick);
    });
}
