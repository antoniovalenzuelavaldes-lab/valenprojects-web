"""Genera la web de ValenProjects en docs/. Uso: python build.py
Sin dependencias externas, sin cookies, sin recursos de terceros. Los datos fiscales se leen de datos/titular.json (ignorado por git)."""
import os, json, html

AQUI = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(AQUI, "docs")
BASE = os.environ.get("BASE", "")

D = {
    "marca": "ValenProjects",
    "dominio": "https://valenprojects.online",
    "titular": "Antonio Valenzuela Valdes",
    "nif": "[[NIF]]",
    "domicilio": "[[DOMICILIO]]",
    "email": "antonio@valenprojects.online",
    "fecha": "28 de octubre de 2026",
}
_t = os.path.join(AQUI, "datos", "titular.json")
if os.path.exists(_t):
    D.update(json.load(open(_t, encoding="utf8")))

PRODUCTOS = [
    {"n": "Valenbeach", "e": "En línea", "css": "on", "url": "https://valenbeach.com",
     "d": "Apartamento vacacional a pie de playa en Torrox Costa (Málaga). Web propia con calendario de disponibilidad conectado en tiempo casi real y reserva por WhatsApp o correo.", "c": "#14b8a6,#0ea5e9"},
    {"n": "GymBroSquads", "e": "En desarrollo", "css": "dev", "url": "",
     "d": "Aplicación de seguimiento de entrenamientos en gimnasios con un marcado carácter social: permite compartir y retar entrenamientos con amigos y grupos.", "c": "#f97316,#ef4444"},
    {"n": "Ruta a la Plaza", "e": "En línea", "css": "on", "url": "https://rutaalaplaza.com",
     "d": "Servicio de preparación de oposiciones (apuntes, tests con la cita de la norma, simulacros y seguimiento del progreso). Es un proyecto independiente, del que es titular Lourdes; nosotros colaboramos con ella en lo técnico.", "c": "#8b5cf6,#6366f1"},
    {"n": "MenusWeb", "e": "En preparación", "css": "soon", "url": "",
     "d": "Aplicación para subir a la web los menús de restaurantes y acceder a ellos mediante códigos QR.", "c": "#eab308,#f59e0b"},
]

EQUIPO = [
    {"n": "Antonio", "r": "CEO · Jefe de orden y concierto", "d": "Si algo está fuera de sitio, lo sabe antes de que lo veas. Sus carpetas tienen carpetas, y las carpetas de las carpetas, ordenadas. Cree en las listas, las etiquetas y los lunes.", "c": "#6d5dfc,#00c2ff"},
    {"n": "Carlos", "r": "CEO · El gurú", "d": "Ideas geniales que nos dejan a todos flipando. Sin aviso previo y casi siempre a la hora de comer.", "c": "#8b5cf6,#ec4899"},
    {"n": "Gonzalo", "r": "El buscavidas", "d": "Huele una oportunidad a tres calles de distancia. La encuentra, la desarrolla hasta tener una idea inicial presentable y nos la trae con el entusiasmo de quien ya ha empezado.", "c": "#14b8a6,#22c55e"},
    {"n": "Antonio Junior", "r": "El comercial", "d": "Es capaz de vender una idea y contarla como nadie. Si dudas de algo, deja que te lo cuente él.", "c": "#f97316,#ef4444"},
    {"n": "Sancho", "r": "El chico para todo", "d": "Da soporte a todos los miembros del equipo. Si algo no funciona, pregúntale. Si funciona, seguro que también ha tenido algo que ver.", "c": "#eab308,#f59e0b"},
    {"n": "Pablo", "r": "El tester", "d": "Lo prueba todo, lo rompe en cinco minutos y, además, propone cómo mejorarlo. Lo que él aprueba, aguanta.", "c": "#0ea5e9,#6366f1"},
]
DISENO = {"r": "Las chicas design", "n": "Lourdes y Ade", "d": "Dan el visto bueno a las ideas, ponen el toque creativo y revisan cada proyecto nuevo. Si ellas dicen que algo no, no sale. Y siempre tienen razón."}

