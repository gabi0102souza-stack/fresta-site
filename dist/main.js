'use strict';

// Navigation remains visible without JavaScript. Enhancement is limited to mobile.
const navigation = document.querySelector('#navegacao');
const toggle = document.querySelector('.menu-toggle');
const mobile = window.matchMedia('(max-width: 600px)');

if (navigation && toggle) {
  document.body.classList.add('enhanced');
  const setMenu = (open, returnFocus = false) => {
    toggle.setAttribute('aria-expanded', String(open));
    navigation.hidden = mobile.matches && !open;
    if (returnFocus) toggle.focus();
  };
  const syncMenu = () => {
    toggle.hidden = !mobile.matches;
    setMenu(false);
  };
  syncMenu();
  if (mobile.addEventListener) mobile.addEventListener('change', syncMenu);
  else mobile.addListener(syncMenu);
  toggle.addEventListener('click', () => setMenu(toggle.getAttribute('aria-expanded') !== 'true'));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') setMenu(false, true);
  });
  navigation.addEventListener('click', event => {
    const link = event.target.closest('a');
    if (!link) return;
    setMenu(false);
    // Move focus to the destination when the mobile navigation closes.
    if (mobile.matches) {
      const destination = document.querySelector(link.getAttribute('href'));
      if (destination) {
        destination.setAttribute('tabindex', '-1');
        destination.focus({ preventScroll: true });
      }
    }
  });
  document.addEventListener('click', event => {
    if (mobile.matches && !event.target.closest('.site-header')) setMenu(false);
  });
}

if ('IntersectionObserver' in window) {
  const hero = document.querySelector('.hero-actions .button');
  const visit = document.querySelector('.visit');
  let heroVisible = true;
  let visitVisible = false;
  const updateReservation = () => document.body.classList.toggle('show-reserve', !heroVisible && !visitVisible);
  const reservationObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.target === hero) heroVisible = entry.isIntersecting;
      if (entry.target === visit) visitVisible = entry.isIntersecting;
    });
    updateReservation();
  }, { threshold: 0 });
  if (hero) reservationObserver.observe(hero);
  if (visit) reservationObserver.observe(visit);

  const sectionObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      document.querySelectorAll('.navigation a').forEach(link => {
        if (link.hash === `#${entry.target.id}`) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    });
  }, { rootMargin: '-20% 0px -55% 0px' });
  document.querySelectorAll('#inicio, #cozinha, #casa, #visite').forEach(section => sectionObserver.observe(section));
} else {
  document.body.classList.add('show-reserve');
}

const copyButton = document.querySelector('.copy-address');
const copyStatus = document.querySelector('.copy-status');
if (copyButton && navigator.clipboard && window.isSecureContext) {
  copyButton.hidden = false;
  copyButton.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText('Rua Simão Álvares, 447 — Pinheiros, São Paulo');
      copyButton.textContent = 'Endereço copiado';
      if (copyStatus) copyStatus.textContent = 'Endereço copiado para a área de transferência.';
    } catch {
      copyButton.textContent = 'Selecione o endereço acima';
      if (copyStatus) copyStatus.textContent = 'Não foi possível copiar. Selecione o endereço acima para copiar manualmente.';
    }
  });
}
