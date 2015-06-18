/**
 * @namespace
 */
var etcd = {};


/**
 * @typedef {{
 *   key:string,
 *   value:(string|undefined),
 *   nodes:(!Array.<!etcd.Node>|undefined)
 * }}
 */
etcd.Node;


/**
 * @typedef {{
 *   action:string,
 *   node:(!etcd.Node|undefined)
 * }}
 */
etcd.Result;


/**
 * @typedef {?function(Error, (etcd.Result|string))}
 */
etcd.Callback;


/**
 * @param {string} key
 * @param {string} value
 * @param {!etcd.Callback} callback
 */
etcd.set = function(key, value, callback) {};


/**
 * @param {string} key
 * @param {!(etcd.Callback|Object)} callback
 * @param {!etcd.Callback=} opt_callback
 */
etcd.get = function(key, callback, opt_callback) {};


/**
 * @param {string} key
 * @param {!etcd.Callback} callback
 */
etcd.del = function(key, callback) {};
