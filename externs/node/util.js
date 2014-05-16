

/**
 * @type {Object.<string,*>}
 */
var util = {};

/**
 * @param {string} format
 * @param {...*} var_args
 * @return {string}
 * @nosideeffects
 */
util.format = function(format, var_args) {};

/**
 * @param {string} string
 */
util.debug = function(string) {};

/**
 * @param {...*} var_args
 */
util.error = function(var_args) {};

/**
 * @param {...*} var_args
 */
util.puts = function(var_args) {};

/**
 * @param {...*} var_args
 */
util.print = function(var_args) {};

/**
 * @param {string} string
 */
util.log = function(string) {};

/**
 * @param {*} object
 * @param {boolean=} showHidden
 * @param {number=} depth
 * @param {boolean=} colors
 * @return {string}
 * @nosideeffects
 */
util.inspect = function(object, showHidden, depth, colors) {};

/**
 * @param {*} object
 * @return {boolean}
 * @nosideeffects
 */
util.isArray = function(object) {};

/**
 * @param {*} object
 * @return {boolean}
 * @nosideeffects
 */
util.isRegExp = function(object) {};

/**
 * @param {*} object
 * @return {boolean}
 * @nosideeffects
 */
util.isDate = function(object) {};

/**
 * @param {*} object
 * @return {boolean}
 * @nosideeffects
 */
util.isError = function(object) {};

/**
 * @param {stream.ReadableStream} readableStream
 * @param {stream.WritableStream} writableStream
 * @param {function(...)=} callback
 * @deprecated
 */
util.pump = function(readableStream, writableStream, callback) {};

/**
 * @param {Function} constructor
 * @param {Function} superConstructor
 */
util.inherits = function(constructor, superConstructor) {};
