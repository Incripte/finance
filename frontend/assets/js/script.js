function carregarDados() {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                var data = JSON.parse(xhr.responseText);
                montarTabela(data);
                console.log(data)
            } else {
                console.error('Erro ao carregar os dados: ' + xhr.status);
            }
        }
        
    };
    xhr.onerror = function() {
        console.error('Erro na requisição.');
    };
    xhr.open('GET', 'http://127.0.0.1:8000/finances/historic/', true);
    xhr.send();
}

// Função para montar a tabela com os dados recebidos
function montarTabela(data) {
    var tabelaCorpo = document.getElementById('body-table');

    // Cria uma nova linha na tabela para cada objeto de renda
    data.forEach(function(item) {
        var novaLinha = document.createElement('tr');
        novaLinha.innerHTML = '<td>' + item.title + '</td>' +
                              '<td>' + item.description + '</td>' +
                              '<td>' + item.type + '</td>' +
                              '<td>' + 'R$ ' + item.value + '</td>' +
                              '<td>' + item.date + '</td>';
        tabelaCorpo.appendChild(novaLinha);
    });
}

// Chamar a função para carregar os dados quando a página carregar
window.onload = carregarDados;