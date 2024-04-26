document.addEventListener("DOMContentLoaded", function() {
    // Seleciona o botão de nova tarefa
    var btnNewStep = document.querySelectorAll('.tasks__list__table__body__item__steps__addstep');

    // Adiciona um evento de clique ao botão de nova tarefa
    btnNewStep.forEach((btn) => {
        btn.addEventListener('click', function() {
            // Exibe o pop-up
            document.querySelector('.popup__steps').style.display = 'inline-block';
            // document.querySelector('.form__newtask').style.display = 'block';
        });
    })

    // Adiciona um evento de clique ao botão de fechar o pop-up
    document.querySelector('.close__popup__step').addEventListener('click', function() {
        closePopup();
    });

    // Adiciona um evento de clique ao pressionar a tecla "Escape"
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            closePopup();
        }
    });

    // Função para fechar o pop-up
    function closePopup() {
        document.querySelector('.popup__steps').style.display = 'none';
    }
});
