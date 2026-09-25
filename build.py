#!/usr/bin/env python3
"""Generate the mnavas.github.io portfolio as a full-screen vertical scroll-snap feed."""
import html, pathlib

OUT = pathlib.Path(__file__).resolve().parent / "index.html"

PROJECTS = [
    dict(id="questbee", emoji="🐝", name="Questbee", accent="#E0A21A",
         img="assets/projects/questbee.jpg",
         tagline="Surveys & field data collection, on your own servers",
         desc="A self-hosted, offline-first data collection platform — build forms in the browser, collect on Android with no internet, and sync when connectivity returns. Full data sovereignty, no per-submission fees, one <code>docker-compose up</code>.",
         tags=["Self-hosted","Docker","Offline-first"],
         open="https://questbee.github.io/page/", repo="https://github.com/Questbee/community"),
    dict(id="image-editor", emoji="🎨", name="image-editor", accent="#7C5CFC",
         img="assets/projects/image-editor.png",
         tagline="Photoshop-grade photo editing, phone-app simple",
         desc="Erase people, edit only part of a picture, curves, colour grading, reshape and film looks — with AI (SAM + LaMa) — that always saves at full original resolution, non-destructively.",
         tags=["Python","PyQt6","OpenCV","AI"],
         open="https://mnavas.github.io/image-editor/", repo="https://github.com/mnavas/image-editor"),
    dict(id="elgatomenu", emoji="🐱", name="ElGatoMenu", accent="#C0392B",
         img="assets/projects/elgatomenu.jpg",
         tagline="QR ordering for restaurants",
         desc="A digital menu, OCR payment verification, a live kitchen display, and staff management — fully self-hosted with Docker. Your restaurant's data stays yours.",
         tags=["Self-hosted","Docker","Web"],
         open="https://mnavas.github.io/elgatomenu-page/", repo="https://github.com/mnavas/elgatomenu"),
    dict(id="quizbuilder", emoji="📝", name="QuizBuilder", accent="#2E6FE0",
         img="assets/projects/quizbuilder.jpg",
         tagline="Self-hosted online assessments",
         desc="Build and run your own online assessments — rich questions with audio and video, auto-scoring and manual review, fully self-hosted with Docker.",
         tags=["Self-hosted","Docker","Web"],
         open="https://mnavas.github.io/quizbuilder/", repo="https://github.com/mnavas/quizbuilder"),
    dict(id="nano-bot", emoji="🤖", name="nano-bot", accent="#12B39B",
         img="assets/projects/nano-bot.png",
         tagline="An AI programming competition inside the human body",
         desc="Write a single Python strategy to command a fleet of nanobots across living tissue — collect energy, claim Habitas Points, and outscore your opponent over 1500 turns. A Habitas Games project.",
         tags=["Python","pygame","AI contest"],
         open="https://habitas-games.github.io/nano-bot-python/", repo="https://github.com/Habitas-Games/nano-bot-python"),
    dict(id="videobuilder", emoji="🎬", name="VideoBuilder", accent="#F5731F",
         img="assets/projects/videobuilder.jpg",
         tagline="A simple timeline video editor & slideshow maker",
         desc="Build videos from clips and photos on one simple timeline — drag, trim, crossfade, add titles and music, and export to MP4 with ffmpeg.",
         tags=["Python","PySide6","ffmpeg"],
         open="https://mnavas.github.io/videobuilder/", repo="https://github.com/mnavas/videobuilder"),
    dict(id="image-selector", emoji="🗂", name="image-selector", accent="#14B8A6",
         img="assets/projects/image-selector.jpg",
         tagline="Keyboard-driven photo triage & editing",
         desc="Browse, sort, and edit photos without leaving the keyboard — 30 film & camera looks, AI-assisted edits via Claude or Ollama, fully non-destructive.",
         tags=["Python","PyQt6","AI"],
         open="https://mnavas.github.io/image-selector/", repo="https://github.com/mnavas/image-selector"),
    dict(id="instax-printing", emoji="🖼", name="instax-printing", accent="#E5397E",
         img="assets/projects/instax-printing.png",
         tagline="Three instax minis on one 4R print",
         desc="Arrange three photos as instax-mini cards on a single print-ready 4R (15×10 cm) sheet — real white border and cut marks. Three instax for the price of one photo.",
         tags=["Python","PyQt6","Print"],
         open="https://mnavas.github.io/instax-printing/", repo="https://github.com/mnavas/instax-printing"),
]

