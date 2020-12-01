// const img = document.querySelector('img')
const menu = document.querySelector('.navbar-toggler');
const sideBar = document.querySelector('.sidenav');
const quit = document.querySelector('.close');
const search2 = document.getElementById('side_search');
const sch2CloseBtn = document.querySelectorAll('.finish');
const sch2Div = document.querySelector('.side-search-small');
const search = document.querySelector('#srh');
const sch1Div = document.querySelector('.main-search');

menu.addEventListener('click', () => {
    sideBar.classList.toggle('open');
    quit.style.opacity = '1';

})
console.log(search);

quit.addEventListener('click', () => {
    sideBar.classList.toggle('open');
    
})

search2.addEventListener('click', () => {
  sideBar.classList.toggle('open');
  sch2Div.classList.toggle('open');
})

search.addEventListener('click', () => {
  sch1Div.classList.toggle('open');
})

sch2CloseBtn.forEach((closeBtn) => {
    if(closeBtn.classList.contains('mega')){
      closeBtn.addEventListener('click', () => {
        sch1Div.classList.toggle('open');
      })
    }
    else{
      closeBtn.addEventListener('click', () => {
        sch2Div.classList.toggle('open');
      })
    }
    
})

// Animation of hero text
const fancy = document.querySelector('.carousel-text h1')
const text = fancy.textContent;
fancy.textContent = "";
for(let i = 0; i < text.length; i++){
  fancy.innerHTML += `<span>${text[i]}</span>`;
}

let char = 0;
let timer = setInterval(onTick, 50);

function onTick(){
  const span = fancy.querySelectorAll('span')[char];
  span.classList.add('fade')
  char++
  if(char === text.length){
    complete();
    return;
  }
} 

function complete(){
  clearInterval(timer)
  timer = null;
}




