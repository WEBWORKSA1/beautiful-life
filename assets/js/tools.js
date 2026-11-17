/* Beautiful.Life — interactive tools (all data stays in the visitor's browser) */
(function(){
  "use strict";
  function $(s,c){ return (c||document).querySelector(s); }
  function store(k,v){ try{ if(v === undefined) return JSON.parse(localStorage.getItem(k)); localStorage.setItem(k, JSON.stringify(v)); }catch(e){ return null; } }
  function esc(s){ return String(s).replace(/[&<>"']/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c];}); }
  var BASE = document.documentElement.getAttribute("data-base") || "./";

  /* ===== Wheel of Life ===== */
  var wheel = $("[data-tool=wheel]");
  if(wheel){
    var AREAS = ["Mind","Body","Money","Love","Home","Purpose","Adventure","Growth"];
    var LINKS = {Mind:"mind",Body:"body",Money:"money",Love:"love",Home:"home",Purpose:"purpose",Adventure:"adventure",Growth:"growth"};
    var saved = store("bl-wheel") || {};
    var box = $(".sliders", wheel);
    box.innerHTML = AREAS.map(function(a){ var v = saved[a] || 5; return '<div class="range-row"><label for="w-'+a+'">'+a+'</label><input type="range" min="1" max="10" value="'+v+'" id="w-'+a+'" data-a="'+a+'"><output>'+v+'</output></div>'; }).join("");
    var cv = $("canvas", wheel), ctx = cv.getContext("2d");
    function draw(){
      var vals = {}; box.querySelectorAll("input").forEach(function(i){ vals[i.getAttribute("data-a")] = +i.value; i.nextElementSibling.textContent = i.value; });
      store("bl-wheel", vals);
      var W = cv.width, H = cv.height, cx = W/2, cy = H/2, R = Math.min(W,H)/2 - 78, n = AREAS.length;
      var dark = document.documentElement.getAttribute("data-theme") === "dark";
      ctx.clearRect(0,0,W,H);
      ctx.strokeStyle = dark ? "#3a2f45" : "#e7dfd3"; ctx.lineWidth = 1;
      for(var r=1;r<=10;r++){ ctx.beginPath(); for(var k=0;k<=n;k++){ var an = -Math.PI/2 + k*2*Math.PI/n, x = cx + Math.cos(an)*R*r/10, y = cy + Math.sin(an)*R*r/10; k ? ctx.lineTo(x,y) : ctx.moveTo(x,y); } ctx.stroke(); }
      var g = ctx.createLinearGradient(0,0,W,H); g.addColorStop(0,"rgba(107,63,160,.55)"); g.addColorStop(1,"rgba(224,96,126,.55)");
      ctx.beginPath();
      AREAS.forEach(function(a,k){ var an = -Math.PI/2 + k*2*Math.PI/n, x = cx + Math.cos(an)*R*vals[a]/10, y = cy + Math.sin(an)*R*vals[a]/10; k ? ctx.lineTo(x,y) : ctx.moveTo(x,y); });
      ctx.closePath(); ctx.fillStyle = g; ctx.fill(); ctx.strokeStyle = "#e0607e"; ctx.lineWidth = 2.5; ctx.stroke();
      ctx.fillStyle = dark ? "#f4eef8" : "#1f1a24"; ctx.font = "600 13px Inter, sans-serif"; ctx.textAlign = "center"; ctx.textBaseline = "middle";
      AREAS.forEach(function(a,k){ var an = -Math.PI/2 + k*2*Math.PI/n; ctx.fillText(a + " " + vals[a], cx + Math.cos(an)*(R+26), cy + Math.sin(an)*(R+22)); });
      var sum = 0, low = AREAS[0], high = AREAS[0];
      AREAS.forEach(function(a){ sum += vals[a]; if(vals[a] < vals[low]) low = a; if(vals[a] > vals[high]) high = a; });
      var avg = (sum/n).toFixed(1), bal = Math.max.apply(null, AREAS.map(function(a){return vals[a];})) - Math.min.apply(null, AREAS.map(function(a){return vals[a];}));
      $(".result", wheel).innerHTML = '<div class="big">'+avg+' / 10</div><p>Your overall life-balance score. Spread between strongest and weakest area: <b>'+bal+' points</b>' + (bal >= 4 ? " — your wheel is lopsided, so small gains in the low area will feel big." : " — a well-balanced wheel.") + '</p><p>Strongest: <b>'+high+'</b>. Biggest opportunity: <b>'+low+'</b>. <a href="'+BASE+'topics/'+LINKS[low]+'.html">Read our '+low+' guides &rarr;</a></p>';
    }
    box.addEventListener("input", draw); draw();
    document.addEventListener("click", function(e){ if(e.target.closest("[data-theme-toggle]")) setTimeout(draw, 30); });
  }

  /* ===== Life satisfaction check ===== */
  var quiz = $("[data-tool=quiz]");
  if(quiz){
    var QS = ["Most days, my life feels close to the way I want it to be.","I feel genuinely rested and energised most mornings.","I have at least two people I could call at 2am in a crisis.","My finances give me more calm than stress.","I regularly do things that feel meaningful to me.","I often notice and enjoy small, beautiful moments.","I am learning or growing in some area of my life.","If I could live the last year again, I would change very little."];
    var SC = ["Strongly disagree","Disagree","Neutral","Agree","Strongly agree"];
    $(".qs", quiz).innerHTML = QS.map(function(q,i){ return '<fieldset class="card" style="margin-bottom:12px"><legend style="font-weight:600;padding:0 6px">'+(i+1)+'. '+q+'</legend><div class="opts" style="grid-template-columns:repeat(5,1fr)">'+SC.map(function(s,k){ return '<label class="opt"><input type="radio" name="q'+i+'" value="'+(k+1)+'" required><span style="font-size:.78rem;text-align:center;padding:10px 4px">'+s+'</span></label>'; }).join("")+'</div></fieldset>'; }).join("");
    quiz.addEventListener("submit", function(e){
      e.preventDefault(); var t = 0, c = 0;
      QS.forEach(function(q,i){ var r = quiz.querySelector("input[name=q"+i+"]:checked"); if(r){ t += +r.value; c++; } });
      if(c < QS.length){ window.BL && BL.toast("Please answer all " + QS.length + " statements."); return; }
      var pct = Math.round((t - QS.length) / (QS.length*4) * 100), band, tip;
      if(pct >= 80){ band = "Flourishing"; tip = "You're thriving. Protect what works and consider mentoring someone else."; }
      else if(pct >= 60){ band = "Doing well"; tip = "Solid foundations. Pick the lowest-scoring statement and give it 30 days of focus."; }
      else if(pct >= 40){ band = "Getting by"; tip = "You're coping, but not flourishing. Our Wheel of Life tool can show you exactly where to start."; }
      else { band = "Running on empty"; tip = "Be gentle with yourself. Start with sleep and connection — and consider speaking with a qualified professional."; }
      store("bl-quiz", {pct:pct, at:Date.now()});
      var res = $(".result", quiz); res.hidden = false;
      res.innerHTML = '<div class="big">'+pct+'%</div><h3>'+band+'</h3><p>'+tip+'</p><p><a class="btn sm" href="'+BASE+'get-matched.html">Get matched with a coach &rarr;</a> <a class="btn sm ghost" href="'+BASE+'tools/wheel-of-life.html">Try the Wheel of Life</a></p>';
      res.scrollIntoView({behavior:"smooth", block:"center"});
    });
  }

  /* ===== Habit tracker ===== */
  var ht = $("[data-tool=habits]");
  if(ht){
    var H = store("bl-habits") || {list:["Drink 2L water","10-minute walk","Read 10 pages"], done:{}};
    function key(d){ return d.toISOString().slice(0,10); }
    function days(){ var a = [], t = new Date(); for(var i=6;i>=0;i--){ var x = new Date(t); x.setDate(t.getDate()-i); a.push(x); } return a; }
    function render(){
      var ds = days();
      var html = '<table class="habit-table"><thead><tr><th>Habit</th>' + ds.map(function(d){ return '<th>'+d.toLocaleDateString(undefined,{weekday:"narrow"})+'<br><small>'+d.getDate()+'</small></th>'; }).join("") + '<th>Streak</th><th></th></tr></thead><tbody>';
      H.list.forEach(function(h,i){
        var streak = 0, t = new Date(); for(var s=0;s<365;s++){ var x = new Date(t); x.setDate(t.getDate()-s); if(H.done[h+"|"+key(x)]) streak++; else if(s>0) break; }
        html += '<tr><td>'+esc(h)+'</td>' + ds.map(function(d){ var k = h+"|"+key(d); return '<td><button class="d'+(H.done[k]?" on":"")+'" data-k="'+esc(k)+'" aria-label="Toggle '+esc(h)+' '+key(d)+'"></button></td>'; }).join("") + '<td><b>'+streak+'</b>&#128293;</td><td><button class="icon-btn" style="width:30px;height:30px" data-del="'+i+'" aria-label="Remove">&times;</button></td></tr>';
      });
      html += '</tbody></table>';
      $(".table", ht).innerHTML = html;
      var total = 0, hit = 0; ds.forEach(function(d){ H.list.forEach(function(h){ total++; if(H.done[h+"|"+key(d)]) hit++; }); });
      $(".result", ht).innerHTML = '<b>' + (total ? Math.round(hit/total*100) : 0) + '%</b> consistency over the last 7 days. Aim for 80% — perfection isn’t the goal, momentum is.';
      store("bl-habits", H);
    }
    ht.addEventListener("click", function(e){
      var b = e.target.closest("button.d"); if(b){ var k = b.getAttribute("data-k"); if(H.done[k]) delete H.done[k]; else H.done[k] = 1; render(); }
      var d = e.target.closest("[data-del]"); if(d){ H.list.splice(+d.getAttribute("data-del"),1); render(); }
    });
    $("form", ht).addEventListener("submit", function(e){ e.preventDefault(); var i = $("input", this); var v = i.value.trim(); if(v && H.list.indexOf(v) < 0 && H.list.length < 12){ H.list.push(v); i.value = ""; render(); } });
    render();
  }

  /* ===== Gratitude journal ===== */
  var gj = $("[data-tool=gratitude]");
  if(gj){
    var G = store("bl-gratitude") || [];
    var PROMPTS = ["Who made your day a little easier recently?","What is something your body let you do today?","What small luxury did you enjoy this week?","Which challenge taught you something?","What in nature caught your eye lately?","What skill are you glad you have?","Which memory still makes you smile?"];
    $(".prompt", gj).textContent = PROMPTS[new Date().getDay()];
    function render(){
      $(".entries", gj).innerHTML = G.slice().reverse().slice(0,30).map(function(x){ return '<div class="entry"><small>'+new Date(x.t).toLocaleDateString(undefined,{weekday:"short",month:"short",day:"numeric"})+'</small><br>'+esc(x.a)+'<br>'+esc(x.b)+'<br>'+esc(x.c)+'</div>'; }).join("") || "<p class='meta'>Your entries will appear here. They never leave this device.</p>";
      var dates = {}; G.forEach(function(x){ dates[new Date(x.t).toDateString()] = 1; });
      $(".count", gj).textContent = Object.keys(dates).length;
    }
    $("form", gj).addEventListener("submit", function(e){ e.preventDefault(); var f = this; G.push({t:Date.now(), a:f.a.value, b:f.b.value, c:f.c.value}); store("bl-gratitude", G); f.reset(); render(); window.BL && BL.toast("Saved. Beautiful."); });
    var ex = $("[data-export]", gj);
    if(ex) ex.addEventListener("click", function(){ var txt = G.map(function(x){ return new Date(x.t).toDateString()+"\n- "+x.a+"\n- "+x.b+"\n- "+x.c; }).join("\n\n"); var a = document.createElement("a"); a.href = URL.createObjectURL(new Blob([txt],{type:"text/plain"})); a.download = "gratitude-journal.txt"; a.click(); });
    render();
  }

  /* ===== Sleep calculator ===== */
  var sl = $("[data-tool=sleep]");
  if(sl){
    function fmt(d){ return d.toLocaleTimeString([], {hour:"numeric", minute:"2-digit"}); }
    function out(list, label){ $(".result", sl).innerHTML = '<p>'+label+'</p><div class="grid g3">' + list.map(function(x){ return '<div class="card center"><div class="big" style="font-size:1.7rem">'+fmt(x.t)+'</div><span class="meta" style="justify-content:center">'+x.c+' cycles · '+(x.c*1.5)+' h</span></div>'; }).join("") + '</div><p class="meta mt">Based on ~90-minute sleep cycles plus ~15 minutes to fall asleep. Individual needs vary; most adults need at least 7 hours.</p>'; }
    $("[data-wake]", sl).addEventListener("click", function(){
      var v = $("#wake", sl).value || "07:00", p = v.split(":"), w = new Date(); w.setHours(+p[0], +p[1], 0, 0);
      var l = [6,5,4].map(function(c){ return {c:c, t:new Date(w - (c*90 + 15)*6e4)}; });
      out(l, "To wake up refreshed at <b>"+fmt(w)+"</b>, try falling asleep at one of these times:");
    });
    $("[data-now]", sl).addEventListener("click", function(){
      var n = new Date(); var l = [4,5,6].map(function(c){ return {c:c, t:new Date(+n + (c*90 + 15)*6e4)}; });
      out(l, "If you go to bed now, aim to wake up at:");
    });
  }

  /* ===== Life in weeks ===== */
  var lw = $("[data-tool=weeks]");
  if(lw){
    var go = function(){
      var b = $("#dob", lw).value; if(!b) return;
      var yrs = +$("#exp", lw).value || 85, born = new Date(b), now = new Date();
      var lived = Math.floor((now - born) / (7*864e5)), total = yrs*52, left = Math.max(total - lived, 0);
      var g = ""; for(var i=0;i<total;i++) g += '<i class="'+(i < lived ? "p" : (i === lived ? "n" : ""))+'"></i>';
      $(".weeks", lw).innerHTML = g;
      $(".result", lw).innerHTML = '<div class="big">'+left.toLocaleString()+' weeks</div><p>You have lived <b>'+lived.toLocaleString()+'</b> weeks ('+Math.round(lived/total*100)+'%). That’s roughly <b>'+Math.round(left/52)+' summers</b>, '+Math.round(left*7/30)+' full moons and '+(left*7).toLocaleString()+' sunrises left to enjoy. Make the next one count.</p>';
      store("bl-dob", {b:b, y:yrs});
    };
    var s = store("bl-dob"); if(s){ $("#dob", lw).value = s.b; $("#exp", lw).value = s.y; go(); }
    $("button", lw).addEventListener("click", go);
  }

  /* ===== Financial freedom calculator ===== */
  var ff = $("[data-tool=freedom]");
  if(ff){
    function calc(){
      var exp = +$("#f-exp", ff).value || 0, saved = +$("#f-saved", ff).value || 0, mon = +$("#f-mon", ff).value || 0, ret = (+$("#f-ret", ff).value || 0)/100, wr = (+$("#f-wr", ff).value || 4)/100;
      var target = exp * 12 / wr, bal = saved, m = 0, r = Math.pow(1+ret, 1/12) - 1;
      while(bal < target && m < 1200){ bal = bal*(1+r) + mon; m++; }
      var y = Math.floor(m/12), mm = m%12;
      $(".result", ff).innerHTML = '<p>Your freedom number</p><div class="big">'+target.toLocaleString(undefined,{maximumFractionDigits:0})+'</div><p>' + (m >= 1200 ? "At this savings rate the target is out of reach — try raising monthly savings or lowering expenses." : 'At your current pace you reach it in <b>'+y+' years'+(mm ? " and "+mm+" months" : "")+'</b>.') + '</p><p class="meta">Illustrative estimate only, not financial advice. Uses a constant real return and the withdrawal rate you chose.</p>';
    }
    ff.addEventListener("input", calc); calc();
  }

  /* ===== Breathing coach ===== */
  var br = $("[data-tool=breath]");
  if(br){
    var ball = $(".breath", br), timer = null, running = false;
    var PAT = {box:[["Breathe in",4],["Hold",4],["Breathe out",4],["Hold",4]], relax:[["Breathe in",4],["Hold",7],["Breathe out",8]], calm:[["Breathe in",5],["Breathe out",5]]};
    function run(){
      var p = PAT[$("#pattern", br).value], i = 0, rounds = 0;
      function next(){
        if(!running) return;
        var s = p[i]; ball.textContent = s[0] + " · " + s[1];
        ball.style.transitionDuration = s[1] + "s";
        if(s[0] === "Breathe in") ball.classList.add("in"); else if(s[0] === "Breathe out") ball.classList.remove("in");
        timer = setTimeout(function(){ i = (i+1) % p.length; if(i === 0){ rounds++; $(".rounds", br).textContent = rounds; } next(); }, s[1]*1000);
      }
      next();
    }
    $("[data-start]", br).addEventListener("click", function(){ running = !running; this.textContent = running ? "Pause" : "Start"; if(running) run(); else { clearTimeout(timer); ball.textContent = "Paused"; } });
  }
})();
