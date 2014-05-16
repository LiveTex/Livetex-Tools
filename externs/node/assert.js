

/**
 * @param {*} value
 * @param {string} message
 * @throws {assert.AssertionError}
 */
var assert = function(value, message) {};


/**
 * @param {{message: string, actual: *, expected: *, operator: string}} options
 * @constructor
 * @extends Error
 */
assert.AssertionError = function(options) {};


/**
 * @return {string}
 */
assert.AssertionError.prototype.toString = function() {};


/**
 * @param {*} value
 * @param {string=} message
 * @throws {assert.AssertionError}
 */
assert.ok = function(value, message) {};


/**
 * @param {*} actual
 * @param {*} expected
 * @param {string} message
 * @param {string} operator
 * @throws {assert.AssertionError}
 */
assert.fail = function(actual, expected, message, operator) {};


/**
 * @param {*} actual
 * @param {*} expected
 * @param {string} message
 * @throws {assert.AssertionError}
 */
assert.equal = function(actual, expected, message) {};


/**
 * @param {*} actual
 * @param {*} expected
 * @param {string} message
 * @throws {assert.AssertionError}
 */
assert.notEqual = function(actual, expected, message) {};


/**
 * @param {*} actual
 * @param {*} expected
 * @param {string} message
 * @throws {assert.AssertionError}
 */
assert.deepEqual = function(actual, expected, message) {};


/**
 * @param {*} actual
 * @param {*} expected
 * @param {string} message
 * @throws {assert.AssertionError}
 */
assert.notDeepEqual = function(actual, expected, message) {};


/**
 * @param {*} actual
 * @param {*} expected
 * @param {string} message
 * @throws {assert.AssertionError}
 */
assert.strictEqual = function(actual, expected, message) {};


/**
 * @param {*} actual
 * @param {*} expected
 * @param {string} message
 * @throws {assert.AssertionError}
 */
assert.notStrictEqual = function(actual, expected, message) {};


/**
 * @param {function()} block
 * @param {Function|RegExp|function(*)} error
 * @param {string=} message
 * @throws {assert.AssertionError}
 */
assert.doesNotThrow = function(block, error, message) {};


/**
 * @param {*} value
 * @throws {assert.AssertionError}
 */
assert.ifError = function(value) {};

