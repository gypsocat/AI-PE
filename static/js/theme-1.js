(function ($) {
    'use strict';

  //Header Search
  if($('.search-box-outer').length) {
    $('.search-box-outer').on('click', function() {
        $('body').addClass('search-active');
    });
    $('.close-search').on('click', function() {
        $('body').removeClass('search-active');
    });
 }

    // Mobile Menu
    $('.mobile-menu nav').meanmenu({
        meanScreenWidth: "991",
        meanMenuContainer: ".mobile-menu",
        meanMenuOpen: "<span></span> <span></span> <span></span>",
        onePage: false,
    });


    // sticky
    var wind = $(window);
    var sticky = $('#sticky-header');
    wind.on('scroll', function () {
        var scroll = wind.scrollTop();
        if (scroll < 100) {
            sticky.removeClass('sticky');
        } else {
            sticky.addClass('sticky');
        }
    });

  // Venubox
    $('.venobox').venobox({
        numeratio: true,
        infinigall: true

    });
    

          // Preloader
  $(document).ready(function() {
    setTimeout(function(){
        $('.loader_bg').fadeToggle();
    }, 1000);

   });


   // counterUp
   $('.counter').counterUp({
    delay: 35,
    time: 2500

  });

     //======< scrollcue js >======
    $(function(){
          scrollCue.init({
          duration : 1500,
          interval : -0.7,
          percentage : 0.90,
          smartSpeed: 500 
          
        })
    });

    // Case Study Active

    $('.hero-slide').owlCarousel({
        loop: true,
        autoplay: true,
        smartSpeed: 1500,
        autoplayTimeout: 1500,
        dots: true,
        nav: false,
        margin: 0,
        navText: [""],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            768: {
                items: 1
            },
            992: {
                items: 1
            },
            1200: {
                items: 1
            },
            1920: {
                items: 1
            }
        }
    })


    $('.testimonial').owlCarousel({
        loop: true,
        autoplay: true,
        smartSpeed: 1500,
        autoplayTimeout: 1500,
        dots: true,
        nav: false,
        margin: 30,
        dotsEach:true,
        navText: [""],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            768: {
                items: 1
            },
            992: {
                items: 1
            },
            1200: {
                items: 1
            },
            1920: {
                items: 1
            }
        }
    })


    $('.brand').owlCarousel({
        loop: true,
        autoplay: true,
        smartSpeed: 1500,
        autoplayTimeout: 1500,
        dots: false,
        nav: true,
        margin: 30,
        navText: [""],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 3
            },
            1200: {
                items: 4
            },
            1920: {
                items: 4
            }
        }
    })


    $('.blog').owlCarousel({
        loop: true,
        autoplay: true,
        smartSpeed: 1500,
        autoplayTimeout: 1500,
        dots: false,
        nav: true,
        margin: 30,
        navText: ["<i class='fas fa-arrow-left'></i>" , "<i class='fas fa-arrow-right'></i>"],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 2
            },
            1200: {
                items: 3
            },
            1920: {
                items: 3
            }
        }
    })


    // Dark Js
  
    $(".toggle-switch").on("click", function(event){
      $("body").toggleClass("dark");
    });



 //======< sign Up >======
