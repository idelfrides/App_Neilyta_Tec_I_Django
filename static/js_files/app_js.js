
$(document).ready(function(){
    $('.box').hide();
    $('.scrollToTop').hide();

    $(window).scroll(function(){
        if($(this).scrollTop() > 100){
            $('.scrollToTop').fadeIn();
            $('.box').fadeIn();
        }else{
            $('.crollToTop').fadeOut();
            $('.box').fadeOut();
        }
    });

    $('.crollToTop').click(function(){
        $('html, body').animate({scrollTop: 0}, 3000);
        return false;
    });

});

// 'slow' or value = 800 (quanto maior mais suave é a rolagem)