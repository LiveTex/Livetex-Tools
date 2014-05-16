

/**
 * @type {Object.<string,*>}
 */
var repl = {};

/**
 * @param {{
 * prompt: ?string,
 * input: ?stream.Readable,
 * output: ?stream.Writable,
 * terminal: ?boolean,
 * eval: ?function(string),
 * useColors: ?boolean,
 * useGlobal: ?boolean,
 * ignoreUndefined: ?boolean,
 * writer: ?function(string)
 * }} options
 * @return {repl.REPLServer}
 */
repl.start = function(options) {};

/**
 * @constructor
 * @extends events.EventEmitter
 */
repl.REPLServer = function() {};

/**
 * @type {Object.<string,*>}
 */
repl.REPLServer.prototype.context;