// Get the modal
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}


  // scroll up
    if($('.prgoress_indicator path').length){
        var progressPath = document.querySelector('.prgoress_indicator path');
        var pathLength = progressPath.getTotalLength();
        progressPath.style.transition = progressPath.style.WebkitTransition = 'none';
        progressPath.style.strokeDasharray = pathLength + ' ' + pathLength;
        progressPath.style.strokeDashoffset = pathLength;
        progressPath.getBoundingClientRect();
        progressPath.style.transition = progressPath.style.WebkitTransition = 'stroke-dashoffset 10ms linear';
        var updateProgress = function () {
          var scroll = $(window).scrollTop();
          var height = $(document).height() - $(window).height();
          var progress = pathLength - (scroll * pathLength / height);
          progressPath.style.strokeDashoffset = progress;
        }
        updateProgress();
        $(window).on('scroll', updateProgress);
        var offset = 250;
        var duration = 550;
        jQuery(window).on('scroll', function () {
          if (jQuery(this).scrollTop() > offset) {
            jQuery('.prgoress_indicator').addClass('active-progress');
          } else {
            jQuery('.prgoress_indicator').removeClass('active-progress');
          }
        });
        jQuery('.prgoress_indicator').on('click', function (event) {
          event.preventDefault();
          jQuery('html, body').animate({ scrollTop: 0 }, duration);
          return false;
        });
    }

        /*  Cart Plus Minus Button
    /*----------------------------------------*/
    
    $('.ctnbutton').on('click', function () {
        var $button = $(this);
        var oldValue = $button.parent().find('input').val();
        if ($button.hasClass('inc')) {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            // Don't allow decrementing below zero
            if (oldValue > 1) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 1;
            }
        }
        $button.parent().find('input').val(newVal);
    });


     //=====< mouse script >====

  

     //=====< barfiller script >====
     $('#bar1').barfiller({
        duration: 7000
    });
    $('#bar2').barfiller({
        duration: 7000
    });
    $('#bar3').barfiller({
        duration: 7000
    });

       // Sidebar
        
       "use strict";
       jQuery(document).ready(function () {
           $('.nav-btn a').on('click', function () {
               $('.xs-sidebar-group').addClass('isActive');
           });
   
           $('.xs-overlay').on('click', function () {
               $('.xs-sidebar-group').removeClass('isActive');
           });
           
           $('.close-side-widget').on('click', function () {
               $('.xs-sidebar-group').removeClass('isActive');
           });
       });


       $(document).ready(function () {
        const tabs = document.querySelectorAll(".tab-btn button");
        const all_content = document.querySelectorAll(".tab-contents");
    
        tabs.forEach((tab, index) => {
          tab.addEventListener("click", () => {
            tabs.forEach((tab) => {
              tab.classList.remove("active");
            });
            tab.classList.add("active");
    
            all_content.forEach((content) => {
              content.classList.remove("active");
            });
            all_content[index].classList.add("active");
          });
        });
      });
    


   //Why choose us tabs
   const tabs= document.querySelectorAll('.why-choose-us-tab');
   const all_content= document.querySelectorAll('.tabs-content1')

   tabs.forEach((tab, index)=>{
       tab.addEventListener('click', ()=>{
           tabs.forEach(tab=>{tab.classList.remove('active')});
           tab.classList.add('active');

           all_content.forEach(content=>{content.classList.remove('active')});
           all_content[index].classList.add('active');
       })
   })

 //cart//

 $(function() {

    "use strict"
    
    var init = "(0)";
    var counters = (0);
  
    // Initial Cart
    $(".counters").html(init);
    
    // Add Items To Basket
    function addToBasket() {
      counters++;
      $(".counters").html(counters).animate({
        'opacity' : '0'
      },300, function() {
        $(".counters").delay(300).animate({
          'opacity' : '1'
        })
      })
    }
  
    // Add To Basket Animation
    $("cart-button").on("click", function() {
      addToBasket(); $(this).parent().parent().find(".product_overlay").css({
        'transform': ' translateY(0px)',
        'opacity': '1',
        'transition': 'all ease-in-out .45s'
      }).delay(1500).queue(function() {
        $(this).css({
          'transform': 'translateY(-500px)',
          'opacity': '0',
          'transition': 'all ease-in-out .45s'
        }).dequeue();
      });
    });
  });




})(jQuery);

//Dark & Light Js /

const button = document.querySelector(".switch");
(function ($) {
  let onpageLoad = localStorage.getItem("theme");
  if (onpageLoad === "darkmode") {
    document.body.classList.add("darkmode");
  }
})();

function themeToggle($) {
  let element = document.body;
  element.classList.toggle("darkmode");

  let theme = localStorage.getItem("theme");
  if (theme && theme === "darkmode") {
    localStorage.setItem("theme", "");
  } else {
    localStorage.setItem("theme", "darkmode");
  }
}
