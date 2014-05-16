

/**
 * @param {string} encoding
 * @constructor
 */
var StringDecoder = function(encoding) {};

/**
 * @param {buffer.Buffer} buffer
 * @return {string}
 */
StringDecoder.prototype.write = function(buffer) {};

/**
 * @return {string}
 */
StringDecoder.prototype.toString = function() {};

/**
 * @param {buffer.Buffer} buffer
 * @return {number}
 */
StringDecoder.prototype.detectIncompleteChar = function(buffer) {};

/**
 * @param {buffer.Buffer} buffer
 * @return {string}
 */
StringDecoder.prototype.end = function(buffer) {};
