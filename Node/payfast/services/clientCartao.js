/**
 * Created by luizmiccieli on 19/11/16.
 */
var restify = require('restify');

function ClientCartao() {
    this._client = restify.createJSONClient({
        url: 'http://localhost:3001'
    });
}


ClientCartao.prototype.autoriza = function (cartao, callback) {
    this._client.post('/cartoes/autoriza',cartao,callback);
    
};

module.exports = function () {
    return ClientCartao;
};



