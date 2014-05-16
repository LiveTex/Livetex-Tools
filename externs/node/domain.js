

/**
 * @type {Object.<string,*>}
 */
var domain = {};

/**
 * @type {domain.Domain}
 */
domain.active;

/**
 * @return {domain.Domain}
 */
domain.create = function() {};

/**
 * @constructor
 * @extends events.EventEmitter
 */
domain.Domain = function() {};

/**
 * @param {function()} fn
 */
domain.Domain.prototype.run = function(fn) {};

/**
 * @type {Array}
 */
domain.Domain.prototype.members;

/**
 * @param {events.EventEmitter} emitter
 */
domain.Domain.prototype.add = function(emitter) {};

/**
 * @param {events.EventEmitter} emitter
 */
domain.Domain.prototype.remove = function(emitter) {};

/**
 * @param {function(...[*])} callback
 * @return {function(...[*])}
 */
domain.Domain.prototype.bind = function(callback) {};

/**
 * @param {function(...[*])} callback
 * @return {function(...[*])}
 */
domain.Domain.prototype.intercept = function(callback) {};

/**
 */
domain.Domain.prototype.dispose = function() {};

// Undocumented

/**
 */
domain.Domain.prototype.enter = function() {};

/**
 */
domain.Domain.prototype.exit = function() {};