def slide(p, i):
    flip = " flip" if i % 2 else ""
    tags = "".join(f'<span class="tag">{html.escape(t)}</span>' for t in p["tags"])
    return f'''
  <section class="slide project{flip}" id="{p['id']}" style="--accent:{p['accent']}">
    <div class="inner">
      <div class="frame">
        <div class="bar"><span class="d r"></span><span class="d y"></span><span class="d g"></span><span class="url">{html.escape(p['name'])}</span></div>
        <div class="shot"><img src="{p['img']}" alt="{html.escape(p['name'])} screenshot" loading="lazy"></div>
      </div>
      <div class="meta">
        <div class="count">{i+1:02d} / {len(PROJECTS):02d}</div>
        <h2><span class="emoji">{p['emoji']}</span>{html.escape(p['name'])}</h2>
        <p class="tagline">{html.escape(p['tagline'])}</p>
        <p class="desc">{p['desc']}</p>
        <div class="tags">{tags}</div>
        <div class="links">
          <a class="open" href="{p['open']}" target="_blank" rel="noopener">Open&nbsp;→</a>
          <a class="repo" href="{p['repo']}" target="_blank" rel="noopener">GitHub</a>
        </div>
      </div>
    </div>
  </section>'''

dots = "".join(f'<a href="#{p["id"]}" aria-label="{html.escape(p["name"])}"></a>' for p in PROJECTS)
slides = "".join(slide(p, i) for i, p in enumerate(PROJECTS))

