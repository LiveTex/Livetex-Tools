

/**
 * @namespace
 */
var fs = {};


/**
 * @param {string} filename
 * @param {(!Object|string)=} opt_options
 * @return {string}
 */
fs.readFileSync = function(filename, opt_options) {};


/**
 * @param {string} filename
 * @param {function(Error, !Buffer)} callback
 */
fs.readFile = function(filename, callback) {};


/**
 * @param {string} filename
 * @param {*} data
 * @param {function(?)} callback
 * @param {Object=} opt_options
 */
fs.writeFile  = function(filename, data, callback, opt_options) {};


/**
 * @param {string} filename
 * @param {string|!Buffer} data
 * @param {string=} opt_encoding
 */
fs.writeFileSync = function(filename, data, opt_encoding) {};


/**
 * @param {string} filename
 * @return {boolean}
 */
fs.existsSync = function(filename) {};


/**
 * @param {string} filename
 */
fs.unlinkSync = function(filename) {};


/**
 * @param {string} filename
 * @param {!Object} options
 * @param {function(string, string)} listener
 */
fs.watchFile = function(filename, options, listener) {};


/**
 * @param {string} filename
 * @param {!Object=} opt_options
 * @param {function(string, string)=} opt_listener
 */
fs.watch = function(filename, opt_options, opt_listener) {};
