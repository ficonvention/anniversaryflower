# -*- coding: utf-8 -*-
"""Anniversary Flower — faithful rebuild of the original Wix layout:
mint page (#C4DCDC), centred logo stack, nav row, teal band (#446666), slideshow, photo collage, brown text (#60391A)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_engine"))
from sitegen import *

EMAIL = "anniversaryflower@naver.com"
LOGO = "images/214ec6_10deec9dc81db78c7e47aad080021d06.png"
BRAND = f'''<a class="brand logo-stack" href="index.html">
  <img src="{LOGO}" alt="Anniversary Flower" class="logo-img">
  <span class="brand-main">Anniversary Flower</span>
  <span class="brand-sub">웨딩 * 파티</span>
  <span class="brand-tag">Creative events.</span>
</a>'''

SITE = dict(
    name="Anniversary Flower", domain="www.anniversaryflower.co.kr",
    brand_main="Anniversary Flower", brand_sub="웨딩 * 파티",
    brand_html=BRAND, header_cls=" header-stack",
    footer_brand_html="Executive Luxury Wedding &amp; Party<br>Anniversary Flower",
    fonts="https://fonts.googleapis.com/css2?family=Fredericka+the+Great&family=Sail&family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Noto+Sans+KR:wght@300;400;500;700&display=swap",
    desc="애니버셔리 플라워 — 웨딩 & 파티 플라워, 가든 웨딩, 돌잔치, 플라워 바스켓·부케·난 선물. 세빛섬 플로팅아일랜드·마리나파크 공식 플라워 파트너. 서울 서초 아크로비스타.",
    og="2649b2_3b3e2509559c43fcbc5da556d9a73398~mv2.jpeg",
    address="Seoul, Seocho-gu, Seocho-dong 1685-3, Acrovista Arcade 112-4 (서울 서초구 서초동 1685-3 아크로비스타 아케이드 112-4)",
    tel="(02) 3443-2117", tel_raw="0234432117", fax="", email=EMAIL,
    legal="Anniversary Flower",
    social=[("Instagram", "https://www.instagram.com/anniversaryflower", IG_SVG), ("YouTube", "https://www.youtube.com/@anniversaryflower", YT_SVG)],
    favicon='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#c4dcdc"/><text x="32" y="43" text-anchor="middle" font-family="Georgia,serif" font-size="30" fill="#60391a">A</text></svg>',
    nav=[
        ("index.html", "Anniversary Flower", []),
        ("flower-basket.html", "Flower basket", []),
        ("flower-bouquet.html", "Flower Bouquet", []),
        ("orchid-gift.html", "Orchid Gift", []),
        ("garden-wedding.html", "Garden Wedding", []),
        ("first-party.html", "1st Party", []),
        ("about.html", "About us", []),
        ("contact.html", "Contact", []),
    ],
)

THEME = """:root{
  --ink:#60391a; --ink-soft:#8a6a4a; --line:#a9c6c6; --paper:#c4dcdc; --cream:#f9eadd;
  --gold:#998564; --gold-deep:#60391a; --teal:#446666; --teal-text:#669999; --sky:#daeef3;
  --serif:"Playfair Display",Georgia,serif; --sans:"Noto Sans KR","Apple SD Gothic Neo",sans-serif;
  --display:"Fredericka the Great",Georgia,serif; --script:"Sail",cursive;
  --wrap:980px; --header-h:300px;
}
body{background:var(--paper);color:var(--ink)}
/* stacked header (static, not fixed) */
.site-header.header-stack{position:static;height:auto;background:var(--paper);border:0;backdrop-filter:none;padding-top:22px}
.site-header.header-stack .wrap{flex-direction:column;height:auto;gap:0}
.logo-stack{display:flex;flex-direction:column;align-items:center;text-align:center;line-height:1.15;margin-bottom:1.4rem}
.logo-img{width:153px;height:auto;margin-bottom:.4rem}
.logo-stack .brand-main{font-family:var(--display);font-size:33px;letter-spacing:0;color:#301c0d;font-weight:400}
.logo-stack .brand-sub{font-family:var(--sans);font-size:18px;letter-spacing:.08em;color:var(--ink);opacity:1;margin-top:2px}
.logo-stack .brand-tag{font-family:var(--script);font-size:25px;color:var(--gold);margin-top:.25rem}
.header-stack .site-nav{width:100%;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.header-stack .site-nav ul{justify-content:space-between;gap:.5rem;padding:0 4px}
.header-stack .site-nav a{font-size:14px;letter-spacing:.02em;text-transform:none;color:var(--ink);padding:.7rem .2rem}
.header-stack .site-nav li.active > a{color:var(--teal-text)}
.header-stack .site-nav li > a::after{display:none}
.has-hero .site-header.header-stack{color:var(--ink)}
.hero,.page-hero{margin-top:0}
/* teal band */
.band{background:var(--teal);color:#f9eadd;text-align:center;padding:.55rem 0;font-family:var(--serif);font-style:italic;font-size:1.45rem;letter-spacing:.02em}
/* slideshow */
.slides{position:relative;width:100%;aspect-ratio:981/392;overflow:hidden;background:#000}
.slides img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity 1s}
.slides img.on{opacity:1}
.slides .dots{position:absolute;bottom:10px;left:0;right:0;text-align:center}
.slides .dots i{display:inline-block;width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,.5);margin:0 3px}
.slides .dots i.on{background:#fff}
/* collage */
.collage{display:grid;grid-template-columns:390px 1fr;gap:4px;margin-top:4px}
.collage .tall img{width:100%;height:575px;object-fit:cover;display:block}
.collage .right{display:grid;grid-template-rows:274px 295px;gap:4px}
.collage .row2{display:grid;grid-template-columns:1fr 188px;gap:4px}
.collage img{width:100%;height:100%;object-fit:cover;display:block}
.collage .txt{padding:1rem 1.2rem;font-family:var(--serif);color:var(--ink);line-height:1.5}
.collage .txt h3{font-family:var(--serif);font-weight:600;font-size:1.3rem;margin-bottom:.4em}
.collage .txt p{margin:0 0 .3em;font-size:.92rem}
.collage .txt .tags{color:var(--teal-text);font-size:.85rem}
.badge{position:absolute;right:16px;bottom:16px;width:120px}
/* sections */
.section{padding:2.5rem 0}
.section.alt{background:#d2e5e5}
h1,h2,h3{color:var(--ink)}
.eyebrow{color:var(--teal-text)}
.btn{border-color:var(--ink);color:var(--ink)}.btn:hover{background:var(--ink);color:#f9eadd}
.btn-light{background:var(--ink);border-color:var(--ink);color:#f9eadd}.btn-light:hover{background:transparent;color:var(--ink)}
.cta-band{background:var(--teal);color:#f9eadd}
.cta-band h2{color:#f9eadd;font-style:italic}
.cta-band .btn-light{background:#f9eadd;border-color:#f9eadd;color:var(--teal)}.cta-band .btn-light:hover{background:transparent;color:#f9eadd}
.cta-band .btn-outline{border-color:#f9eadd;color:#f9eadd}
.page-hero{min-height:300px}.page-hero::before{background:linear-gradient(to top,rgba(68,102,102,.75),rgba(68,102,102,.1))}
.page-hero h1{font-family:var(--display);font-weight:400;font-size:clamp(2rem,5vw,3.2rem)}
.page-hero .lead{font-family:var(--script);font-style:normal;font-size:1.6rem}
.gallery{gap:6px}
.site-footer{background:var(--paper);color:var(--ink);border-top:1px solid var(--line);font-family:var(--serif);padding:2rem 0 1.2rem}
.site-footer a:hover,.f-links a:hover{color:var(--teal-text)}
.f-brand{font-family:var(--serif);font-size:.95rem;letter-spacing:0;color:var(--ink);line-height:1.5}
.f-social svg{fill:var(--ink)}.f-social a:hover svg{fill:var(--teal-text)}
.copyright{border-top-color:var(--line);color:var(--ink-soft)}
.contact-card{background:var(--cream);border-left-color:var(--teal)}
.contact-form input,.contact-form select,.contact-form textarea{background:#fffdf9;border-color:var(--line)}
.menu-card,.room{background:var(--cream)}
@media (max-width:820px){
  .header-stack .site-nav{position:static;transform:none;background:transparent;padding:0;overflow:visible}
  .header-stack .site-nav ul{flex-direction:row;flex-wrap:wrap;justify-content:center;gap:.2rem .9rem}
  .header-stack .site-nav li > a{border:0;padding:.5rem .1rem;font-size:13px}
  .header-stack .nav-toggle{display:none}
  .collage{grid-template-columns:1fr}.collage .tall img{height:360px}.collage .right{grid-template-rows:auto auto}.collage .row2{grid-template-columns:1fr}
}
"""

L = lambda ids: [(f"2649b2_{i}", "L") for i in ids]
M = lambda ids: [(f"2649b2_{i}", o) for i, o in ids]
BASKET = M([("d31ceaab180a4bb0b4d65beed5604eed~mv2.jpeg","P"),("d87cc19660a14903be1ecce9a6f820ac~mv2.jpg","L"),("1a273b135f0640b082b4660dab7a7015~mv2.jpeg","P"),("3b3e2509559c43fcbc5da556d9a73398~mv2.jpeg","L"),("fce4216ee6b24f0da3e4d490285f12d5~mv2.jpeg","L"),("5b284827f3774276a018e668aac2b664~mv2.jpeg","L"),("45f3627a86b94f57ab1417a653f18409~mv2.jpeg","P"),("a1bd2cf008cc423db67387aafc3d1bf3~mv2.jpeg","P")])
BOUQUET = L(["93d08445d2dc429ba2f50c6a221847d6~mv2.jpeg","b12fa1162c5645deacc7e50b4b244e10~mv2.jpeg","94ec7c309bfd4811af575e506d2846f8~mv2.jpeg","82a4e10e7f884dfba3e0583a59ec0fd0~mv2.jpg","0617ca98bc2b47198ae10878570ddb52~mv2.jpeg","43fb92b7225546f5b3888c01f3f2b7a6~mv2.jpeg","a88d7c73f8bf40a99e6d896d2f955274~mv2.jpeg","45a442721dbd4869aa8ac8f20baa7c8e~mv2.jpeg"])
ORCHID = M([("1120698b90804d21bcb0d55bddb1b634~mv2.jpg","P"),("09911a0c14324bbdbd28f1afe00f3636~mv2.jpg","P"),("056794cba56e4755b6b776c73734cf9d~mv2.jpg","P"),("9054181a05da4d88a4b3928b769d5757~mv2.jpg","L"),("dc4dbbeb56f84227ba5b7f25877fad7c~mv2.jpg","P"),("d8a786fbad2340fbaf2433b05cb8c824~mv2.jpg","P"),("b500e497f0ac4bfcaec6285d1333192c~mv2.jpg","P"),("20fd2a89a5b14b7a876bb31006147526~mv2.jpg","P")])
GARDEN = M([("46c480252bd646ab97a342b924b34146~mv2.jpg","P"),("926d1d3725bb4d4a853244a1ca7bc81b~mv2.jpeg","L"),("95f605b00f3f49b6845ed7074266fc22~mv2.jpeg","P"),("c811c03a634e41469b5897f08429ecbd~mv2.jpeg","L"),("506c049da29942a39657381d3aef98e3~mv2.jpeg","P"),("fe6b49e638814c9dbb513ca9b8c9982b~mv2.jpeg","L"),("945ac5dc98c94213806ed6540cc4b7ef~mv2.jpg","L"),("8e174f5fcb7d45a2a779e040a28bc89e~mv2.jpeg","P"),("7004d402a2fb42c19096d3ba58ba9e6f~mv2.jpg","L"),("a2bab69af7684509b4a38e681ba9ec8c~mv2.jpeg","L"),("cc9933c732cc4d38a9d9dc8c25dbfd1d~mv2.jpg","L"),("233c8e2f2396414e8a5a3387801e827e~mv2.jpg","L"),("d2dc6184b20e4c6684d6b27c01ae5e92~mv2.jpg","P")])
FIRST = L(["ee94671c80f442af873287e8655c0ea7~mv2_d_4080_2720_s_4_2.jpg","2275c0701e184c5c9eb251f6e1be4923~mv2.jpg","f13f3601633543cf8d17d4dea515c99c~mv2_d_3931_2563_s_4_2.jpg","7b8813bde2254943862fd7bc7cef56fa~mv2.jpg","dd33516c33c345f2958cfe3d65ef98b3~mv2.jpg","067cbbccf0724c299cba02833b5488fc~mv2.jpeg","0da4a3fe651443939eccfd1d7880486f~mv2.jpg","1e9f8cdda90b46aab2ea75285213baca~mv2.jpg","dddc35318db44927b70b3e9bbf361027~mv2_d_4080_2720_s_4_2.jpg","3e361c29f45543898a1b16eac53bd589~mv2.jpg","f5d3dc60bdf04c8d9c664865d1c82ab7~mv2.jpg","974418257a1142df87f657f526bcb4bd~mv2_d_2732_2048_s_2.jpg"])

SLIDES = ["2649b2_926d1d3725bb4d4a853244a1ca7bc81b~mv2.jpeg","2649b2_c811c03a634e41469b5897f08429ecbd~mv2.jpeg","2649b2_e3b66f9f898c4d7f810bd94b3238425f~mv2.jpeg","2649b2_fe6b49e638814c9dbb513ca9b8c9982b~mv2.jpeg","2649b2_7004d402a2fb42c19096d3ba58ba9e6f~mv2.jpg"]

def band(text):
    return f'<div class="band">{text}</div>'

home = f"""
{band("Executive Luxury Wedding &amp; Flower")}
<div class="wrap" style="padding:0">
  <div class="slides" id="slides">{''.join(f'<img src="{wix(s)}" alt="" class="{"on" if i==0 else ""}">' for i, s in enumerate(SLIDES))}<div class="dots">{''.join(f'<i class="{"on" if i==0 else ""}"></i>' for i in range(len(SLIDES)))}</div></div>
  <div class="collage">
    <div class="tall"><img src="{wix('2649b2_29f82f33c7564087b22b22bc6d6d40bef000.jpg')}" alt=""></div>
    <div class="right">
      <div class="row1"><img src="{wix('2649b2_26b18ba7ff6b4c4588d754c6af4bc191~mv2.jpg')}" alt=""></div>
      <div class="row2">
        <div class="txt"><h3>디테일이 살아있는 플라워</h3><p>- Wedding 21</p><p class="tags">#세빛섬 플로팅아일랜드 &nbsp;#마리나파크<br>#스포사벨라 &nbsp;#애니버셔리 플라워</p><p>완벽한 웨딩 연출</p></div>
        <div style="position:relative"><img src="{wix('2649b2_61a33e0604794842842133f2881f4ee3~mv2.jpg')}" alt=""><img class="badge" src="images/214ec6_c2f78b9b0e49b637ef67cbf2d7e5b4b1.png" alt="BEST" onerror="this.remove()"></div>
      </div>
    </div>
  </div>
  <div class="collage" style="grid-template-columns:1fr 390px;margin-top:4px">
    <div class="txt" style="padding:2.2rem 1.5rem;font-family:var(--serif)"><h3 style="font-family:var(--display);font-weight:400;font-size:1.9rem;color:#301c0d">Wedding &amp; Party</h3><h3 style="font-family:var(--script);font-weight:400;font-size:1.8rem;color:var(--gold);margin:0">Flower</h3><p style="margin-top:.8rem;font-style:italic">Since 1995</p><p>플로리스트와의 사전미팅을 통해 연출되는 웨딩 &amp; 파티 플라워는 로맨틱한 감성과 클래식한 아름다움이 살아있는 최고의 작품입니다.</p><a class="btn" href="about.html">About us</a></div>
    <div><img src="{wix('2649b2_3b3e2509559c43fcbc5da556d9a73398~mv2.jpeg')}" alt="" style="width:100%;height:295px;object-fit:cover;display:block"></div>
  </div>
</div>
{band("Executive Luxury Wedding &amp; Party")}
<script>
(function(){{var s=document.querySelectorAll('#slides img'),d=document.querySelectorAll('#slides .dots i'),i=0;if(s.length<2)return;setInterval(function(){{s[i].classList.remove('on');d[i].classList.remove('on');i=(i+1)%s.length;s[i].classList.add('on');d[i].classList.add('on')}},3500)}})();
</script>
"""

def gal_page(hero, title, lead, note, items, cls="gallery"):
    return f"""{band(title)}
{page_hero(hero, 'Anniversary Flower', title, lead)}
<section class="section"><div class="wrap"><p class="center sub">{note}</p>{gallery(items, cls)}</div></section>
{cta("주문 문의", "Anniversary Flower · 02 3443 2117", "전화 주문", "tel:0234432117", ("E-mail", f"mailto:{EMAIL}"))}"""

basket = gal_page("2649b2_3b3e2509559c43fcbc5da556d9a73398~mv2.jpeg", "Flower Basket", "Flower Basket Gift", "Anniversary Flower - Flower Basket Gift 02 3443 2117", BASKET)
bouquet = gal_page("2649b2_93d08445d2dc429ba2f50c6a221847d6~mv2.jpeg", "Flower Bouquet", "Flower Gift", "Anniversary Flower - Flower Gift 02 3443 2117", BOUQUET, "gallery cols-4")
orchid = gal_page("2649b2_9054181a05da4d88a4b3928b769d5757~mv2.jpg", "Orchid Gift", "Flower Gift", "Anniversary Flower - Flower Gift 02 3443 2117", ORCHID, "gallery cols-4")
garden = gal_page("2649b2_926d1d3725bb4d4a853244a1ca7bc81b~mv2.jpeg", "Garden Wedding", "Making dreams come true", "세빛섬 플로팅아일랜드·마리나파크 가든 웨딩 플라워 연출 — Contact to: (02) 537-2440", GARDEN)
first = gal_page("2649b2_ee94671c80f442af873287e8655c0ea7~mv2_d_4080_2720_s_4_2.jpg", "1st Party", "돌잔치 · 가족연회", "탤런트 유선, 가수 김태우, 탤런트 장영남, 아나운서 김현욱·김주하, 방송인 안선영 씨 등 많은 셀러브리티 아기의 첫 돌잔치를 담당해 온 애니버셔리 파티 &amp; 플라워 팀의 작업들", FIRST, "gallery cols-3")

about = f"""
{band("Weddings &amp; Party")}
<section class="section"><div class="wrap">
  <div class="service-grid three" style="margin-bottom:2.5rem">
    <a class="service" href="garden-wedding.html"><img src="{wix('214ec6_7f85287db99fbf2307aec1d342e1dd58.jpg')}" loading="lazy" alt=""><h3>Wedding</h3></a>
    <a class="service" href="first-party.html"><img src="{wix('2649b2_2ff7657da13740a798d45a6fc7dfabbe~mv2_d_4080_2720_s_4_2.jpg')}" loading="lazy" alt=""><h3>1st Party</h3></a>
    <a class="service" href="contact.html"><img src="{wix('2649b2_b19ffa5093074692880f0c134b178493~mv2.jpeg')}" loading="lazy" alt=""><h3>Business Party</h3></a>
  </div>
  <div class="narrow prose" style="max-width:800px;margin:0 auto">
  <p>플로리스트와의 사전미팅을 통해 연출되는 웨딩 &amp; 파티 플라워는 로맨틱한 감성과 클래식한 아름다움이 살아있는 최고의 작품입니다.</p>
  <p>세빛섬 플로팅 아일랜드, 마리나파크의 웨딩, 돌잔치, 가족연회, 기업연회 등 파티를 디자인하고 만들어온 애니버셔리 파티 &amp; 플라워 팀은 장미 꽃잎과 캔들로 꾸며지는 로맨틱 파티 셋업으로 이국적 정취가 느껴지는 파티를 준비해드립니다.</p>
  <p>GOD 김태우, 탤런트 유선, 장영남, 안선영, 아나운서 김주하, 김현욱 님 등 아기의 돌잔치를 기획하고 준비해드렸던 애니버셔리의 플라워는 디자인학 박사인 대표와 수많은 경력을 가진 디자이너, 베테랑 플라워 팀의 경험과 노하우를 바탕으로 아기와 부모 모두에게 잊을 수 없는 최고의 돌잔치를 선사해드립니다.</p>
  <p>프랑스 바스티유 데이, 미국 대사관 독립기념일, 인도·스웨덴·인도네시아 국경일 행사 등 대사관의 주요 행사와 해외 국빈 방문 만찬, 명품 브랜드와 현대·삼성 런칭 행사의 기업연회 플라워 장식을 맡아온 경험을 바탕으로 20년간 브랜드를 성장시켜 온 애니버셔리 플라워는 아름다운 컬러감이 돋보이는 환상적인 작품의 완성도와 최상품의 싱싱한 플라워만을 엄선하여 연회의 품격을 높여줍니다.</p>
  </div>
</div></section>
{cta("Executive Luxury Wedding &amp; Party", "", "Contact", "contact.html")}
"""

contact = f"""
{band("Contact")}
<section class="section"><div class="wrap split contact-split">
  <div class="split-text">
    <h2>Please feel free to contact us.</h2>
    <p>Our team is ready to give its best effort to your order.</p>
    <div class="contact-card"><h3>ANNIVERSARY FLOWER</h3><p>서울 서초구 서초동 1685-3 아크로비스타 아케이드 112-4</p><p>Tel: <a href="tel:0234432117">02-3443-2117</a><br><a href="mailto:{EMAIL}">{EMAIL}</a><br>Instagram: <a href="https://www.instagram.com/anniversaryflower" target="_blank" rel="noopener">@anniversaryflower</a></p></div>
    <div class="contact-card"><h3>FLOATING ISLAND</h3><p>Tel: <a href="tel:025372440">02-537-2440</a> · <a href="mailto:ficonvention@gmail.com">ficonvention@gmail.com</a></p><h3>MARINA PARK</h3><p>Tel: <a href="tel:025962440">02-596-2440</a> · Instagram: <a href="https://www.instagram.com/marinaparkwedding" target="_blank" rel="noopener">@marinaparkwedding</a></p></div>
  </div>
  {contact_form(EMAIL, ["Flower Basket", "Flower Bouquet", "Orchid Gift", "Wedding Flower", "1st Party / 돌잔치", "Business Party", "기타 / Other"])}
</div></section>
<section class="map-section"><iframe title="Anniversary Flower 위치" src="https://www.google.com/maps?q=%EC%84%9C%EC%9A%B8+%EC%84%9C%EC%B4%88%EA%B5%AC+%EC%84%9C%EC%B4%88%EB%8F%99+1685-3+%EC%95%84%ED%81%AC%EB%A1%9C%EB%B9%84%EC%8A%A4%ED%83%80&output=embed" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade"></iframe></section>
"""

PAGES = {
    "index.html": ("Anniversary Flower", home, False),
    "about.html": ("About us", about, False),
    "flower-basket.html": ("Flower Basket", basket, False),
    "flower-bouquet.html": ("Flower Bouquet", bouquet, False),
    "orchid-gift.html": ("Orchid Gift", orchid, False),
    "garden-wedding.html": ("Garden Wedding", garden, False),
    "first-party.html": ("1st Party", first, False),
    "contact.html": ("Contact", contact, False),
}

EXTRA_CSS = """
.service-grid.three{grid-template-columns:repeat(3,1fr)}
.gallery.cols-4{grid-template-columns:repeat(4,1fr);grid-auto-rows:240px}
.gallery.cols-4 .g-item.portrait{grid-row:span 1}
.contact-card+.contact-card{margin-top:1rem}
@media (max-width:820px){.service-grid.three{grid-template-columns:1fr}.gallery.cols-4{grid-template-columns:repeat(2,1fr);grid-auto-rows:200px}}
"""

if __name__ == "__main__":
    build(SITE, PAGES, os.path.dirname(os.path.abspath(__file__)), THEME + EXTRA_CSS)
