// Esses testes devem ser rodados via Postman.
// Atenção: o nome Saltadores Ultimato está com erro de gráfia porque no arquivo de fixtures estava errado também.


pm.test("Status code is 200", function(){
    pm.response.to.have.status(200);
});

pm.test("Resposta está no formato JSON", function(){
    pm.response.to.be.json;
});

pm.test("Saltadores Utimato no body da resposta", function(){
    pm.expect(pm.response.text()).to.include("Saltadores Utimato");
});