CSS = """
:root{--bg:#f7f8fc;--fg:#12162b;--mut:#5a6280;--card:#fff;--line:#e2e5f1;--a1:#6d5dfc;--a2:#00c2ff;--a3:#ff5ca8;--ok:#0f9d6e}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#0b0e1c;--fg:#eef0fb;--mut:#9aa3c4;--card:#131833;--line:#252c52;--a1:#8b7dff;--a2:#38d0ff;--a3:#ff7ab8;--ok:#3ddc97;color-scheme:dark}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.65 system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));overflow-x:hidden}
a{color:var(--a1)}
.wrap{max-width:1080px;margin:0 auto}
header.top{position:sticky;top:0;z-index:20;margin:0 calc(-1*max(16px,env(safe-area-inset-left,0px)));padding:10px max(16px,env(safe-area-inset-left,0px));background:color-mix(in srgb,var(--bg) 85%,transparent);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:14px;flex-wrap:wrap}
.logo{display:flex;align-items:center;gap:9px;text-decoration:none;color:var(--fg);font:700 1.2rem system-ui,sans-serif;letter-spacing:-.01em}
.logo b{background:linear-gradient(90deg,var(--a1),var(--a2));-webkit-background-clip:text;background-clip:text;color:transparent}
nav{display:flex;gap:18px;font-size:.9rem}nav a{color:var(--mut);text-decoration:none}nav a:hover{color:var(--fg)}
.hero{position:relative;margin:0 calc(-1*max(16px,env(safe-area-inset-left,0px)));padding:96px max(16px,env(safe-area-inset-left,0px)) 84px;overflow:hidden;text-align:center}
.blob{position:absolute;border-radius:50%;filter:blur(70px);opacity:.55;animation:flota 14s ease-in-out infinite alternate}
.b1{width:420px;height:420px;background:var(--a1);top:-140px;left:8%}
.b2{width:360px;height:360px;background:var(--a2);top:20px;right:6%;animation-delay:-4s}
.b3{width:300px;height:300px;background:var(--a3);bottom:-140px;left:42%;animation-delay:-8s;opacity:.4}
@keyframes flota{from{transform:translate(0,0) scale(1)}to{transform:translate(40px,30px) scale(1.15)}}
@media (prefers-reduced-motion:reduce){.blob{animation:none}.card:hover{transform:none}}
.hero .wrap{position:relative}
.tag{display:inline-block;font:600 .8rem system-ui,sans-serif;letter-spacing:.14em;text-transform:uppercase;padding:6px 14px;border:1px solid var(--line);border-radius:999px;background:color-mix(in srgb,var(--card) 70%,transparent)}
h1{font:800 clamp(2.4rem,7.5vw,4.6rem)/1.05 system-ui,sans-serif;letter-spacing:-.03em;margin:.5em auto .3em;max-width:16ch;text-wrap:balance}
h1 em{font-style:normal;background:linear-gradient(90deg,var(--a1),var(--a2) 55%,var(--a3));-webkit-background-clip:text;background-clip:text;color:transparent}
.lead{max-width:56ch;margin:0 auto 1.6em;color:var(--mut);font-size:1.15rem}
.btn{display:inline-block;background:linear-gradient(90deg,var(--a1),var(--a2));color:#fff;text-decoration:none;padding:13px 26px;border-radius:999px;font-weight:700;box-shadow:0 8px 24px -8px var(--a1)}
.btn.sec{background:transparent;color:var(--fg);border:1px solid var(--line);box-shadow:none;margin-left:8px}
section{padding:64px 0 8px}
h2{font:750 clamp(1.7rem,4.5vw,2.4rem)/1.15 system-ui,sans-serif;letter-spacing:-.02em;margin:0 0 .4em}
.sub{color:var(--mut);max-width:60ch;margin:0 0 1.6em}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}
.card{position:relative;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:22px;display:flex;flex-direction:column;gap:10px;transition:transform .2s,box-shadow .2s;overflow:hidden;color:inherit;text-decoration:none}
.card:hover{transform:translateY(-4px);box-shadow:0 18px 40px -20px var(--a1)}
.card::before{content:"";position:absolute;inset:0 0 auto 0;height:4px;background:linear-gradient(90deg,var(--c1),var(--c2))}
.ico{width:46px;height:46px;border-radius:13px;display:grid;place-items:center;color:#fff;font:800 1.3rem system-ui,sans-serif;background:linear-gradient(135deg,var(--c1),var(--c2))}
.card h3{margin:.2em 0 0;font:700 1.25rem system-ui,sans-serif}
.card p{margin:0;color:var(--mut);font-size:.97rem;flex:1}
.est{align-self:flex-start;font:700 .72rem system-ui,sans-serif;letter-spacing:.08em;text-transform:uppercase;padding:4px 10px;border-radius:999px;border:1px solid var(--line);color:var(--mut)}
.est.on{color:var(--ok);border-color:color-mix(in srgb,var(--ok) 45%,var(--line))}
.est.dev{color:var(--a3)}
.go{font-weight:700;color:var(--a1);font-size:.92rem}
.how{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}
.how div{border-left:3px solid var(--a1);padding:4px 0 4px 16px}
.how b{display:block;font-size:1.05rem;margin-bottom:2px}
.how span{color:var(--mut);font-size:.96rem}

.team{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px}
.mem{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:20px;display:flex;flex-direction:column;gap:6px}
.av{width:64px;height:64px;border-radius:50%;display:grid;place-items:center;color:#fff;font:800 1.5rem system-ui,sans-serif;background:linear-gradient(135deg,var(--c1),var(--c2));box-shadow:0 8px 20px -10px var(--c1);margin-bottom:6px}
.mem h3{margin:0;font:700 1.15rem system-ui,sans-serif}
.mem .rol{font:700 .75rem system-ui,sans-serif;letter-spacing:.07em;text-transform:uppercase;color:var(--a1)}
.mem p{margin:.2em 0 0;color:var(--mut);font-size:.95rem}
.mem.wide{grid-column:1/-1;flex-direction:row;align-items:center;gap:20px;flex-wrap:wrap}
.mem.wide .avs{display:flex}.mem.wide .avs .av{margin-right:-14px;border:3px solid var(--card)}
.mem.wide .txt{flex:1;min-width:230px}
.nota{color:var(--mut);font-size:.85rem;margin-top:14px}
.contacto{margin-top:64px;padding:36px;border-radius:22px;background:linear-gradient(135deg,color-mix(in srgb,var(--a1) 18%,var(--card)),color-mix(in srgb,var(--a2) 14%,var(--card)));border:1px solid var(--line);text-align:center}
footer{margin-top:60px;border-top:1px solid var(--line);padding:26px 0 44px;color:var(--mut);font-size:.88rem}
footer a{color:var(--mut)}
.legal main{max-width:760px;margin:0 auto;padding:36px 0}.legal h1{font-size:2.2rem;max-width:none;margin:.3em 0 .5em;text-align:left;background:none;color:var(--fg)}
.legal h2{font-size:1.25rem;margin-top:1.6em}.meta{color:var(--mut);font-size:.9rem}
.legal table{border-collapse:collapse;width:100%;display:block;overflow-x:auto}.legal td,.legal th{border:1px solid var(--line);padding:6px 10px;text-align:left;vertical-align:top}
"""

