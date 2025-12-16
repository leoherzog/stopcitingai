function redirectToLanguage(lang) {
  // English is at root, other languages in subdirectories
  const path = lang === 'en' ? '/' : '/' + lang + '/';
  window.location.assign(window.location.origin + path);
}

function isDirectNavigation() {
  return !document.referrer || new URL(document.referrer).origin !== window.location.origin;
}

function findBestMatch(tag, available) {
  const normalized = (tag || '').toLowerCase();
  if (!normalized) return null;

  const base = normalized.split('-')[0];
  let baseMatch = null;

  for (const opt of available) {
    const lower = opt.toLowerCase();
    if (lower === normalized) return opt;
    if (lower === base) baseMatch = opt;
  }

  return baseMatch;
}

function checkLanguageState() {
  const thisPageLang = document.documentElement.lang;
  const languageSelect = document.getElementById('language');
  const availableLangs = Array.from(languageSelect.options).map(opt => opt.value);
  const currentLangMatch = findBestMatch(thisPageLang, availableLangs);

  languageSelect.value = currentLangMatch || availableLangs[0];

  // Skip redirect logic if coming from language picker
  const pickerNavigationLang = sessionStorage.getItem('languageRedirectFromPicker');
  if (pickerNavigationLang) {
    sessionStorage.removeItem('languageRedirectFromPicker');
    return;
  }

  // Skip redirect logic if URL has explicit language segment
  const pathSegments = window.location.pathname.split('/').filter(Boolean);
  if (pathSegments.length > 0 && availableLangs.includes(pathSegments[0])) {
    return;
  }

  // Only do language detection for direct navigation
  if (!isDirectNavigation()) return;

  // Try stored preference first
  const preferenceLang = localStorage.getItem('preferredLanguage');
  if (preferenceLang) {
    const matchedPref = findBestMatch(preferenceLang, availableLangs);
    if (matchedPref && matchedPref !== currentLangMatch) {
      redirectToLanguage(matchedPref);
      return;
    }
  }

  // Fall back to browser language
  const browserLangs = navigator.languages?.length ? navigator.languages : [navigator.language];
  for (const lang of browserLangs) {
    const matched = findBestMatch(lang, availableLangs);
    if (matched) {
      if (matched !== currentLangMatch) redirectToLanguage(matched);
      return;
    }
  }
}

document.addEventListener('DOMContentLoaded', function() {
  checkLanguageState();
  document.getElementById('language').addEventListener('change', function() {
    const selectedLang = this.value;
    localStorage.setItem('preferredLanguage', selectedLang);
    sessionStorage.setItem('languageRedirectFromPicker', selectedLang);
    redirectToLanguage(selectedLang);
  });
});
