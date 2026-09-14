
(function() {
  "use strict";

  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader.classList.contains('scroll-up-sticky') && !selectHeader.classList.contains('sticky-top') && !selectHeader.classList.contains('fixed-top')) return;
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('scroll', toggleScrolled);
  window.addEventListener('load', toggleScrolled);

  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    mobileNavToggleBtn.classList.toggle('bi-list');
    mobileNavToggleBtn.classList.toggle('bi-x');
  }
  mobileNavToggleBtn.addEventListener('click', mobileNavToogle);

  document.querySelectorAll('#navmenu a').forEach(navmenu => {
    navmenu.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });

  });

  document.querySelectorAll('.navmenu .toggle-dropdown').forEach(navmenu => {
    navmenu.addEventListener('click', function(e) {
      e.preventDefault();
      this.parentNode.classList.toggle('active');
      this.parentNode.nextElementSibling.classList.toggle('dropdown-active');
      e.stopImmediatePropagation();
    });
  });

  let scrollTop = document.querySelector('.scroll-top');

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
  }
  if (scrollTop) {
    scrollTop.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  window.addEventListener('load', toggleScrollTop);
  document.addEventListener('scroll', toggleScrollTop);

  function aosInit() {
    AOS.init({
      duration: 600,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', aosInit);

  const glightbox = GLightbox({
    selector: '.glightbox'
  });

  function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function(swiperElement) {
      let config = JSON.parse(
        swiperElement.querySelector(".swiper-config").innerHTML.trim()
      );

      if (swiperElement.classList.contains("swiper-tab")) {
        initSwiperWithCustomPagination(swiperElement, config);
      } else {
        new Swiper(swiperElement, config);
      }
    });
  }

  window.addEventListener("load", initSwiper);

  new PureCounter();

  document.querySelectorAll('.isotope-layout').forEach(function(isotopeItem) {
    let layout = isotopeItem.getAttribute('data-layout') ?? 'masonry';
    let filter = isotopeItem.getAttribute('data-default-filter') ?? '*';
    let sort = isotopeItem.getAttribute('data-sort') ?? 'original-order';

    let initIsotope;
    imagesLoaded(isotopeItem.querySelector('.isotope-container'), function() {
      initIsotope = new Isotope(isotopeItem.querySelector('.isotope-container'), {
        itemSelector: '.isotope-item',
        layoutMode: layout,
        filter: filter,
        sortBy: sort
      });
    });

    isotopeItem.querySelectorAll('.isotope-filters li').forEach(function(filters) {
      filters.addEventListener('click', function() {
        isotopeItem.querySelector('.isotope-filters .filter-active').classList.remove('filter-active');
        this.classList.add('filter-active');
        initIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        if (typeof aosInit === 'function') {
          aosInit();
        }
      }, false);
    });

  });

  document.querySelectorAll('.faq-item h3, .faq-item .faq-toggle').forEach((faqItem) => {
    faqItem.addEventListener('click', () => {
      faqItem.parentNode.classList.toggle('faq-active');
    });
  });

  let navmenulinks = document.querySelectorAll('.navmenu a');

  function navmenuScrollspy() {
    navmenulinks.forEach(navmenulink => {
      if (!navmenulink.hash) return;
      let section = document.querySelector(navmenulink.hash);
      if (!section) return;
      let position = window.scrollY + 200;
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        document.querySelectorAll('.navmenu a.active').forEach(link => link.classList.remove('active'));
        navmenulink.classList.add('active');
      } else {
        navmenulink.classList.remove('active');
      }
    });
  }
  window.addEventListener('load', navmenuScrollspy);
  document.addEventListener('scroll', navmenuScrollspy);

})();

(function() {
  const root = document.querySelector('#atestimonials');
  if (!root) return;

  const photos = Array.from(root.querySelectorAll('.atestimonial-photo'));
  const slides = Array.from(root.querySelectorAll('.atestimonial-slide'));
  const total = photos.length;
  if (!total) return;

  const rotations = [-7, 6, -5, 8, -6, 5];
  let active = 0;
  let timer = null;

  function render() {
    photos.forEach((img, i) => {
      const isActive = i === active;
      img.style.zIndex = isActive ? total : total - Math.abs(i - active);
      img.style.opacity = isActive ? '1' : '0.35';
      img.style.transform = isActive ?
        'translateY(0) scale(1) rotate(0deg)' :
        'translateY(14px) scale(0.92) rotate(' + rotations[i % rotations.length] + 'deg)';
    });
    slides.forEach((s, i) => s.classList.toggle('is-active', i === active));
  }

  function go(step) {
    active = (active + step + total) % total;
    render();
  }

  function startAutoplay() {
    clearInterval(timer);
    timer = setInterval(() => go(1), 5000);
  }

  root.querySelectorAll('.atestimonial-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      go(btn.dataset.dir === 'prev' ? -1 : 1);
      startAutoplay();
    });
  });

  render();
  startAutoplay();
})();

(function() {
  const table = document.querySelector('.compare-table');
  if (!table) return;

  const mq = window.matchMedia('(max-width: 767px)');

  function reorder() {
    table.querySelectorAll('tr').forEach((row) => {
      const highlight = row.querySelector('.cmp-highlight');
      if (!highlight) return;

      if (mq.matches) {
        if (row.children[1] !== highlight) {
          row.insertBefore(highlight, row.children[1]);
        }
      } else if (row.lastElementChild !== highlight) {
        row.appendChild(highlight);
      }
    });
  }

  reorder();
  mq.addEventListener('change', reorder);
})();