SPARK = '<svg width="26" height="26" viewBox="0 0 24 24" aria-hidden="true"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8b7dff"/><stop offset="1" stop-color="#00c2ff"/></linearGradient></defs><path d="M12 1.5l2.6 6.9 6.9 2.6-6.9 2.6L12 20.5l-2.6-6.9L2.5 11l6.9-2.6z" fill="url(#g)"/><circle cx="19" cy="19" r="2.3" fill="#ff5ca8"/></svg>'


def e(s):
    return html.escape(s, quote=True)


def cab(titulo, desc, ruta, legal=False):
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(titulo)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{D['dominio']}{ruta}">
<meta property="og:title" content="{e(titulo)}"><meta property="og:description" content="{e(desc)}"><meta property="og:type" content="website">
<style>{CSS}</style></head><body class="{'legal' if legal else ''}"><header class="top"><div class="wrap"><a class="logo" href="/">{SPARK}<span>Valen<b>Projects</b></span></a>
<nav><a href="/#productos">Productos</a><a href="/#como">Cómo trabajamos</a><a href="/#equipo">Equipo</a><a href="/#contacto">Contacto</a></nav></div></header>"""


def pie():
    return f"""<footer><div class="wrap"><p><b>{e(D['marca'])}</b> · Titular: {e(D['titular'])} · NIF {e(D['nif'])}<br>{e(D['domicilio'])} · <a href="mailto:{D['email']}">{D['email']}</a></p>
