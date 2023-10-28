$(document).ready(function(){

//   Показать-скрыть блок комментариев

let blockComm = $('.block-comments');
let btnShow = $('#count-comm');
let btnHide = $('#hide-comm');
console.log(blockComm)
blockComm.hide();

btnShow.click(function(){
    blockComm.show();
});

btnHide.click(function(){
    blockComm.hide();
});


});