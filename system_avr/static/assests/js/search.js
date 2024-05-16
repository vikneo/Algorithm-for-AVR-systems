function searchID() {
    let search = document.getElementById('search')[0].value;

    btn_search.onclick = function(event) {
        if (event.which == 1) {
            console.log(`${event.which}; ${search}`);
            form.onsubmit = function () { return true;}
        }
    }

    if (search == 0) {
        console.log('В строке поиска должно быть число больше нуля!');
        form.onsubmit = function () { return false;}
        }
    
    if (!Number.isInteger(Number(search))) {
        alert('В строке поиска должно быть только целое число!')
        form.onsubmit = function () { return false;}
    }
}

function addToReestr () {
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
  window.onclick = function(event) {
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