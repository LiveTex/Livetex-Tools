

/**
 * @type events.EventEmitter
 */
var cluster;

/**
 * @typedef {{exec: string, args: Array.<string>, silent: boolean}}
 */
cluster.Settings;

/**
 * @type {cluster.Settings}
 */
cluster.settings;

/**
 * @type {boolean}
 */
cluster.isMaster;

/**
 * @type {boolean}
 */
cluster.isWorker;

/**
 * @param {cluster.Settings=} settings
 */
cluster.setupMaster = function(settings) {};

/**
 * @param {Object.<string,*>} env
 * @return {cluster.Worker}
 */
cluster.fork = function(env) {};

/**
 * @param {function()=} callback
 */
cluster.disconnect = function(callback) {};

/**
 * @type {?cluster.Worker}
 */
cluster.worker;

/**
 * @type {?Object.<string,cluster.Worker>}
 */
cluster.workers;

/**
 * @constructor
 * @extends events.EventEmitter
 */
cluster.Worker = function() {};

/**
 * @type {string}
 */
cluster.Worker.prototype.id;

/**
 * @type {child_process.ChildProcess}
 */
cluster.Worker.prototype.process;

/**
 * @type {boolean}
 */
cluster.Worker.prototype.suicide;

/**
 * @param {Object} message
 * @param {*=} sendHandle
 */
cluster.Worker.prototype.send = function(message, sendHandle) {};

/**
 */
cluster.Worker.prototype.destroy = function() {};

/**
 */
cluster.Worker.prototype.disconnect = function() {};
