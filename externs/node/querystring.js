

/**
 * @type {Object.<string,*>}
 */
var querystring = {};

/**
 * @param {Object.<string,*>} obj
 * @param {string=} sep
 * @param {string=} eq
 * @return {string}
 * @nosideeffects
 */
querystring.stringify = function(obj, sep, eq) {};

/**
 * @param {string} str
 * @param {string=} sep
 * @param {string=} eq
 * @param {*=} options
 * @nosideeffects
 */
querystring.parse = function(str, sep, eq, options) {};

/**
 * @param {string} str
 * @return {string}
 */
querystring.escape = function(str) {};

/**
 * @param {string} str
 * @return {string}
 */
querystring.unescape = function(str) {};

/**
 * @param {buffer.Buffer} s
 * @param {boolean} decodeSpaces
 */
querystring.unescapeBuffer = function(s, decodeSpaces) {};
