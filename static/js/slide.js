let index = 0;
let slides = document.querySelector('.slides')
let slideimg = document.querySelectorAll('.slides li');
const slideCount = slideimg.length;
const speed = 1000;
const prev = document.querySelector('.prev');
const next = document.querySelector('.next');
const slideWidth = 80;
makeClone();
initfunction(); // 슬라이드 넓이 및 위치값 초기화 함수
autoSlide();

function makeClone(){
    let cloneSlide_first = slideimg[0].cloneNode(true);
    let cloneSlide_last = slides.lastElementChild.cloneNode(true);
    slides.append(cloneSlide_first);
    slides.insertBefore(cloneSlide_last, slides.firstElementChild);
}

function initfunction() {
    slides.style.width = (slideWidth) * (slideCount+2) + 'vw';
    slides.style.left = -(slideWidth) + 'vw';
}

function autoSlide() { //자동슬라이드 코드
    setInterval(function () {
        if (index <= slideCount -1){
            slides.style.left = -(index + 2) * (slideWidth) + 'vw';
            slides.style.transition = `${0.5}s ease-out`;
        }
        if (index === slideCount - 1) {
            setTimeout(function () {
                slides.style.left = -(slideWidth) + 'vw';
                slides.style.transition = `${0}s ease-out`;
            }, 500);
            index = -1;
        }
        index += 1;
    }, 4000);
}

let timer
next.addEventListener('click', function() { 
    if(!timer){
        timer = setTimeout(() => {
            if (index <= slideCount -1){
                slides.style.left = - (index + 2) * (slideWidth) + 'vw';
                slides.style.transition = `${0.5}s ease-out`;
            }
            if (index === slideCount - 1){ //마지막 슬라이드다.
                setTimeout(function() {
                    slides.style.left = -(slideWidth) + 'vw';
                    slides.style.transition = `${0}s ease-out`;
                }, 500);
                index = -1;
            }
            index += 1;
            timer = null;
        }, 600);
    }
});

prev.addEventListener('click', function(){
    if(!timer){
        timer = setTimeout(() => {
            if (index >=0 ){
                slides.style.left = - index * (slideWidth) + 'vw';
                slides.style.transition = `${0.5}s ease-out`;
            }
            if (index === 0){
                setTimeout(function() {
                    slides.style.left = -slideCount * (slideWidth) + 'vw';
                    slides.style.transition = `${0}s ease-out`;
                }, 500);
                index = slideCount;
            }
            index -= 1;
            timer = null;
        }, 600);
    }
});