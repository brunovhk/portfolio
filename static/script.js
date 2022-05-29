/* Abre e fecha o menu lateral em modo mobile */

const menuMobile = document.querySelector(".menu-mobile");
const body = document.querySelector("body");
const logo = document.querySelectorAll('#logo path')

menuMobile.addEventListener("click", () => {
    menuMobile.classList.contains("bi-list")
        ? menuMobile.classList.replace("bi-list", "bi-x")
        : menuMobile.classList.replace("bi-x", "bi-list");
    body.classList.toggle("menu-nav-active");
});
// Descrição das badges
$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})
// Fecha o menu quando clicar em alguma seção e altera o ícone

const navItem = document.querySelectorAll('.nav-item');

navItem.forEach(item => {
    item.addEventListener("click", () => {
        body.classList.contains("menu=nav-active")
            ? body.classList.remove("manu-nav-active") : body.classList.replace("bi-x", "bi-list");
        body.classList.toggle("menu-nav-active");
    });
})

// Animar os itens com atributo data-anime

const item = document.querySelectorAll("[data-anime]");

const animeScroll = () => {
    const windowTop = window.pageYOffset + window.innerHeight * 0.85;

    item.forEach((element) => {
        if (windowTop > element.offsetTop) {
            element.classList.add("animate");
        } else {
            element.classList.remove("animate");
        }
    });
};

animeScroll();

window.addEventListener("scroll", () => {
    animeScroll();
})
// Ativar loading no botão de enviar o formulário

const btnEnviar = document.querySelector('#btn-enviar')
const btnEnviarLoader = document.querySelector('#btn-enviar-loader')

btnEnviar.addEventListener("click", () =>{
    btnEnviarLoader.style.display = "block";
    btnEnviar.style.display = "none"
})
// Remove o alert após 5s
setTimeout(()=> {
    document.querySelector('#alerta').style.display = 'none';
}, 5000)
// Logo
for (let i = 0; i < logo.length; i++){
    console.log(`Letter ${i} is ${logo[i].getTotalLength()}`);
}