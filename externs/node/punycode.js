

/**
 * @type {Object.<string,*>}
 */
var punycode = {};

/**
 * @param {string} string
 * @return {string}
 */
punycode.decode = function(string) {};

/**
 * @param {string} string
 * @return {string}
 */
punycode.encode = function(string) {};

/**
 * @param {string} domain
 * @return {string}
 */
punycode.toUnicode = function(domain) {};

/**
 * @param {string} domain
 * @return {string}
 */
punycode.toASCII = function(domain) {};

/**
 * @type {Object.<string,*>}
 */
punycode.ucs2 = {};

/**
 * @param {string} string
 * @return {Array.<number>}
 */
punycode.ucs2.decode = function(string) {};

/**
 * @param {Array.<number>} codePoints
 * @return {string}
 */
punycode.ucs2.encode = function(codePoints) {};

/**
 * @type {string}
 */
punycode.version;
