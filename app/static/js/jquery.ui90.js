$(document).ready(function(){


	// 字体调整
	$('.fontSize span').click(function(){
		var $p_size = $('.post_content p').css('font-size');
		var textFontSize = parseFloat($p_size,10);
		var $cName = $(this).attr('id');
		if($cName == "fontBig"){
			if(textFontSize <= 20){
				textFontSize += 2;
			}
		}else if($cName == "fontSmall"){
			if(textFontSize >= 14){
				textFontSize -= 2;
			}
		}
		$('.post_content p').css('font-size',textFontSize + 'px');
	});

	
	//搜索
	
	// $(document).click(function() {
	// 	if($('#search').is(':visible')){ 
	// 		$('#search').slideUp();
	// 	}
	// });
	// $("#search").click(function(event) {
	// 	event.stopPropagation();
	// });
	// $('#J_search_toggle').click(function(){ 
	// 	if($('#search').is(':visible')){ 
	// 		$('#search').slideUp();
	// 	}else{ 
	// 		$('#search').slideDown();
	// 	}
	// 	event.stopPropagation();
	// })
	// 
	
	
	//mini 导航
	$('#J_mobileMenu_toggle').click(function(){ 
		if($('#mobileMenu').is(':visible')){ 
			$('#mobileMenu').slideUp();
		}else{ 
			$('#mobileMenu').slideDown();
		}
	})
	


	// 滑动到顶部
	$(window).scroll(function () {
		if ($(this).scrollTop() > 600) {
			$('#backTop').fadeIn();
		} else {
			$('#backTop').fadeOut();
		}
	});
	$('#backTop a').click(function () {
		$('body,html').animate({
			scrollTop: 0
		}, 400);
		return false;
	});
	
	
//all jquery end
});
