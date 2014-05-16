

/**
 * @type {Object.<string,*>}
 */
var dgram = {};

/**
 * @param {string} type
 * @param {function(...)=} callback
 * @return {dgram.Socket}
 */
dgram.createSocket = function(type, callback) {};

/**
 * @constructor
 * @extends events.EventEmitter
 */
dgram.Socket = function() {};

/**
 * @param {buffer.Buffer} buf
 * @param {number} offset
 * @param {number} length
 * @param {number} port
 * @param {string} address
 * @param {function(...)=} callback
 */
dgram.Socket.prototype.send = function(buf, offset, length, port, address,
                                       callback) {};

/** 
 * @param {number} port
 * @param {string=} address
 */
dgram.Socket.prototype.bind = function(port, address) {};

/**
 */
dgram.Socket.prototype.close = function() {};

/**
 * @return {string}
 */
dgram.Socket.prototype.address = function() {};

/**
 * @param {boolean} flag
 */
dgram.Socket.prototype.setBroadcast = function(flag) {};

/**
 * @param {number} ttl
 * @return {number}
 */
dgram.Socket.prototype.setTTL = function(ttl) {};

/**
 * @param {number} ttl
 * @return {number}
 */
dgram.Socket.prototype.setMulticastTTL = function(ttl) {};

/**
 * @param {boolean} flag
 */
dgram.Socket.prototype.setMulticastLoopback = function(flag) {};

/**
 * @param {string} multicastAddress
 * @param {string=} multicastInterface
 */
dgram.Socket.prototype.addMembership = function(multicastAddress,
                                                multicastInterface) {};

/**
 * @param {string} multicastAddress
 * @param {string=} multicastInterface
 */
dgram.Socket.prototype.dropMembership = function(multicastAddress,
                                                 multicastInterface) {};
