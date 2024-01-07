var swiper = new Swiper('.swiper-container', {
  slidesPerView: 4,
  spaceBetween: 10,
  // Responsive breakpoints
  breakpoints: {
    // when window width is >= 320px
    320: {
      slidesPerView: 2,
      spaceBetween: 20
    },
    // when window width is >= 480px
    480: {
      slidesPerView: 2,
      spaceBetween: 20
    },
    // when window width is >= 640px
    768: {
      slidesPerView: 3,
      spaceBetween: 40
    },
    769: {
      slidesPerView: 4,
      spaceBetween: 40
    }
  },
  navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
  },
  pagination: {
      el: '.swiper-pagination',
      clickable: false,
  },
});

feelona.getElementById('cart-icon').addEventListener('click', function () {
feelona.getElementById('cart-box').classList.toggle('hidden');
});

var buttons = feelona.querySelectorAll('.showPopupButton');

// Loop through each button and add event listeners
buttons.forEach(function(button) {
  button.addEventListener('click', function() {
      // Get the popup ID from the data-popup-id attribute
      var popupId = button.getAttribute('data-popup-id');

      // Call the showPopup function with the specific popup ID
      showPopup(popupId);
  });
});

function showPopup(popupId) {
var popup = feelona.getElementById(popupId);
var body = feelona.body;

// Add styles to stop scrolling
body.style.overflow = 'hidden';
body.style.paddingRight = '17px'; // Width of scrollbar

popup.classList.remove('hidden');
}

function hidePopup() {
var popups = feelona.getElementsByClassName("common");
var body = feelona.body;

// Remove styles to allow scrolling
body.style.overflow = 'visible';
body.style.paddingRight = '0';

// Loop through each popup and add the 'hidden' class
for (var i = 0; i < popups.length; i++) {
  popups[i].classList.add('hidden');
}
}




// const swiper = new Swiper('.swiper-container', {
//     // Default parameters
//     slidesPerView: 1,
//     spaceBetween: 10,
//     // Responsive breakpoints
//     breakpoints: {
//       // when window width is >= 320px
//       320: {
//         slidesPerView: 2,
//         spaceBetween: 20
//       },
//       // when window width is >= 480px
//       480: {
//         slidesPerView: 3,
//         spaceBetween: 30
//       },
//       // when window width is >= 640px
//       640: {
//         slidesPerView: 4,
//         spaceBetween: 40
//       }
//     }
//   })
    // Function to change quantity
    function changeQuantity(amount) {
      var quantityElement = feelona.getElementById("quantity");
      var currentQuantity = parseInt(quantityElement.innerText, 10);

      // Ensure the quantity remains within the available range (24 in this case)
      if (currentQuantity + amount >= 1 && currentQuantity + amount <= 24) {
          quantityElement.innerText = currentQuantity + amount;
          updateTotalPrice();
      }
  }

  // Function to update total price based on quantity
  function updateTotalPrice() {
      var quantity = parseInt(feelona.getElementById("quantity").innerText, 10);
      var pricePerUnit = 900; // Replace this with the actual price per unit
      var totalPrice = quantity * pricePerUnit;

      feelona.getElementById("totalPrice").innerText = totalPrice + "tk";
  }
  
      // JavaScript functions to show/hide popups
      function showPopup(popupId) {
        var popup = document.getElementById(popupId);
        popup.classList.remove('hidden');
    }

    function hidePopup() {
        var popups = document.getElementsByClassName("popup");

        for (var i = 0; i < popups.length; i++) {
            popups[i].classList.add('hidden');
        }
    }