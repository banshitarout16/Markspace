document.documentElement.classList.add('js');

const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
}, { threshold: 0.2 });

document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// class size slider
const qsRange = document.getElementById('qsRange');
if (qsRange) {
    const people = n => '<i class="p"></i>'.repeat(Math.min(n, 60));
    const fmt = s => s < 60 ? s + ' sec' : (Math.round(s / 6) / 10) + ' min';
    const update = () => {
        const n = +qsRange.value;
        document.getElementById('qsCount').textContent = n;
        document.getElementById('qsOldPeople').innerHTML = people(n);
        document.getElementById('qsNewPeople').innerHTML = people(n);
        document.getElementById('qsOldTime').textContent = fmt(n * 5);
    };
    qsRange.addEventListener('input', update);
    update();
}