<p><a href="/aviso-legal/">Aviso legal</a> · <a href="/privacidad/">Privacidad y cookies</a></p></div></footer></body></html>"""


def equipo_html():
    t = ""
    for m in EQUIPO:
        c1, c2 = m["c"].split(",")
        t += (f'<div class="mem" style="--c1:{c1};--c2:{c2}"><div class="av">{e(m["n"][0])}</div><h3>{e(m["n"])}</h3>'
              f'<span class="rol">{e(m["r"])}</span><p>{e(m["d"])}</p></div>')
    t += (f'<div class="mem wide" style="--c1:#ec4899;--c2:#8b5cf6"><div class="avs"><div class="av">L</div><div class="av" style="--c1:#8b5cf6;--c2:#6366f1">A</div></div>'
          f'<div class="txt"><h3>{e(DISENO["n"])}</h3><span class="rol">{e(DISENO["r"])}</span><p>{e(DISENO["d"])}</p></div></div>')
    return t


def home():
    cards = ""
    for p in PRODUCTOS:
        c1, c2 = p["c"].split(",")
        tag = "a" if p["url"] else "div"
        href = f' href="{p["url"]}" target="_blank" rel="noopener"' if p["url"] else ""
        go = '<span class="go">Visitar →</span>' if p["url"] else ""
        cards += (f'<{tag} class="card" style="--c1:{c1};--c2:{c2}"{href}><div class="ico">{e(p["n"][0])}</div>'
                  f'<span class="est {p["css"]}">{e(p["e"])}</span><h3>{e(p["n"])}</h3><p>{e(p["d"])}</p>{go}</{tag}>')
    h = cab("ValenProjects · Ideas que se mueven", "Creamos productos digitales con ayuda de inteligencia artificial: apps, plataformas y webs que funcionan.", "/")
    h += f"""<div class="hero"><i class="blob b1"></i><i class="blob b2"></i><i class="blob b3"></i><div class="wrap">
