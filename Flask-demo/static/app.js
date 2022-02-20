const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar__menu');
const navLogo = document.querySelector('#navbar__logo');

// Display Mobile Menu
const mobileMenu = () => {
  menu.classList.toggle('is-active');
  menuLinks.classList.toggle('active');
};

menu.addEventListener('click', mobileMenu);

// Show active menu when scrolling
const highlightMenu = () => {
  const elem = document.querySelector('.highlight');
  const homeMenu = document.querySelector('#home-page');
  const aboutMenu = document.querySelector('#about-page');
  const servicesMenu = document.querySelector('#services-page');
  let scrollPos = window.scrollY;
  // console.log(scrollPos);

  // adds 'highlight' class to my menu items
  if (window.innerWidth > 960 && scrollPos < 600) {
    homeMenu.classList.add('highlight');
    aboutMenu.classList.remove('highlight');
    return;
  } else if (window.innerWidth > 960 && scrollPos < 1400) {
    aboutMenu.classList.add('highlight');
    homeMenu.classList.remove('highlight');
    servicesMenu.classList.remove('highlight');
    return;
  } else if (window.innerWidth > 960 && scrollPos < 2345) {
    servicesMenu.classList.add('highlight');
    aboutMenu.classList.remove('highlight');
    return;
  }

  if ((elem && window.innerWIdth < 960 && scrollPos < 600) || elem) {
    elem.classList.remove('highlight');
  }
};

window.addEventListener('scroll', highlightMenu);
window.addEventListener('click', highlightMenu);

//  Close mobile Menu when clicking on a menu item
const hideMobileMenu = () => {
  const menuBars = document.querySelector('.is-active');
  if (window.innerWidth <= 768 && menuBars) {
    menu.classList.toggle('is-active');
    menuLinks.classList.remove('active');
  }
};

menuLinks.addEventListener('click', hideMobileMenu);
navLogo.addEventListener('click', hideMobileMenu);

// (A) INITIALIZE SHOPPING LIST
items : [], // current shopping list
hform : null, // html add item <form>
hitem : null, // html add item <input> field
hadd : null, // html add item submit button
hlist : null, // html <div> shopping list
init : () => {
  // (A1) GET HTML ELEMENTS
  slist.hform = document.getElementById("shop-form");
  slist.hitem = document.getElementById("shop-item");
  slist.hadd = document.getElementById("shop-add");
  slist.hlist = document.getElementById("shop-list");
 
  // (A2) "ACTIVATE" HTML ADD ITEM FORM
  slist.hitem.setAttribute("autocomplete", "off");
  slist.hform.onsubmit = slist.add;
  slist.hitem.disabled = false;
  slist.hadd.disabled = false;
 
  // (A3) RESTORE PREVIOUS SHOPPING LIST
  if (localStorage.items == undefined) { localStorage.items = "[]"; }
  slist.items = JSON.parse(localStorage.items);
 
  // (A4) DRAW HTML SHOPPING LIST
  slist.draw();
}
window.addEventListener("load", slist.init);