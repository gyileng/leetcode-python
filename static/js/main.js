$(document).on("click", "#return-top-bottom>div", function () {
    const to = $(this).attr("data-to");
    const scroll_val = to === 'top' ? 0 : window.document.getElementById("main").clientHeight;
    $('html,body').animate({scrollTop: scroll_val}, 800)
});

$(function () {
    // nav收缩展开
    $('.nav-item>a').on('click', function () {
        if ($(this).next().css('display') == "none") {
            //展开未展开
            $('.nav-item').children('ul').slideUp(300);
            $(this).next('ul').slideDown(300);
            $(this).parent('li').addClass('nav-show').siblings('li').removeClass('nav-show');
        } else {
            //收缩已展开
            $(this).next('ul').slideUp(300);
            $('.nav-item.nav-show').removeClass('nav-show');
        }
    });

    $('.nav-mini>a').on('click', function () {
        if ($(this).next().css('display') == "none") {
            //展开未展开
            $(this).children('ul').slideUp(300);
            $(this).next('ul').slideDown(300);
            $(this).parent('li').addClass('nav-show').siblings('li').removeClass('nav-show');
        } else {
            //收缩已展开
            $(this).next('ul').slideUp(300);
            $('.nav-mini.nav-show').removeClass('nav-show');
        }
    });
});