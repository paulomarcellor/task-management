document.getElementById('btn__new__task').addEventListener('click', function() {
    var formContainer = document.querySelector('.form__newtask');
    var taskList = document.querySelector('.tasks__list');

    // Alterna a exibição do formulário
    if (formContainer.style.display === 'none') {
        formContainer.style.display = 'block';
        taskList.style.display = 'none'; // Esconde o botão
    } else {
        formContainer.style.display = 'none';
        taskList.style.display = 'block'; // Mostra o botão
    }
});