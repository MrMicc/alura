/**
 * Created by luizmiccieli on 17/11/16.
 */

function PagamentoDAO(connection){
    this._connection  = connection;
}

PagamentoDAO.prototype.salva = function (pagamento, callback) {
    this._connection.query('INSERT INTO pagamentos SET ?',pagamento,callback);
};

PagamentoDAO.prototype.lista = function (callback) {
    this._connection.query('SELECT * FROM pagamentos', callback);
};

PagamentoDAO.prototype.getByID = function (pagamento, callback) {
    this._connection.query('SELECT * FROM pagamentos WHERE ID = ?', pagamento.id, callback);
};

module.exports = function () {
    return PagamentoDAO;
}