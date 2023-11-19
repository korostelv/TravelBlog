

$(document).ready(function(){


// **********  Скрипт выпадающего меню при вводе названия городф в ass_post  ************ 
$('#data').hide()
let dataString = $('#data').text();
let cityList = JSON.parse(dataString);

let cityInput = $('#id_city');
let dropDownMenu = $('#ddmenu'); 


cityInput.on('input', function() {
    dropDownMenu.html('');
    dropDownMenu.hide();
    let city = cityInput.val().toLowerCase();
    let count = 0; 

    if (city.length === 0){
        dropDownMenu.hide();
        return;
    }

    for (let i = 0; i < cityList.length; i++) {
        if (cityList[i].toLowerCase().startsWith(city)) { 
            let li = $('<li>').html(cityList[i]);
            dropDownMenu.append(li);
            
            count++;
            if (count === 5) {
                break;
            }
            dropDownMenu.show();
            li.click(function() {
                cityInput.val($(this).html());
                dropDownMenu.hide();
            });
        }
    }
});

cityInput.on('keydown', function(e) {
    if (e.keyCode === 8) { 
        city = cityInput.val().slice(0, -1).toLowerCase();
        let count = 0;
        dropDownMenu.html('');

        for (let i = 0; i < cityList.length; i++) {
            if (cityList[i].toLowerCase().startsWith(city)) {
                let li = $('<li>').html(cityList[i]);
                dropDownMenu.append(li);

                count++;
                if (count === 5) {
                    break;
                }
                dropDownMenu.show();
                li.click(function() {
                    cityInput.val($(this).html());
                    dropDownMenu.hide();
                });

            }
        }
    }
});

//   Показать-скрыть блок комментариев

// let blockComm = $('.block-comments');
// let btnShow = $('#count-comm');
// console.log(blockComm)
// blockComm.hide();

// btnShow.click(function(){
//     alert('111')
// })


















// **************************************************************************************




});


//const swiper = new Swiper('.swiper', {
//    speed: 400,
//    spaceBetween: 100,
//
//    //   autoplay: {
//    //     delay: 2000,
//    //   },
//      loop: false,
//      navigation: {
//        nextEl: '.swiper-button-next',
//        prevEl: '.swiper-button-prev',
//      },
//    //   pagination: {
//    //     el: '.swiper-pagination',
//    //     // type: 'bullets',
//    //     type: 'progressbar',
//    //     // clickable: true,
//    //   },
//
//      mousewheel: {
//        invert: false,
//      },
//      keyboard: {
//        enabled: true,
//        onlyInViewport: false,
//      },
//      scrollbar: {
//        el: '.swiper-scrollbar',
//        draggable: true,
//      },
//      grabCursor: true,
//      slidesPerView: 1,
//      spaceBetween:20,
//      centeredSlides: true,
//    //   direction: 'vertical',
//    zoom: {
//        maxRatio: 5,
//        minRatio:1,
//      },
//  });





