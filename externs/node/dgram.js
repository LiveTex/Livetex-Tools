


/**
 * @namespace
 */
var dgram = {};

/**
 * @param {string} protocol
 * @return {!dgram.Socket}
 */
dgram.createSocket = function(protocol) {};

/**
 * @constructor
 * @extends {events.EventEmitter}
 */
dgram.Socket = function() {};

/**
 * @param {!Buffer} buffer
 * @param {number} offset
 * @param {number} length
 * @param {number} port
 * @param {string} host
 * @param {Function=} opt_callback
 */
dgram.Socket.prototype.send = function(buffer, offset, length, port, host, opt_callback) {};


/**
 *
 */
dgram.Socket.prototype.close = function() {};

