

/**
 * @type {Object.<string,*>}
 */
var vm = {};

/**
 * @constructor
 */
vm.Context = function() {};

/**
 * @param {string} code
 * @param {string=} filename
 */
vm.runInThisContext = function(code, filename) {};

/**
 * @param {string} code
 * @param {Object.<string,*>=} sandbox
 * @param {string=} filename
 */
vm.runInNewContext = function(code, sandbox, filename) {};

/**
 * @param {string} code
 * @param {vm.Context} context
 * @param {string=} filename
 */
vm.runInContext = function(code, context, filename) {};

/**
 * @param {Object.<string,*>=} initSandbox
 * @return {vm.Context}
 * @nosideeffects
 */
vm.createContext = function(initSandbox) {};

/**
 * @constructor
 */
vm.Script = function() {};

/**
 * @param {string} code
 * @param {string=} filename
 * @return {vm.Script}
 * @nosideeffects
 */
vm.createScript = function(code, filename) {};

/**
 */
vm.Script.prototype.runInThisContext = function() {};

/**
 * @param {Object.<string,*>=} sandbox
 */
vm.Script.prototype.runInNewContext = function(sandbox) {};
