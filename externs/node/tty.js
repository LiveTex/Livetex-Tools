

/**
 * @type {Object.<string,*>}
 */
var tty = {};

/**
 * @param {*} fd
 * @return {boolean}
 */
tty.isatty = function(fd) {};

/**
 * @param {boolean} mode
 */
tty.setRawMode = function(mode) {};

/**
 * @constructor
 * @extends net.Socket
 */
tty.ReadStream = function() {};

/**
 * @type {boolean}
 */
tty.ReadStream.prototype.isRaw;

/**
 * @param {boolean} mode
 */
tty.ReadStream.prototype.setRawMode = function(mode) {};

/**
 * @constructor
 * @extends net.Socket
 */
tty.WriteStream = function() {};

/**
 * @type {number}
 */
tty.WriteStream.prototype.columns;

/**
 * @type {number}
 */
tty.WriteStream.prototype.rows;
