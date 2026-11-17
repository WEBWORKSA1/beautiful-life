/* Beautiful.Life — core interactions */
(function(){
  "use strict";
  var root = document.documentElement;
  var BASE = root.getAttribute("data-base") || "./";

  /* ---------- Theme ---------- */
  try{ var t = localStorage.getItem("bl-theme"); if(t) root.setAttribute("data-theme", t); }catch(e){}
  document.addEventListener("click", function(e){
    var b = e.target.closest("[data-theme-toggle]");
    if(!b) return;
    var n = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", n);
    try{ localStorage.setItem("bl-theme", n); }catch(err){}
  });

  /* ---------- Mobile nav ---------- */
  var burger = document.querySelector(".burger"), nav = document.querySelector(".nav");
  if(burger && nav){ burger.addEventListener("click", function(){ var o = nav.classList.toggle("open"); burger.setAttribute("aria-expanded", o); }); }

  /* ---------- Toast ---------- */
  function toast(msg){
    var el = document.querySelector(".toast");
    if(!el){ el = document.createElement("div"); el.className = "toast"; el.setAttribute("role","status"); document.body.appendChild(el); }
    el.textContent = msg; el.classList.add("show");
    clearTimeout(el._t); el._t = setTimeout(function(){ el.classList.remove("show"); }, 3200);
  }
  window.BL = { toast: toast };

  /* ---------- Reveal on scroll ---------- */
  if("IntersectionObserver" in window){
    var io = new IntersectionObserver(function(es){ es.forEach(function(x){ if(x.isIntersecting){ x.target.classList.add("in"); io.unobserve(x.target); } }); }, {threshold:.12});
    document.querySelectorAll(".reveal").forEach(function(el){ io.observe(el); });
  } else document.querySelectorAll(".reveal").forEach(function(el){ el.classList.add("in"); });

  /* ---------- Back to top ---------- */
  var top = document.querySelector(".totop");
  if(top){ window.addEventListener("scroll", function(){ top.classList.toggle("show", window.scrollY > 700); }, {passive:true});
    top.addEventListener("click", function(){ window.scrollTo({top:0,behavior:"smooth"}); }); }

  /* ---------- Cookie consent ---------- */
  var ck = document.querySelector(".cookie");
  try{
    if(ck && !localStorage.getItem("bl-consent")) setTimeout(function(){ ck.classList.add("show"); }, 900);
  }catch(e){}
  document.addEventListener("click", function(e){
    var b = e.target.closest("[data-consent]"); if(!b) return;
    try{ localStorage.setItem("bl-consent", b.getAttribute("data-consent")); }catch(err){}
    if(ck) ck.classList.remove("show");
    if(b.getAttribute("data-consent") === "essential"){ (window.adsbygoogle = window.adsbygoogle || []).requestNonPersonalizedAds = 1; }
  });

  /* ---------- Daily quote & action (deterministic by date) ---------- */
  var QUOTES = [
    ["The happiness of your life depends upon the quality of your thoughts.","Marcus Aurelius"],
    ["It is not that we have a short time to live, but that we waste a lot of it.","Seneca"],
    ["Go confidently in the direction of your dreams. Live the life you have imagined.","Henry David Thoreau"],
    ["Happiness is the meaning and the purpose of life, the whole aim and end of human existence.","Aristotle"],
    ["The journey of a thousand miles begins with one step.","Lao Tzu"],
    ["Adopt the pace of nature: her secret is patience.","Ralph Waldo Emerson"],
    ["We are what we repeatedly do.","Will Durant (summarising Aristotle)"],
    ["Keep your face always toward the sunshine, and shadows will fall behind you.","Walt Whitman"],
    ["Nothing is worth more than this day.","Johann Wolfgang von Goethe"],
    ["What you do makes a difference, and you have to decide what kind of difference you want to make.","Jane Goodall"],
    ["Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.","Attributed to the Buddha"],
    ["Simplicity is the ultimate sophistication.","Attributed to Leonardo da Vinci"],
    ["Wealth consists not in having great possessions, but in having few wants.","Epictetus"],
    ["Be kind, for everyone you meet is fighting a hard battle.","Attributed to Ian Maclaren"],
    ["Look deep into nature, and then you will understand everything better.","Albert Einstein"],
    ["To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.","Attributed to Ralph Waldo Emerson"],
    ["The best way to cheer yourself is to try to cheer someone else up.","Mark Twain"],
    ["Begin at once to live, and count each separate day as a separate life.","Seneca"],
    ["Joy in looking and comprehending is nature's most beautiful gift.","Albert Einstein"],
    ["Very little is needed to make a happy life; it is all within yourself.","Marcus Aurelius"],
    ["Gratitude is not only the greatest of virtues, but the parent of all the others.","Cicero"]
  ];
  var ACTIONS = [
    "Send a two-line thank-you message to someone who helped you this year.",
    "Take a 10-minute walk outside without your phone.",
    "Write down three things that went well today — and why.",
    "Drink a full glass of water before your first coffee.",
    "Clear one surface in your home completely.",
    "Move your bedtime 20 minutes earlier tonight.",
    "Call a friend instead of texting them.",
    "Check one subscription you no longer use — and cancel it.",
    "Do 4 rounds of box breathing (4 in, 4 hold, 4 out, 4 hold).",
    "Learn one new word, fact or skill and teach it to someone.",
    "Eat one meal today slowly, without a screen.",
    "Put 1% of today's income into a savings pot.",
    "Compliment a stranger sincerely.",
    "Spend 15 minutes on a hobby you've neglected.",
    "Write a one-sentence vision for your life five years from now.",
    "Stretch for five minutes before bed.",
    "Donate one item you haven't used in a year.",
    "Plan a micro-adventure for this weekend.",
    "Notice and name five beautiful things around you.",
    "Forgive one small grudge — let it go on paper.",
    "Ask someone a question you've never asked them before."
  ];
  var d = new Date(); var dayN = Math.floor((d - new Date(d.getFullYear(),0,0)) / 864e5);
  var qEl = document.querySelector("[data-quote]");
  if(qEl){ var q = QUOTES[dayN % QUOTES.length]; qEl.querySelector(".q").textContent = "“" + q[0] + "”"; qEl.querySelector(".a").textContent = "— " + q[1]; }
  document.querySelectorAll("[data-action]").forEach(function(el){ el.textContent = ACTIONS[dayN % ACTIONS.length]; });
  document.querySelectorAll("[data-today]").forEach(function(el){ el.textContent = d.toLocaleDateString(undefined,{weekday:"long",month:"long",day:"numeric"}); });
  document.querySelectorAll("[data-year]").forEach(function(el){ el.textContent = d.getFullYear(); });

  /* ---------- Secure form relay (address never rendered) ---------- */
  var K = [119,100,96,116,107,119,109,115,96,51,67,99,104,103,105,109,44,96,107,104]; // encoded
  function relay(){ var s = ""; for(var i=0;i<K.length;i++) s += String.fromCharCode(K[i] ^ (i % 7)); return "https://formsubmit.co/ajax/" + s; }

  document.querySelectorAll("form[data-form]").forEach(function(f){
    f.addEventListener("submit", function(e){
      e.preventDefault();
      var kind = f.getAttribute("data-form");
      if(f.querySelector(".hp input") && f.querySelector(".hp input").value) return; // bot
      var msg = f.querySelector(".form-msg");
      var btn = f.querySelector("[type=submit]");
      var data = {};
      new FormData(f).forEach(function(v,k){ if(k === "_hp") return; data[k] = data[k] ? data[k] + ", " + v : v; });
      data._subject = "Beautiful.Life — " + (f.getAttribute("data-subject") || kind) + " submission";
      data._template = "table"; data._captcha = "false";
      data.form_type = kind; data.page = location.href;
      if(btn){ btn.disabled = true; btn._t = btn.textContent; btn.textContent = "Sending…"; }
      fetch(relay(), {method:"POST", headers:{"Content-Type":"application/json","Accept":"application/json"}, body: JSON.stringify(data)})
        .then(function(r){ return r.json().catch(function(){ return {}; }); })
        .then(function(){ done(true); })
        .catch(function(){ done(false); });
      function done(ok){
        if(btn){ btn.disabled = false; btn.textContent = btn._t; }
        if(msg){ msg.className = "form-msg " + (ok ? "ok" : "err"); msg.textContent = ok ? (f.getAttribute("data-ok") || "Thank you! We’ve received your submission and will be in touch soon.") : "Something went wrong — please try again in a moment."; }
        if(ok){
          try{ var c = JSON.parse(localStorage.getItem("bl-leads") || "0"); localStorage.setItem("bl-leads", c + 1); }catch(err){}
          if(kind === "blueprint"){ try{ localStorage.setItem("bl-blueprint","1"); }catch(err){} setTimeout(function(){ location.href = BASE + "blueprint.html#unlocked"; }, 900); }
          f.reset(); toast("Submitted — thank you!");
          if(f._stepReset) f._stepReset();
        }
      }
    });
  });

  /* ---------- Multi-step forms ---------- */
  document.querySelectorAll("[data-steps]").forEach(function(f){
    var steps = f.querySelectorAll(".step"), bars = f.querySelectorAll(".steps span"), i = 0;
    function show(n){ i = n; steps.forEach(function(s,k){ s.classList.toggle("on", k === n); }); bars.forEach(function(b,k){ b.classList.toggle("on", k <= n); }); }
    f.addEventListener("click", function(e){
      if(e.target.closest("[data-next]")){
        e.preventDefault();
        var req = steps[i].querySelectorAll("[required]"), ok = true;
        req.forEach(function(r){
          if(r.type === "radio"){ if(!f.querySelector("input[name='"+r.name+"']:checked")) ok = false; }
          else if(!r.checkValidity()){ ok = false; r.reportValidity(); }
        });
        if(!ok){ toast("Please complete this step first."); return; }
        show(Math.min(i+1, steps.length-1));
      }
      if(e.target.closest("[data-prev]")){ e.preventDefault(); show(Math.max(i-1,0)); }
    });
    f._stepReset = function(){ show(0); };
    show(0);
  });

  /* ---------- Modal (lead magnet exit-intent, once per 7 days) ---------- */
  var modal = document.querySelector(".modal");
  function openModal(){ if(modal){ modal.classList.add("show"); try{ localStorage.setItem("bl-modal", Date.now()); }catch(e){} } }
  document.addEventListener("click", function(e){
    if(e.target.closest("[data-open-modal]")){ e.preventDefault(); openModal(); }
    if(e.target.closest(".modal .x") || e.target === modal){ modal.classList.remove("show"); }
  });
  try{
    var last = +localStorage.getItem("bl-modal") || 0, unlocked = localStorage.getItem("bl-blueprint");
    if(modal && !unlocked && Date.now() - last > 7*864e5){
      var armed = false;
      setTimeout(function(){ armed = true; }, 15000);
      document.addEventListener("mouseout", function h(e){ if(armed && !e.relatedTarget && e.clientY < 10){ openModal(); document.removeEventListener("mouseout", h); } });
    }
  }catch(e){}

  /* ---------- Share ---------- */
  document.addEventListener("click", function(e){
    var b = e.target.closest("[data-share]"); if(!b) return;
    e.preventDefault();
    var u = encodeURIComponent(location.href), t = encodeURIComponent(document.title), w = b.getAttribute("data-share"), url;
    if(w === "copy"){ (navigator.clipboard ? navigator.clipboard.writeText(location.href) : Promise.reject()).then(function(){ toast("Link copied"); }, function(){ toast(location.href); }); return; }
    if(w === "native" && navigator.share){ navigator.share({title:document.title,url:location.href}); return; }
    url = {x:"https://twitter.com/intent/tweet?url="+u+"&text="+t, fb:"https://www.facebook.com/sharer/sharer.php?u="+u, li:"https://www.linkedin.com/sharing/share-offsite/?url="+u, wa:"https://wa.me/?text="+t+"%20"+u, pin:"https://pinterest.com/pin/create/button/?url="+u+"&description="+t}[w];
    if(url) window.open(url, "_blank", "noopener,width=640,height=560");
  });

  /* ---------- Reading progress ---------- */
  var rp = document.querySelector(".read-progress");
  if(rp){ window.addEventListener("scroll", function(){ var h = document.documentElement; rp.style.width = (h.scrollTop / (h.scrollHeight - h.clientHeight) * 100) + "%"; }, {passive:true}); }

  /* ---------- Filter + search for card lists ---------- */
  document.querySelectorAll("[data-filter-group]").forEach(function(g){
    var list = document.querySelector(g.getAttribute("data-filter-group"));
    var search = document.querySelector("[data-search='" + g.getAttribute("data-filter-group") + "']");
    var cur = "all";
    function apply(){
      var q = search ? search.value.toLowerCase().trim() : "";
      list.querySelectorAll("[data-cat]").forEach(function(c){
        var okC = cur === "all" || c.getAttribute("data-cat") === cur;
        var okQ = !q || c.textContent.toLowerCase().indexOf(q) > -1;
        c.style.display = okC && okQ ? "" : "none";
      });
    }
    g.addEventListener("click", function(e){ var b = e.target.closest("button"); if(!b) return; g.querySelectorAll("button").forEach(function(x){ x.classList.remove("on"); }); b.classList.add("on"); cur = b.getAttribute("data-f"); apply(); });
    if(search) search.addEventListener("input", apply);
    var h = location.hash.replace("#",""); if(h){ var hb = g.querySelector("[data-f='"+h+"']"); if(hb) hb.click(); }
  });

  /* ---------- Good-news feed (auto-updated JSON) ---------- */
  function esc(s){ return String(s || "").replace(/[&<>"']/g, function(c){ return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]; }); }
  document.querySelectorAll("[data-news]").forEach(function(box){
    var limit = +box.getAttribute("data-news") || 9;
    fetch(BASE + "data/news.json", {cache:"no-cache"}).then(function(r){ return r.json(); }).then(function(j){
      var items = (j.items || []).slice(0, limit);
      var up = document.querySelector("[data-news-updated]"); if(up && j.updated) up.textContent = new Date(j.updated).toLocaleString();
      box.innerHTML = items.map(function(it){
        return '<article class="card hov news-item reveal in" data-cat="'+esc(it.cat||"world")+'"><span class="src">'+esc(it.source)+'</span><h3><a href="'+esc(it.link)+'" target="_blank" rel="noopener nofollow">'+esc(it.title)+'</a></h3><p>'+esc(it.summary)+'</p><span class="meta">'+esc(it.date ? new Date(it.date).toLocaleDateString() : "")+'</span></article>';
      }).join("") || "<p>Fresh stories are on their way.</p>";
    }).catch(function(){ box.innerHTML = "<p>Fresh stories are on their way.</p>"; });
  });

  /* ---------- Videos (auto-updated JSON, click-to-load for speed & privacy) ---------- */
  document.querySelectorAll("[data-videos]").forEach(function(box){
    var limit = +box.getAttribute("data-videos") || 6;
    fetch(BASE + "data/videos.json", {cache:"no-cache"}).then(function(r){ return r.json(); }).then(function(j){
      var vids = (j.items || []).slice(0, limit);
      box.innerHTML = vids.map(function(v){
        return '<div class="reveal in" data-cat="'+esc(v.cat||"mind")+'"><div class="vid" data-yt="'+esc(v.id)+'" role="button" tabindex="0" aria-label="Play: '+esc(v.title)+'"><img loading="lazy" alt="" src="https://i.ytimg.com/vi/'+esc(v.id)+'/hqdefault.jpg"><div class="play"><span>&#9654;</span></div></div><h3 style="font-size:1.05rem;margin-top:12px">'+esc(v.title)+'</h3><p class="meta">'+esc(v.channel||"")+'</p></div>';
      }).join("");
      box.querySelectorAll(".vid img").forEach(function(img){
        img.addEventListener("load", function(){ if(img.naturalWidth === 120){ var c = img.closest("[data-cat]"); if(c) c.remove(); } }); // drop unavailable videos
      });
    }).catch(function(){});
    function play(v){ var id = v.getAttribute("data-yt"); v.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&rel=0" title="Video" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'; }
    box.addEventListener("click", function(e){ var v = e.target.closest(".vid[data-yt]"); if(v && !v.querySelector("iframe")) play(v); });
    box.addEventListener("keydown", function(e){ if(e.key === "Enter"){ var v = e.target.closest(".vid[data-yt]"); if(v) play(v); } });
  });

  /* ---------- Live counters ---------- */
  document.querySelectorAll("[data-count]").forEach(function(el){
    var end = +el.getAttribute("data-count"), dur = 1400, st = null;
    function step(ts){ if(!st) st = ts; var p = Math.min((ts - st)/dur, 1); el.textContent = Math.floor(end * (1 - Math.pow(1-p,3))).toLocaleString() + (el.getAttribute("data-suffix") || ""); if(p < 1) requestAnimationFrame(step); }
    if("IntersectionObserver" in window){ var o = new IntersectionObserver(function(es){ if(es[0].isIntersecting){ requestAnimationFrame(step); o.disconnect(); } }); o.observe(el); } else el.textContent = end.toLocaleString();
  });

  /* ---------- Donation tiers ---------- */
  document.querySelectorAll(".tiers").forEach(function(t){
    t.addEventListener("click", function(e){
      var c = e.target.closest(".tier"); if(!c) return;
      t.querySelectorAll(".tier").forEach(function(x){ x.classList.remove("on"); }); c.classList.add("on");
      var amt = document.querySelector("#donation-amount"); if(amt){ amt.value = c.getAttribute("data-amt"); }
    });
  });

  /* ---------- Payment links from config (optional) ---------- */
  var CFG = window.BL_CONFIG || {};
  document.querySelectorAll("[data-pay]").forEach(function(a){
    var u = CFG[a.getAttribute("data-pay")];
    if(u){ a.href = u; a.target = "_blank"; a.rel = "noopener"; a.hidden = false; } else a.hidden = true;
  });
})();
