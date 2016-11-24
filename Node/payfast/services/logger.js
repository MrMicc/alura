/**
 * Created by ter00409 on 24/11/2016.
 */
var winston = require('winston');
var fs = require('fs');
winston.emitErrs = true;

/*
Se nao existe a pasta logs cria...
 */
if(!fs.existsSync('../logs')){
    fs.mkdir('../logs');
}

var logger = new winston.Logger({
        transports : [
            new winston.transports.File({
                level: 'info',
                filename: '../logs/paysfast.log',
                handleExceptions: true,
                json: true,
                maxsize: 5242880, //5MB
                maxFiles: 5,
                colorize: false
            }),
            new winston.transports.Console({
                level: 'debug',
                handleExceptions: true,
                json: false,
                colorize: true
            })
        ]

    }
);


module.exports = logger;
module.exports.stream = {
    write: function(message, encoding){
        logger.info(message);
    }
};