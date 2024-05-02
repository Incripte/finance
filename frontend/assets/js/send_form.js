// Função para lidar com o envio do formulário
function enviarFormulario(event) {
    event.preventDefault(); // Evita que o formulário seja enviado da maneira padrão

    // Obter os valores dos campos do formulário
    var title = document.getElementById('title').value;
    var description = document.getElementById('description').value;
    var type = document.getElementById('type').value;
    var value = document.getElementById('value').value;
    var date = document.getElementById('date').value;

    // Objeto com os dados do lançamento
    var lancamento = {
        title: title,
        description: description,
        type: type,
        value: value,
        date: date
    };

    // Enviar os dados do lançamento para o backend
    fetch('http://127.0.0.1:8000/finances/income/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(lancamento)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro ao criar lançamento');
        }
        return response.json();
    })
    .then(data => {
        // Se o lançamento foi criado com sucesso, faça algo com os dados de resposta (se houver)
        console.log('Lançamento criado:', data);
        // Limpar os campos do formulário
        document.getElementById('form-lancamento').reset();
    })
    .catch(error => {
        // Se houver um erro, trate-o aqui
        console.error(error);
    });
}

// Adicionar um event listener para o envio do formulário
document.getElementById('form-lancamento').addEventListener('submit', enviarFormulario);