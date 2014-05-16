

/**
 * @type {Object.<string,function(*, ...[*])>}
 */
var console = {};

/**
 * @param {*} data
 * @param {...*} var_args
 */
console.log = function(data, var_args) {};

/**
 * @param {*} data
 * @param {...*} var_args
 */
console.info = function(data, var_args) {};

/**
 * @param {*} data
 * @param {...*} var_args
 */
console.error = function(data, var_args) {};

/**
 * @param {*} data
 * @param {...*} var_args
 */
console.warn = function(data, var_args) {};

/**
 * @param {*} obj
 */
console.dir = function(obj) {};

/**
 * @param {*} label
 */
console.time = function(label) {};

/**
 * @param {*} label
 */
console.timeEnd = function(label) {};

/**
 * @param {*} label
 */
console.trace = function(label) {};

/**
 * @param {*} expression
 * @param {*} message
 * @throws {assert.AssertionError}
 */
console.assert = function(expression, message) {};
