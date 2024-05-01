function displayFinances(finances) {
    const listFinances = document.getElementById('list_finances');
    listFinances.innerHTML = '';
    finances.forEach(finance => {
        const li = document.createElement('li');
        li.textContent = `${finance.title}: ${finance.description}`;
        listFinances.appendChild(li);
    });
}


fetch('http://127.0.0.1:8000/finances/historic/')
    .then(Response => Response.json())
    .then(data => {
        displayFinances(data);
    })
    .catch(error => console.error('Erro ao buscar histórico:', error))
