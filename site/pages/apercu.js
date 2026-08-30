/* APERÇU LOCAL uniquement. Traduit les URLs WordPress (/mon-approche) en fichiers
   locaux (02-mon-approche.html) pour pouvoir naviguer hors ligne.
   Ce script n'est PAS à copier dans WordPress. */
(function(){
  var map={
    '/':'01-accueil.html',
    '/mon-approche':'02-mon-approche.html',
    '/accompagnements':'03-accompagnements.html',
    '/atelier-nomade':'04-atelier-nomade.html',
    '/a-propos':'05-a-propos.html',
    '/contact':'06-contact.html',
    '/faq':'07-faq.html',
    '/mentions-legales':'08-mentions-legales.html',
    '/politique-de-confidentialite':'09-politique-de-confidentialite.html',
    '/quiz':'10-quiz.html'
  };
  document.querySelectorAll('.ads a[href^="/"]').forEach(function(a){
    var cible=map[a.getAttribute('href')];
    if(cible){a.setAttribute('href',cible);}
  });
  var ici=location.pathname.split('/').pop();
  document.querySelectorAll('.apercu-bar nav a').forEach(function(a){
    if(a.getAttribute('href')===ici){a.setAttribute('aria-current','page');}
  });
})();