<span class="tag">Proyectos con IA</span><h1>Ideas que se <em>mueven</em></h1>
<p class="lead">Creamos productos digitales con ayuda de inteligencia artificial: apps, plataformas y webs pensadas para usarse, no para quedarse en un cajón.</p>
<a class="btn" href="#productos">Ver proyectos</a><a class="btn sec" href="#contacto">Hablemos</a></div></div>
<main class="wrap"><section id="productos"><h2>Nuestros proyectos</h2><p class="sub">Cada uno con su marca, su web y sus propias condiciones. Estos son los que tenemos en marcha.</p><div class="grid">{cards}</div></section>
<section id="como"><h2>Cómo trabajamos</h2><p class="sub">Un equipo pequeño que se apoya en la IA para ir rápido, sin renunciar al cuidado.</p><div class="how">
<div><b>De la idea al prototipo, rápido</b><span>Probamos pronto y ajustamos sobre la marcha.</span></div>
<div><b>La IA como copiloto</b><span>La usamos para programar, redactar y comprobar, pero revisamos todo antes de publicarlo.</span></div>
<div><b>Datos en su sitio</b><span>Cada proyecto tiene su propia base de datos y su propia política de privacidad. Sin cookies de seguimiento.</span></div>
<div><b>Transparencia</b><span>Quién está detrás, cómo contactar y qué datos se tratan, siempre a la vista.</span></div></div></section>
<section id="equipo"><h2>El equipo</h2><p class="sub">Ocho personas, una idea fija: que las cosas salgan bien, y a ser posible con una sonrisa.</p><div class="team">{equipo_html()}</div><p class="nota">Los avatares ilustrados llegan pronto.</p></section>
<section id="contacto"><div class="contacto"><h2>¿Hablamos?</h2><p class="sub" style="margin:0 auto 1.2em">Cuéntanos tu idea, una duda o una propuesta de colaboración.</p>
<a class="btn" href="mailto:{D['email']}">{D['email']}</a></div></section></main>"""
    return h + pie()


AVISO = f"""
<p class="meta">Última actualización: {D['fecha']}.</p>
<h2>1. Datos identificativos</h2>
<p>En cumplimiento del artículo 10 de la Ley 34/2002 (LSSI), se informa de que este sitio web es titularidad de:</p>
<p><b>Titular:</b> {D['titular']}<br><b>NIF:</b> {D['nif']}<br><b>Domicilio:</b> {D['domicilio']}<br><b>Correo electrónico:</b> {D['email']}<br><b>Nombre comercial:</b> {D['marca']}<br><b>Actividad:</b> desarrollo y explotación de servicios y aplicaciones web<br><b>Condición:</b> persona física; sin inscripción en el Registro Mercantil.</p>
<h2>2. Objeto</h2>
<p>Esta web presenta la actividad y los proyectos de {D['marca']}. Cada proyecto tiene su propio sitio, con su aviso legal, su política de privacidad y, en su caso, sus condiciones de contratación, donde figura quién es su titular.</p>
<h2>3. Propiedad intelectual</h2>
<p>Los textos, diseños y código de esta web pertenecen al titular. No se permite su reproducción o comunicación pública sin autorización, salvo lo permitido por la ley. Los nombres y marcas de terceros citados pertenecen a sus titulares.</p>
<h2>4. Responsabilidad</h2>
<p>La información de esta web es orientativa y se mantiene actualizada en la medida de lo posible. El titular no responde de los contenidos de sitios de terceros a los que se pueda enlazar.</p>
<h2>5. Legislación y jurisdicción</h2>
<p>Legislación española. Si eres consumidor, son competentes los juzgados y tribunales de tu domicilio.</p>
"""

PRIV = f"""
<p class="meta">Última actualización: {D['fecha']}.</p>
<h2>1. Responsable</h2>
<p><b>{D['titular']}</b>, NIF {D['nif']}, con domicilio en {D['domicilio']}. Contacto: {D['email']}.</p>
<h2>2. Qué datos tratamos</h2>
<p>Esta web <b>no tiene formularios ni cuentas de usuario</b> y no guarda datos. Solo trataremos los que tú nos envíes por correo electrónico (tu dirección y lo que escribas) para responderte, con base en tu solicitud (art. 6.1.b RGPD) o en nuestro interés legítimo en atender consultas (art. 6.1.f).</p>
<h2>3. Destinatarios</h2>
<p>El correo de este dominio se reenvía mediante el servicio Email Routing de Cloudflare y se recibe en una cuenta de Gmail (Google). La web se aloja en GitHub Pages, que puede registrar tu dirección IP por motivos técnicos y de seguridad. No cedemos tus datos a terceros salvo obligación legal. Algunos proveedores pueden implicar transferencias fuera del Espacio Económico Europeo, amparadas en decisiones de adecuación o cláusulas contractuales tipo.</p>
<h2>4. Conservación</h2>
<p>Conservamos tus mensajes el tiempo necesario para atender tu consulta y, después, durante los plazos legales que correspondan.</p>
<h2>5. Tus derechos</h2>
<p>Puedes ejercer los derechos de acceso, rectificación, supresión, oposición, limitación y portabilidad escribiendo a {D['email']}. Si crees que tus datos no se tratan correctamente, puedes reclamar ante la Agencia Española de Protección de Datos (<a href="https://www.aepd.es">www.aepd.es</a>).</p>
<h2>6. Cookies</h2>
<p>Esta web <b>no instala cookies</b> ni usa herramientas de analítica o publicidad, ni carga recursos de terceros. Por eso no muestra aviso de cookies.</p>
"""


def legal(titulo, cuerpo, ruta):
    return cab(f"{titulo} · {D['marca']}", titulo, ruta, legal=True) + f"<main><h1>{e(titulo)}</h1>{cuerpo}</main>" + pie()


def w(ruta, contenido):
    p = os.path.join(SITE, ruta.strip("/"), "index.html") if ruta != "/" else os.path.join(SITE, "index.html")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    if BASE:
        import re
        contenido = re.sub(r'(href|src)="/(?!/)', lambda m: m.group(1) + '="' + BASE + '/', contenido)
        contenido = contenido.replace('<meta charset="utf-8">', '<meta charset="utf-8"><meta name="robots" content="noindex,nofollow">', 1)
    open(p, "w", encoding="utf8").write(contenido)


if __name__ == "__main__":
    os.makedirs(SITE, exist_ok=True)
    w("/", home())
    w("/aviso-legal/", legal("Aviso legal", AVISO, "/aviso-legal/"))
    w("/privacidad/", legal("Privacidad y cookies", PRIV, "/privacidad/"))
    open(os.path.join(SITE, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {D['dominio']}/sitemap.xml\n")
    open(os.path.join(SITE, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' +
        "".join(f"<url><loc>{D['dominio']}{u}</loc></url>" for u in ("/", "/aviso-legal/", "/privacidad/")) + "</urlset>")
    if not BASE:
        open(os.path.join(SITE, "CNAME"), "w").write("valenprojects.online\n")
        open(os.path.join(SITE, "404.html"), "w", encoding="utf8").write(legal("Página no encontrada", "<p>Esta página no existe.</p><p><a href='/'>Volver al inicio</a></p>", "/404.html"))
    print("docs/ generado")
