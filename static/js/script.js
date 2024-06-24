(function($) {

    "use strict";

    //  Header sticky
    const headerSticky = function() {
      const header = document.querySelector('#header');
      if (!header) return;      
      const trigHeight = 1;

      window.addEventListener('scroll', function () {
          let tj = window.scrollY;

          if (tj > trigHeight) {
              header.classList.add('sticky');
          } else {
              header.classList.remove('sticky');
          }
      });
    };
    
    
    $(document).ready(function() {
      
      /* Video */
      var $videoSrc;  
        $('.play-btn').click(function() {
          $videoSrc = $(this).data( "src" );
        });
  
        $('#myModal').on('shown.bs.modal', function (e) {
  
        $("#video").attr('src',$videoSrc + "?autoplay=1&amp;modestbranding=1&amp;showinfo=0" ); 
      })
  
      $('#myModal').on('hide.bs.modal', function (e) {
        $("#video").attr('src',$videoSrc); 
      })

      var testimonialSwiper = new Swiper(".testimonial-swiper", {
        spaceBetween: 20,
        pagination: {
            el: ".testimonial-swiper-pagination",
            clickable: true,
          },
        breakpoints: {
          0: {
            slidesPerView: 1,
          },
          800: {
            slidesPerView: 2,
          },
          1400: {
            slidesPerView: 4,
          }
        },
      });
      
      var gallerySwiper = new Swiper(".gallery-swiper", {
        spaceBetween: 20,
        pagination: {
            el: ".gallery-swiper-pagination",
            clickable: true,
          },
        breakpoints: {
          0: {
            slidesPerView: 1,
          },
          800: {
            slidesPerView: 2,
          },
          1400: {
            slidesPerView: 4,
          }
        },
      });

      headerSticky();

    }); // End of a document ready

})(jQuery);