DOC = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Mario Navas — Projects</title>
<meta name="description" content="Free and open-source desktop and self-hosted apps by Mario Navas (@mnavas): a full-resolution photo editor, a self-hosted data platform, restaurant ordering, a video editor, an AI programming game, and more." />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{--ink:#1a1922;--muted:#5b5866;--line:#e6e5ea;--bg:#fff;--g50:#faf9fc;--accent:#7C5CFC}}
html{{scroll-snap-type:y mandatory;scroll-behavior:smooth;height:100%}}
body{{font-family:'Inter',sans-serif;color:var(--ink);background:var(--bg);line-height:1.6;height:100%;overflow-x:hidden}}
a{{text-decoration:none}}
img{{max-width:100%;display:block}}

/* top bar */
.top{{position:fixed;top:0;left:0;right:0;z-index:50;display:flex;align-items:center;justify-content:space-between;
  padding:.85rem 1.5rem;background:rgba(255,255,255,.82);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}}
.top .brand{{font-weight:800;color:var(--ink);font-size:1.05rem}}
.top .right{{display:flex;gap:1.25rem;align-items:center}}
.top .right a{{font-size:.85rem;font-weight:600;color:var(--muted)}}
.top .right a.gh{{background:var(--ink);color:#fff;padding:.45rem 1rem;border-radius:8px}}
.top .right a:hover{{color:var(--ink)}} .top .right a.gh:hover{{opacity:.88;color:#fff}}

/* dot nav */
.dots{{position:fixed;right:1.1rem;top:50%;transform:translateY(-50%);z-index:50;display:flex;flex-direction:column;gap:.7rem}}
.dots a{{width:10px;height:10px;border-radius:50%;background:#cfcdd8;transition:.2s;border:2px solid transparent}}
.dots a:hover{{background:var(--ink);transform:scale(1.2)}}
@media(max-width:820px){{.dots{{display:none}}}}

/* slides */
.slide{{min-height:100vh;min-height:100dvh;scroll-snap-align:start;display:flex;align-items:center;justify-content:center;padding:6rem 2rem 3rem;position:relative}}
.slide.project{{background:
  radial-gradient(1100px 600px at 100% 0%, color-mix(in srgb, var(--accent) 9%, transparent), transparent 60%),
  radial-gradient(900px 500px at 0% 100%, color-mix(in srgb, var(--accent) 7%, transparent), transparent 55%),
  var(--bg)}}
.slide:nth-child(even).project{{background:
  radial-gradient(1100px 600px at 0% 0%, color-mix(in srgb, var(--accent) 9%, transparent), transparent 60%),
  var(--g50)}}
.inner{{max-width:1120px;width:100%;display:grid;grid-template-columns:1.15fr .85fr;gap:3.2rem;align-items:center}}
.slide.flip .inner .frame{{order:2}}

/* window frame + screenshot */
.frame{{border-radius:16px;overflow:hidden;background:#1c1b24;border:1px solid rgba(0,0,0,.08);
  box-shadow:0 30px 70px -20px color-mix(in srgb, var(--accent) 45%, rgba(20,15,40,.5))}}
.bar{{display:flex;align-items:center;gap:7px;padding:.6rem .85rem;background:#151420}}
.bar .d{{width:11px;height:11px;border-radius:50%}}
.bar .r{{background:#ff5f57}}.bar .y{{background:#febc2e}}.bar .g{{background:#28c840}}
.bar .url{{margin-left:.6rem;font-family:'JetBrains Mono',monospace;font-size:.72rem;color:#8b899a}}
.shot{{aspect-ratio:16/10;background:#0e0d15}}
.shot img{{width:100%;height:100%;object-fit:cover;object-position:center}}

/* text column */
.meta .count{{font-family:'JetBrains Mono',monospace;font-size:.8rem;font-weight:600;color:var(--accent);letter-spacing:.05em;margin-bottom:.6rem}}
.meta h2{{font-size:clamp(1.8rem,4vw,2.8rem);font-weight:900;line-height:1.1;display:flex;align-items:center;gap:.6rem}}
.meta h2 .emoji{{font-size:.9em}}
.meta .tagline{{font-size:1.1rem;font-weight:600;color:var(--accent);margin:.5rem 0 .9rem}}
.meta .desc{{font-size:1rem;color:var(--muted);line-height:1.7;max-width:46ch}}
.meta .desc code{{background:color-mix(in srgb,var(--accent) 12%,transparent);color:var(--ink);padding:.1em .4em;border-radius:5px;font-family:'JetBrains Mono',monospace;font-size:.85em}}
.meta .tags{{display:flex;flex-wrap:wrap;gap:.5rem;margin:1.1rem 0 1.4rem}}
.tag{{font-size:.72rem;font-weight:600;color:var(--muted);background:#fff;border:1px solid var(--line);padding:3px 10px;border-radius:999px;font-family:'JetBrains Mono',monospace}}
.links{{display:flex;gap:.75rem}}
.links a{{font-size:.92rem;font-weight:700;padding:.7rem 1.3rem;border-radius:10px;transition:.15s}}
.links .open{{background:var(--accent);color:#fff}}.links .open:hover{{filter:brightness(1.08);transform:translateY(-1px)}}
.links .repo{{background:transparent;color:var(--ink);border:1.5px solid var(--line)}}.links .repo:hover{{border-color:var(--accent);color:var(--accent)}}

/* hero */
.hero{{background:radial-gradient(1200px 700px at 50% -10%, #efeaff, #fff 60%)}}
.hero .inner-h{{max-width:820px;text-align:center;padding:0 1rem}}
.hero .eyebrow{{display:inline-block;background:#efeaff;border:1px solid #7C5CFC44;color:#5B3EE8;font-size:.8rem;font-weight:700;padding:5px 14px;border-radius:999px;margin-bottom:1.4rem}}
.hero h1{{font-size:clamp(2.2rem,6vw,4rem);font-weight:900;line-height:1.08;letter-spacing:-.02em}}
.hero h1 .hl{{color:#7C5CFC}}
.hero p{{font-size:1.15rem;color:var(--muted);max-width:620px;margin:1.2rem auto 0}}
.hero .meta-row{{margin-top:1.6rem;display:flex;gap:1.4rem;justify-content:center;flex-wrap:wrap;font-size:.82rem;color:#8b899a}}
.scrollhint{{position:absolute;bottom:2rem;left:50%;transform:translateX(-50%);color:#a5a3ae;font-size:.8rem;font-weight:600;display:flex;flex-direction:column;align-items:center;gap:.3rem;animation:bob 1.8s ease-in-out infinite}}
@keyframes bob{{0%,100%{{transform:translateX(-50%) translateY(0)}}50%{{transform:translateX(-50%) translateY(6px)}}}}

/* support + footer */
.support{{background:var(--g50);flex-direction:column}}
.support .s-inner{{max-width:900px;width:100%;display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:center}}
.support h2{{font-size:clamp(1.6rem,3.5vw,2.3rem);font-weight:800;margin-bottom:1rem}}
.support p{{color:var(--muted);margin-bottom:1rem}} .support p.fine{{font-size:.85rem;color:#a5a3ae}}
.donate{{background:#fff;border:1.5px solid var(--line);border-radius:16px;padding:2rem}}
.donate h3{{font-size:1rem;font-weight:700;margin-bottom:1.1rem}}
.donate .opt{{display:flex;flex-direction:column;gap:.7rem}}
.dbtn{{display:flex;align-items:center;gap:12px;padding:.85rem 1.2rem;border-radius:10px;font-size:.875rem;font-weight:700;border:none;cursor:pointer;color:#fff;width:100%;font-family:'Inter',sans-serif}}
.dbtn small{{display:block;font-weight:400;opacity:.75;font-size:.75rem}} .dbtn .t{{text-align:left;line-height:1.2}}
.gh2{{background:#24292F}}.pp{{background:#003087}}.du{{background:#1a1a2e}}
@media(max-width:820px){{.support .s-inner{{grid-template-columns:1fr}}}}
footer{{background:#141320;color:#a5a3ae;text-align:center;padding:2.5rem 2rem;scroll-snap-align:end}}
footer .fb{{color:#fff;font-weight:800;font-size:1.05rem}} footer p{{font-size:.8rem;margin-top:.4rem}}
footer a{{color:#cfcdd8;font-size:.82rem}} footer a:hover{{color:#fff}}

/* modal */
.overlay{{display:none;position:fixed;inset:0;z-index:999;background:rgba(0,0,0,.7);align-items:center;justify-content:center}}
.overlay.open{{display:flex}}
.box{{background:#fff;border-radius:20px;padding:2rem;max-width:340px;width:90%;text-align:center;box-shadow:0 24px 60px rgba(0,0,0,.3)}}
.box h3{{font-weight:700;margin-bottom:.25rem}} .box p{{font-size:.85rem;color:var(--muted);margin-bottom:1rem}}
.box img{{width:100%;max-width:260px;border-radius:12px}}
.box button{{margin-top:1rem;padding:.5rem 1.5rem;background:#f0eff4;border:none;border-radius:8px;font-weight:600;cursor:pointer;font-family:'Inter',sans-serif}}

/* mobile */
@media(max-width:820px){{
  .inner{{grid-template-columns:1fr;gap:1.6rem}}
  .slide.flip .inner .frame{{order:0}}
  .slide{{padding:5rem 1.25rem 2.5rem}}
  .meta .desc{{max-width:none}}
}}
</style>
</head>
<body>

<div class="top">
  <span class="brand">Mario&nbsp;Navas</span>
  <div class="right">
    <a href="#support">Support</a>
    <a class="gh" href="https://github.com/mnavas" target="_blank" rel="noopener">GitHub</a>
  </div>
</div>

<div class="dots">{dots}</div>

<section class="slide hero" id="top">
  <div class="inner-h">
    <span class="eyebrow">👋 Free &amp; open source</span>
    <h1>I build small, useful apps that <span class="hl">respect your data</span>.</h1>
    <p>Desktop and self-hosted tools — no accounts, no cloud, no telemetry. Everything runs on your own machine. Scroll to explore.</p>
    <div class="meta-row"><span>🖥 Desktop &amp; self-hosted</span><span>🔒 100% local</span><span>🐍 Python · Qt · Docker</span></div>
  </div>
  <a class="scrollhint" href="#{PROJECTS[0]['id']}"><span>Scroll</span><span>↓</span></a>
</section>
{slides}

<section class="slide support" id="support">
  <div class="s-inner">
    <div>
      <h2>Support the work</h2>
      <p>These are built and maintained as side projects — free and open source, with no company or VC behind them.</p>
      <p>If something here saves you time or money, a small contribution helps keep it going. Thank you!</p>
      <p class="fine">All contributions go directly to the developer.</p>
    </div>
    <div class="donate">
      <h3>Choose how to support</h3>
      <div class="opt">
        <a class="dbtn gh2" href="https://github.com/sponsors/mnavas" target="_blank" rel="noopener"><span>♥</span><span class="t">GitHub Sponsors<small>Monthly or one-time</small></span></a>
        <a class="dbtn pp" href="https://paypal.me/warionv" target="_blank" rel="noopener"><span>💳</span><span class="t">PayPal<small>paypal.me/warionv</small></span></a>
        <button class="dbtn du" onclick="document.getElementById('deuna').classList.add('open')"><span>📱</span><span class="t">De Una · Banco Pichincha<small>Pago con QR — Ecuador</small></span></button>
      </div>
    </div>
  </div>
</section>

<footer>
  <div class="fb">Mario Navas</div>
  <p>Free &amp; open-source apps · everything runs on your machine</p>
  <p style="margin-top:1rem"><a href="https://github.com/mnavas" target="_blank" rel="noopener">GitHub</a> · <a href="#top">Back to top</a></p>
</footer>

<div class="overlay" id="deuna" onclick="if(event.target===this)this.classList.remove('open')">
  <div class="box">
    <h3>De Una · Banco Pichincha</h3>
    <p>Escanea el QR con tu app bancaria para enviar tu aporte.<br>¡Muchas gracias!</p>
    <img src="assets/deuna-qr.png" alt="QR De Una — Banco Pichincha" />
    <button onclick="document.getElementById('deuna').classList.remove('open')">Cerrar</button>
  </div>
</div>

<script>
// highlight the active dot as you scroll
const io=new IntersectionObserver((es)=>{{es.forEach(e=>{{if(e.isIntersecting){{const id=e.target.id;document.querySelectorAll('.dots a').forEach(a=>a.style.background=a.getAttribute('href')==='#'+id?'#1a1922':'');}}}})}},{{threshold:.6}});
document.querySelectorAll('.slide.project').forEach(s=>io.observe(s));
</script>
</body>
</html>'''

OUT.write_text(DOC)
print("wrote", OUT, len(DOC), "bytes;", len(PROJECTS), "project slides")
