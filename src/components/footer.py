import streamlit as st


def footer_home():

    st.html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&family=Teko:wght@300..700&family=Titan+One&display=swap');

.footer {
    width: 90%;
    max-width: 720px;
    margin: 45px auto 20px auto;
    padding: 20px 18px 14px 18px;
    background: rgba(255, 255, 255, 0.96);
    border-radius: 30px;
    text-align: center;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
}

.footer-brand {
    font-family: 'Titan One', sans-serif;
    font-size: 23px;
    color: #5865F2;
    margin-bottom: 3px;
}

.footer-tagline {
    font-family: 'Outfit', sans-serif;
    font-size: 18px;
    color: #666;
    margin-bottom: 13px;
}

.footer-links {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 8px;
    margin-bottom: 13px;
}

.footer-link {
    font-family: 'Outfit', sans-serif;
    text-decoration: none;
    color: #5865F2;
    background: #f1f2ff;
    padding: 6px 13px;
    border-radius: 18px;
    font-size: 11px;
    font-weight: 600;
    transition: 0.2s ease;
}

.footer-link:hover {
    background: #5865F2;
    color: white;
    transform: translateY(-2px);
}

.footer-divider {
    width: 65%;
    height: 1px;
    background: #e6e6e6;
    margin: 0 auto 10px auto;
}

.footer-credit {
    font-family: 'Outfit', sans-serif;
    font-size: 12px;
    color: #888;
}

.heart {
    color: #ff5c7a;
    font-size: 12px;
}
</style>

<div class="footer">
<div class="footer-brand">MarkSpace</div>
<div class="footer-tagline">The smarter way to show up.</div>




<div class="footer-divider"></div>

<div class="footer-credit">
Made with <span class="heart">♥</span> by Banshita Rout
<div class="footer-links">
<a class="footer-link" href="https://github.com/banshitarout16" target="_blank">GitHub</a>
<a class="footer-link" href="https://www.linkedin.com/in/banshita-rout16/" target="_blank">LinkedIn</a>
<a class="footer-link" href="mailto:banshitarout@gmail.com">Email</a>
</div>

</div>
</div>
""")