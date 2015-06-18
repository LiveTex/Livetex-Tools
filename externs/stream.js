

/**
 * @interface
 * @extends {events.IEventEmitter}
 * @event data
 * @event error
 * @event end - EOF or FIN
 */
var IReadableStream = function() {};


IReadableStream.prototype.pause = function() {};


IReadableStream.prototype.resume = function() {};



/**
 * @interface
 * @extends {events.IEventEmitter}
 * @event error
 * @event close
 */
var IWritableStream = function() {};


/**
 * @param {!Buffer|string} bufferOrString
 * @param {string=} opt_encoding
 * @param {!function()=} opt_callback
 * @return {boolean}
 */
IWritableStream.prototype.write =
    function(bufferOrString, opt_encoding, opt_callback) {};


/**
 * @param {(!Buffer|string)=} opt_bufferOrString
 * @param {string=} opt_encoding
 */
IWritableStream.prototype.end = function(opt_bufferOrString, opt_encoding) {};



/**
 * @interface
 * @extends {IWritableStream}
 * @extends {IReadableStream}
 */
var IStream = function() {};


IStream.prototype.destroy = function() {};

