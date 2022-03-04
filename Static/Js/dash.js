//This is the choir button for sending lyrics
let choirSend = document.getElementById('chToggle');
//Close lyrics toggle id
let closeLys = document.getElementById('closeLyricsToggle');

//Opening lyrics part to send
choirSend.addEventListener('click',toggleChoir);

function toggleChoir(){
    console.log('click');

    let darkPart = document.getElementById('theShade');

    //The dark part toggle

    let togVl = false;

    if( togVl == false ){

        //Change the toggle condition
        togVl = true;

        //Change the show

        darkPart.style.display = 'flex';


    }
}

//Closing lyrics part to send
closeLys.addEventListener('click',closeLy);

function closeLy(){

    console.log('click')

    let darkPart = document.getElementById('theShade');

    //The dark part toggle

    let togVl = true;

    if( togVl == true ){

        //Change the toggle condition
        togVl = false;

        //Change the show

        darkPart.style.display = 'none';


    }

}