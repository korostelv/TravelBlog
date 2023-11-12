

$(document).ready(function(){
// Лайк-дизлайк без перезагрузки страницы
    let likeBtn = $('.like');
    let dislikeBtn = $('.dislike');

    likeBtn.click(function(event){
        event.preventDefault();

        let postID = $(this).attr('data-post-id');

        $.ajax({
            type: "POST",
            url: "/likes/" + postID + "/",
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}',
                post_id: postID
            },
            success: function(response) {
                if (response.rating !== undefined) {
                    $('.rating-count').html('<b>Рейтинг статьи: </b><span style="color: #006633;">'+response.rating+'</span>')
                }
                if (response.message !== undefined) {
                    $('.message-rating').text(response.message)
                }
            }
        });
    });

    dislikeBtn.click(function(event){
        event.preventDefault();

        let postID = $(this).attr('data-post-id');

        $.ajax({
            type: "POST",
            url: "/dislikes/" + postID + "/",
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}',
                post_id: postID
            },
            success: function(response) {
                if (response.rating !== undefined) {
                    $('.rating-count').html('<b>Рейтинг статьи: </b><span style="color: #006633;">'+response.rating+'</span>')
                }
                if (response.message !== undefined) {
                    $('.message-rating').text(response.message)
                }
            }
        });
    });



    
});