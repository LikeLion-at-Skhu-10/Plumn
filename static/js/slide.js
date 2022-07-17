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

next.addEventListener('click', function() { 
    
    if (index <= slideCount -1){
        console.log(index, slideWidth)
        slides.style.left = - (index + 2) * (slideWidth) + 'vw';
        slides.style.transition = `${0}s ease-out`;
    }
    if (index === slideCount - 1){ //마지막 슬라이드다.
        console.log("마지막 슬라이드")
        setTimeout(function() {
            slides.style.left = -(slideWidth) + 'vw';
            slides.style.transition = `${0}s ease-out`;
        }, 500);
        index = -1;
    }
    index += 1;
    
});

prev.addEventListener('click', function(){
    if (index >=0 ){
        slides.style.left = - index * (slideWidth) + 'vw';
        slides.style.transition = `${0}s ease-out`;
    }
    if (index === 0){
        setTimeout(function() {
            slides.style.left = -slideCount * (slideWidth) + 'vw';
            slides.style.transition = `${0}s ease-out`;
        }, 500);
        index = slideCount;
    }
    index -= 1;
});