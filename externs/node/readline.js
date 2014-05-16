

/**
 * @type {Object.<string,*>}
 */
var readline = {};

/**
 * @param {{
 * input: stream.ReadableStream,
 * output: stream.WritableStream,
 * completer: function(string, function(*, Array)=),
 * terminal: boolean
 * }} options
 * @return {readline.Interface}
 */
readline.createInterface = function(options) {};

/**
 * @constructor
 * @extends events.EventEmitter
 */
readline.Interface = function() {};

/**
 * @param {string} prompt
 * @param {number} length
 */
readline.Interface.prototype.setPrompt = function(prompt, length) {};

/**
 * @param {boolean=} preserveCursor
 */
readline.Interface.prototype.prompt = function(preserveCursor) {};

/**
 * @param {string} query
 * @param {function(string)} callback
 */
readline.Interface.prototype.question = function(query, callback) {};

/**
 */
readline.Interface.prototype.pause = function() {};

/**
 */
readline.Interface.prototype.resume = function() {};

/**
 */
readline.Interface.prototype.close = function() {};

/**
 * @param {string} data
 * @param {Object.<string,*>=} key
 */
readline.Interface.prototype.write = function(data, key) {};
