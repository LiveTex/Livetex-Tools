

var https = {};

/**
 * @constructor
 * @extends tls.Server
 */
https.Server = function() {};

/**
 * @param {...*} var_args
 */
https.Server.prototype.listen = function(var_args) {};

/**
 * @param {function()=} callback
 */
https.Server.prototype.close = function(callback) {};

/**
 * @param {tls.CreateOptions} options
 * @param {function(http.IncomingMessage, http.ServerResponse)=} requestListener
 */
https.createServer = function(options, requestListener) {};

/**
 * @typedef {{
 * host: ?string,
 * hostname: ?string,
 * port: ?number,
 * method: ?string,
 * path: ?string,
 * headers: ?Object.<string,string>,
 * auth: ?string,
 * agent: ?(https.Agent|boolean),
 * pfx: ?(string|buffer.Buffer),
 * key: ?(string|buffer.Buffer),
 * passphrase: ?string,
 * cert: ?(string|buffer.Buffer),
 * ca: ?Array.<string>,
 * ciphers: ?string, rejectUnauthorized: ?boolean}}
 */
https.ConnectOptions;

/**
 * @param {https.ConnectOptions|string} options
 * @param {function(http.IncomingMessage)} callback
 * @return {http.ClientRequest}
 */
https.request = function(options, callback) {};

/**
 * @param {https.ConnectOptions|string} options
 * @param {function(http.IncomingMessage)} callback
 * @return {http.ClientRequest}
 */
https.get = function(options, callback) {};

/**
 * @constructor
 * @extends http.Agent
 */
https.Agent = function() {};

/**
 * @type {https.Agent}
 */
https.globalAgent;
