document.addEventListener("DOMContentLoaded", function() {
    // Seleciona todas as linhas da tabela
    var tableRows = document.querySelectorAll('.tasks__list__table__body__item');

    // Adiciona um evento de clique a cada linha
    tableRows.forEach(function(row) {
        row.addEventListener('click', function() {
            // Exibe o pop-up
            document.querySelector('.popup').style.display = 'block';
        });
    });

    // Adiciona um evento de clique ao botão de fechar o pop-up
    document.querySelector('.close__popup').addEventListener('click', function() {
        // Fecha o pop-up
        document.querySelector('.popup').style.display = 'none';
    });
});