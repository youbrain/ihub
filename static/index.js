$(document).ready(function(){
	const date = new Date().getDate();
	document.querySelector("a.calendar span").innerHTML = (date + []).length == 1 ? `0${date}` : date;

	let year = (new Date()).getFullYear();
	if (+year > 2021) document.querySelector(".footer__2020").innerHTML = `2021-${year}`;
	
	$('.reviews-carousel').owlCarousel({
	    center:true,
	    items:4,
	    // autoplayHoverPause:true,
	    smartSpeed:200,
	    // autoplay:true,
	    dots:true,
	    loop:true,
	    // animateOut: 'fadeOut',
	    margin:10,
	    responsive:{
	        0:{
	            items:1
	        },
	        800:{
	            items:2
	        },
	        1000:{
	            items:3
	        },
	        1500:{
	            items:3
	        }
	    }
	});
	$('.ivents-carousel').owlCarousel({
	    loop:true,
	    // smartSpeed:3000,
	    dots:false,
	    autoplayHoverPause:true,
	    nav:true,
	    // center: true,
	    margin:10,
	    navText:["<div class='carousel-control-prev'><img src='static/img/angle-left.png'></div>","<div class='carousel-control-next'><img src='static/img/angle-right.png'></div>"],
	    autoplay:true,
	    responsive:{
	        0:{
	            nav:false,
	            items:1
	        },
	        800:{
	            items:2
	        },
	        1000:{
	            nav:true,
	            items:3
	        },
	        1500:{
	            nav:true,
	            items:3
	        }
	    }
	});
	$('.team-carousel').owlCarousel({
	    loop:true,
	    // smartSpeed:2000,
	    dots:false,
	    nav:true,
	    autoplayHoverPause:true,
	    margin:10,
	    navText:["<div class='carousel-control-prev'><img src='static/img/angle-left.png'></div>","<div class='carousel-control-next'><img src='static/img/angle-right.png'></div>"],
	    // autoplay:true,
	    responsive:{
	        0:{
	            nav:false,
	            items:1
	        },
	        800:{
	            nav:true,
	            items:2
	        },
	        1000:{
	            nav:true,
	    		center: true,
	            items:3
	        },
	        1500:{
	    		center: true,
	            nav:true,
	            items:3
	        }
	    }
	});

});