document.getElementById('task-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita o envio padrão do formulário

    var form = this;
    var formData = new FormData(form); // Obtém os dados do formulário
    
    // Envia uma solicitação POST assíncrona
    fetch('http://localhost:8000/api/datatasks/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': '{{ csrf_token }}' // Adiciona o token CSRF ao cabeçalho da solicitação
        }
    })
    .then(function(response) {
        if (response.ok) {
            // Se a resposta for bem-sucedida, mostra a mensagem de sucesso e limpa o formulário
            document.querySelector('.success-message').style.display = 'block';
            form.reset();
        } else {
            // Se houver um erro na resposta, mostra uma mensagem de erro
            alert('Error submitting task!');
        }
    })
    .catch(function(error) {
        // Se houver um erro durante a solicitação, mostra uma mensagem de erro
        console.error('Error:', error);
        alert('Error submitting task!');
    });
});