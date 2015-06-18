


/**
 * @namespace
 */
var path = {};


/**
 * @param {string} p
 * @return {string}
 */
path.normalize = function(p) {};


/**
 * @param {...string} var_paths
 * @return {string}
 */
path.join = function(var_paths) {};


/**
 * @param {!Array.<string>} from
 * @param {string} to
 */
path.resolve = function(from, to) {};


/**
 * @param {string} from
 * @param {string} to
 * @return {string}
 */
path.relative = function(from, to) {};


/**
 * @param {string} p
 * @return {string}
 */
path.dirname = function(p) {};


/**
 * @param {string} p
 * @param {!Array.<string>} ext
 * @return {string}
 */
path.basename = function(p, ext) {};


/**
 * @param {string} p
 * @return {string}
 */
path.extname = function(p) {};


/**
 * @type {string}
 */
path.sep;


/**
 * @type {string}
 */
path.delimiter;
