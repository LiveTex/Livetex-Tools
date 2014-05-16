

/**
 * @type {Object.<string,*>}
 */
var tls = {};

/**
 * @typedef {{
 * pfx: (string|buffer.Buffer),
 * key: (string|buffer.Buffer),
 * passphrase: string,
 * cert: (string|buffer.Buffer),
 * ca: Array.<string|buffer.Buffer>,
 * crl: (string|Array.<string>),
 * ciphers: string,
 * honorCipherOrder: boolean,
 * requestCert: boolean,
 * rejectUnauthorized: boolean,
 * NPNProtocols: (Array|buffer.Buffer),
 * SNICallback: function(string),
 * sessionIdContext: string
 * }}
 */
tls.CreateOptions;

/**
 * 
 * @param {tls.CreateOptions} options
 * @param {function(...)=} secureConnectionListener
 * @return {tls.Server}
 */
tls.createServer = function(options, secureConnectionListener) {};

/**
 * @typedef {{
 * host: string,
 * port: number,
 * socket: *,
 * pfx: (string|buffer.Buffer),
 * key: (string|buffer.Buffer),
 * passphrase: string,
 * cert: (string|buffer.Buffer),
 * ca: Array.<string>,
 * rejectUnauthorized: boolean,
 * NPNProtocols: Array.<string|buffer.Buffer>,
 * servername: string
 * }}
 */
tls.ConnectOptions;

/**
 * 
 * @param {number|tls.ConnectOptions} port
 * @param {(string|tls.ConnectOptions|function(...))=} host
 * @param {(tls.ConnectOptions|function(...))=} options
 * @param {function(...)=} callback
 */
tls.connect = function(port, host, options, callback) {};

/**
 * @param {crypto.Credentials=} credentials
 * @param {boolean=} isServer
 * @param {boolean=} requestCert
 * @param {boolean=} rejectUnauthorized
 * @return {tls.SecurePair}
 */
tls.createSecurePair = function(credentials, isServer, requestCert,
                                rejectUnauthorized) {};

/**
 * @constructor
 * @extends events.EventEmitter
 */
tls.SecurePair = function() {};

/**
 * @constructor
 * @extends net.Server
 */
tls.Server = function() {};

/**
 * @param {string} hostname
 * @param {string|buffer.Buffer} credentials
 */
tls.Server.prototype.addContext = function(hostname, credentials) {};

/**
 * @constructor
 * @extends stream.Duplex
 */
tls.CleartextStream = function() {};

/**
 * @type {boolean}
 */
tls.CleartextStream.prototype.authorized;

/**
 * @type {?string}
 */
tls.CleartextStream.prototype.authorizationError;

/**
 * @return {Object.<string,(string|Object.<string,string>)>}
 */
tls.CleartextStream.prototype.getPeerCertificate = function() {};

/**
 * @return {{name: string, version: string}}
 */
tls.CleartextStream.prototype.getCipher = function() {};

/**
 * @return {{port: number, family: string, address: string}}
 */
tls.CleartextStream.prototype.address = function() {};

/**
 * @type {string}
 */
tls.CleartextStream.prototype.remoteAddress;

/**
 * @type {number}
 */
tls.CleartextStream.prototype.remotePort;
