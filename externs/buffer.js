


/**
 * @param {(number|string|!Array.<number>)} sizeOrData
 * @param {string=} opt_encoding
 * @constructor
 */
var Buffer = function(sizeOrData, opt_encoding) {};


/**
 * @param {string} string
 * @return {number}
 */
Buffer.byteLength = function(string) {};


/**
 * @param {!Array.<!Buffer>} list
 * @param {number=} opt_totalLength
 * @return {!Buffer}
 */
Buffer.concat = function(list, opt_totalLength) {};


/**
 * @type {number}
 */
Buffer.prototype.length = 0;


/**
 * @param {number=} opt_start
 * @param {number=} opt_end
 * @return {!Buffer}
 */
Buffer.prototype.slice = function(opt_start, opt_end) {};


/**
 *
 * @param {string} string
 * @param {number=} opt_offset
 * @param {number=} opt_length
 * @param {string=} opt_encoding
 */
Buffer.prototype.write = function(string, opt_offset, opt_length, opt_encoding) {};


/**
 * @param {!Buffer} target
 * @param {number=} opt_targetStart
 * @param {number=} opt_sourceStart
 * @param {number=} opt_sourceEnd
 */
Buffer.prototype.copy =
  function(target, opt_targetStart, opt_sourceStart, opt_sourceEnd) {};


/**
 * @param {string=} opt_encoding
 * @param {number=} opt_start
 * @param {number=} opt_end
 * @return {string}
 */
Buffer.prototype.toString = function(opt_encoding, opt_start, opt_end) {};


/**
 * @param {number} value
 * @param {number} offset
 * @param {boolean=} opt_noAssert
 */
Buffer.prototype.writeUInt32LE = function(value, offset, opt_noAssert) {};


/**
 * @param {number} value
 * @param {number} offset
 * @param {boolean=} opt_noAssert
 */
Buffer.prototype.writeUInt32BE = function(value, offset, opt_noAssert) {};


/**
 * @param {number} value
 * @param {number} offset
 * @param {boolean=} opt_noAssert
 */
Buffer.prototype.writeInt32LE = function(value, offset, opt_noAssert) {};


/**
 * @param {number} value
 * @param {number} offset
 * @param {boolean=} opt_noAssert
 */
Buffer.prototype.writeInt32BE = function(value, offset, opt_noAssert) {};
