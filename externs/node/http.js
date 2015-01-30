



/**
 * @namespace
 */
var http = {};


/**
 * @param {function(!http.IncomingMessage,
 *  !http.ServerResponse)=} opt_requestHandler
 * @return {!http.Server}
 */
http.createServer = function(opt_requestHandler) {};


/**
 * @param {!Object} options
 * @param {Function=} opt_callback
 */
http.request = function(options, opt_callback) {};


/**
 * @constructor
 * @param {{maxSockets: number}=} opt_options
 */
http.Agent = function(opt_options) {};


/**
 * @type {!http.Agent}
 */
http.globalAgent;


/**
 * @constructor
 * @extends {events.EventEmitter}
 */
http.Server = function() {};


/**
 * @param {number} port
 * @param {string|function()=} opt_host
 * @param {function()=} opt_callback
 */
http.Server.prototype.listen = function(port, opt_host, opt_callback) {};


http.Server.prototype.close = function() {};


/**
 * @constructor
 * @implements {IReadableStream}
 * @extends {events.EventEmitter}
 */
http.IncomingMessage = function() {};


/**
 * @type {!Object.<string, string>}
 */
http.IncomingMessage.prototype.headers = {};


/**
 * @type {!net.Socket}
 */
http.IncomingMessage.prototype.connection;


/**
 * @type {string}
 */
http.IncomingMessage.prototype.method = '';


/**
 * @type {string}
 */
http.IncomingMessage.prototype.url = '';


http.IncomingMessage.prototype.resume = function() {};


http.IncomingMessage.prototype.pause = function() {};


/**
 * @param {string} event Событие.
 * @param {function(!Object)} callback Обработчик результата.
 */
http.IncomingMessage.prototype.on = function(event, callback) {};


/**
 * @constructor
 * @extends {events.EventEmitter}
 * @implements {IWritableStream}
 */
http.ServerResponse = function() {};


/**
 * @param {!Buffer|string} bufferOrString
 * @param {string=} opt_encoding
 */
http.ServerResponse.prototype.write = function(bufferOrString, opt_encoding) {};


/**
 * @param {(!Buffer|string)=} opt_bufferOrString
 * @param {string=} opt_encoding
 */
http.ServerResponse.prototype.end = function(opt_bufferOrString, opt_encoding) {};


/**
 * @param {string} name
 * @param {string} value
 */
http.ServerResponse.prototype.setHeader = function(name, value) {};


/**
 * @param {number} code
 * @param {!Object=} opt_headers
 */
http.ServerResponse.prototype.writeHead = function(code, opt_headers) {};


/**
 * @type {number}
 */
http.ServerResponse.prototype.statusCode = 200;


/**
 * @type {!Object}
 */
http.ServerResponse.prototype.headers;


