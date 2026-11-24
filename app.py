from flask import Flask, render_template_string

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Bonkers Shadow",
        "category": "Streetwear",
        "price": 2499,
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=700",
        "tag": "BESTSELLER"
    },
    {
        "id": 2,
        "name": "Bonkers Air Max",
        "category": "Running",
        "price": 3299,
        "image": "https://images.unsplash.com/photo-1552346154-21d32810aba3?w=700",
        "tag": "NEW DROP"
    },
    {
        "id": 3,
        "name": "Bonkers Street Pro",
        "category": "Lifestyle",
        "price": 2799,
        "image": "https://images.unsplash.com/photo-1495555961986-6d4c1ecb7be3?w=700",
        "tag": "TRENDING"
    },
    {
        "id": 4,
        "name": "Bonkers Classic",
        "category": "Casual",
        "price": 1999,
        "image": "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=700",
        "tag": "POPULAR"
    },
    {
        "id": 5,
        "name": "Bonkers Runner",
        "category": "Running",
        "price": 2999,
        "image": "https://images.unsplash.com/photo-1539185441755-769473a23570?w=700",
        "tag": "LIMITED"
    },
    {
        "id": 6,
        "name": "Bonkers High Top",
        "category": "Streetwear",
        "price": 3499,
        "image": "https://images.unsplash.com/photo-1520256862855-398228c41684?w=700",
        "tag": "HOT"
    }
]

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BONKERS | Own Your Move</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#0a0a0a;color:#fff;font-family:Arial,sans-serif}
nav{height:78px;display:flex;align-items:center;justify-content:space-between;padding:0 7%;border-bottom:1px solid #292929;position:sticky;top:0;background:#0a0a0a;z-index:10}
.logo{font-size:29px;font-weight:1000;letter-spacing:3px}
.logo span{color:#d7ff36}
nav a{color:white;text-decoration:none;margin:0 15px;font-size:13px}
.cart{border:1px solid #d7ff36;padding:11px 17px;border-radius:25px;color:#d7ff36}
.hero{min-height:560px;padding:90px 8%;display:flex;align-items:center;justify-content:space-between;gap:30px;background:radial-gradient(circle at 75% 45%,#333 0,#111 35%,#090909 75%)}
.hero-text{max-width:550px}
.eyebrow{color:#d7ff36;letter-spacing:4px;font-size:12px;font-weight:bold}
.hero h1{font-size:clamp(55px,8vw,105px);line-height:.92;margin:25px 0;font-weight:1000;letter-spacing:-5px}
.hero h1 span{color:#d7ff36}
.hero p{color:#aaa;line-height:1.8;max-width:420px}
.btn{display:inline-block;background:#d7ff36;color:#080808;padding:16px 28px;text-decoration:none;font-weight:bold;margin-top:28px;border-radius:3px}
.hero-img{width:45%;max-width:510px;filter:drop-shadow(0 20px 35px #000)}
.hero-img img{width:100%;border-radius:20px;transform:rotate(-8deg)}
.section{padding:75px 8%}
.section-head{display:flex;justify-content:space-between;align-items:end;margin-bottom:35px}
.section h2{font-size:42px;letter-spacing:-2px}
.section h2 span{color:#d7ff36}
.muted{color:#999;font-size:13px;margin-top:10px}
.search{background:#171717;border:1px solid #333;color:white;padding:13px 16px;border-radius:5px;width:220px}
.products{display:grid;grid-template-columns:repeat(3,1fr);gap:25px}
.card{background:#151515;border:1px solid #292929;border-radius:9px;overflow:hidden;transition:.3s}
.card:hover{transform:translateY(-8px);border-color:#d7ff36}
.card img{width:100%;height:260px;object-fit:cover;background:#222}
.card-content{padding:20px}
.tag{font-size:10px;color:#d7ff36;letter-spacing:2px}
.card h3{margin:12px 0;font-size:19px}
.category{font-size:12px;color:#999}
.price-row{display:flex;justify-content:space-between;align-items:center;margin-top:20px}
.price{font-size:20px;font-weight:bold}
.add{background:#d7ff36;border:0;padding:10px 14px;font-weight:bold;cursor:pointer;border-radius:3px}
.banner{margin:20px 8% 75px;padding:65px 8%;background:#d7ff36;color:#080808;border-radius:8px}
.banner h2{font-size:clamp(35px,5vw,60px);font-weight:1000}
.banner p{margin-top:12px}
footer{border-top:1px solid #292929;padding:35px 8%;display:flex;justify-content:space-between;color:#888;font-size:12px}
@media(max-width:800px){
nav{padding:0 5%}nav a{margin:0 5px}.hero{flex-direction:column;padding:65px 7%}.hero-img{width:90%}
.products{grid-template-columns:repeat(2,1fr)}
.section-head{gap:20px;flex-direction:column;align-items:start}
}
@media(max-width:520px){
nav{height:auto;padding:20px 5%;flex-wrap:wrap;gap:15px}
nav .links{order:3;width:100%;display:flex;justify-content:space-between}
.products{grid-template-columns:1fr}
.card img{height:280px}
.section h2{font-size:34px}
footer{flex-direction:column;gap:15px}
}
</style>
</head>
<body>

<nav>
  <div class="logo">BONKERS<span>.</span></div>
  <div class="links">
    <a href="#home">HOME</a>
    <a href="#collection">COLLECTION</a>
    <a href="#about">ABOUT</a>
  </div>
  <div class="cart">BAG (<span id="count">0</span>)</div>
</nav>

<section class="hero" id="home">
  <div class="hero-text">
    <div class="eyebrow">NOT MADE TO BLEND IN.</div>
    <h1>OWN<br>YOUR <span>MOVE.</span></h1>
    <p>Step into a world where comfort meets confidence.
       Discover sneakers designed for those who make their own rules.</p>
    <a href="#collection" class="btn">EXPLORE COLLECTION ↗</a>
  </div>
  <div class="hero-img">
    <img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=900" alt="Red sneaker">
  </div>
</section>

<section class="section" id="collection">
  <div class="section-head">
    <div>
      <div class="eyebrow">FRESH FROM THE STREET</div>
      <h2>THE <span>COLLECTION.</span></h2>
      <p class="muted">Find your pair. Define your style.</p>
    </div>
    <input class="search" id="search" placeholder="Search sneakers..." oninput="filterProducts()">
  </div>

  <div class="products" id="products">
    {% for p in products %}
    <div class="card" data-name="{{ p.name|lower }}">
      <img src="{{ p.image }}" alt="{{ p.name }}">
      <div class="card-content">
        <div class="tag">{{ p.tag }}</div>
        <h3>{{ p.name }}</h3>
        <div class="category">{{ p.category }}</div>
        <div class="price-row">
          <div class="price">₹{{ "{:,}".format(p.price) }}</div>
          <button class="add" onclick="addToCart()">ADD +</button>
        </div>
      </div>
    </div>
    {% endfor %}
  </div>
</section>

<section class="banner" id="about">
  <div class="eyebrow" style="color:#222">THE BONKERS ATTITUDE</div>
  <h2>WALK DIFFERENT.<br>LIVE DIFFERENT.</h2>
  <p>It's not just footwear. It's your statement.</p>
</section>

<footer>
  <div class="logo">BONKERS<span>.</span></div>
  <div>© 2026 BONKERS. DEMO STORE.</div>
  <div>OWN YOUR MOVE.</div>
</footer>

<script>
let cartCount = 0;

function addToCart(){
  cartCount++;
  document.getElementById("count").innerText = cartCount;
  alert("Added to your demo shopping bag!");
}

function filterProducts(){
  let query = document.getElementById("search").value.toLowerCase();
  document.querySelectorAll(".card").forEach(card => {
    card.style.display = card.dataset.name.includes(query) ? "" : "none";
  });
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
