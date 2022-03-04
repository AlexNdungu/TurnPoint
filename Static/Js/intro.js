let navBar = document.querySelector('.bagger');
let barX = false;

navBar.addEventListener('click', () => {
    if(!barX){
        navBar.classList.remove('open')
        barX = true;
    }
    else {
        navBar.classList.add('open')
        barX = false;
    }

});