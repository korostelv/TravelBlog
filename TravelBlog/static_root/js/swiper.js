const swiper = new Swiper('.swiper', {
    speed: 400,
    spaceBetween: 100,

    //   autoplay: {
    //     delay: 2000,
    //   },
      loop: false,
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
    //   pagination: {
    //     el: '.swiper-pagination',
    //     // type: 'bullets',
    //     type: 'progressbar',
    //     // clickable: true,
    //   },

      mousewheel: {
        invert: false,
      },
      keyboard: {
        enabled: true,
        onlyInViewport: false,
      },
      scrollbar: {
        el: '.swiper-scrollbar',
        draggable: true,
      },
      grabCursor: true,
      slidesPerView: 1,
      spaceBetween:20,
      centeredSlides: true,
    zoom: {
        maxRatio: 5,
        minRatio:1,
      },
  });


