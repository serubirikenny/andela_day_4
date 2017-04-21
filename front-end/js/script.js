$( function(){
	var headerB= $('.header_b');

	$(window).scroll( function(){
			
			var scrollPos=$(window).scrollTop();
			$(".header_b").removeClass("fixed_head");
				
			if(scrollPos>40){
				
				$(".header_b").addClass("fixed_head");
				
			}
			
});
	
	
	
	
	
	
});

	