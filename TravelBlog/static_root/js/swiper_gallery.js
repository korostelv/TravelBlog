window.onload = function() {
  $('.swiper_gallery').show();


const swiperGallery = new Swiper('.swiper_gallery', {

  direction: 'vertical',
  slidesPerView: 2,
  autoplay: {
        delay: 10000,
      },
  loop: true,
    centeredSlides: true,
      effect:'fade',
      fadeEffect :{
        crossFade: true,
      },

});

};