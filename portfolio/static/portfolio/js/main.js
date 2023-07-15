addEventListener("DOMContentLoaded", (event) => {
    window.addEventListener("load", (event) => {

        let trigger_menu = document.querySelector('.trigger-menu');
        let nav = document.querySelector('nav');

        trigger_menu.addEventListener("click", function () {

            if (nav.classList.contains('nav--active')) {
                nav.classList.remove('nav--active');
                trigger_menu.classList.remove('active');
            } else {
                nav.classList.add('nav--active');
                trigger_menu.classList.add('active');

            }
        });
    });
});


function inserir(valor) {
    document.getElementById("resultado").value += valor;
}

function limpar() {
    document.getElementById("resultado").value = "";
}

function calcular() {
    var expressao = document.getElementById("resultado").value;
    var resultado = eval(expressao);
    document.getElementById("resultado").value = resultado;
}

    document.addEventListener('DOMContentLoaded', function() {
        const links = document.querySelectorAll('.dropdown-content a[data-section]');
        links.forEach(function(link) {
            link.addEventListener('click', function(event) {
                event.preventDefault();
                const sectionId = this.getAttribute('data-section');
                const section = document.getElementById(sectionId);
                if (section) {
                    section.scrollIntoView({ behavior: 'smooth' });
                }
            });
        });
    });